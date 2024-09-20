import socket
import subprocess
import re
import concurrent.futures

# Função para descobrir o gateway padrão (IP do roteador) no Windows
def obter_ip_roteador():
    try:
        proc = subprocess.Popen("route print", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        saida, erro = proc.communicate()

        if erro:
            print(f"Erro ao executar o comando: {erro.decode('utf-8')}")
            return None

        saida = saida.decode('cp437')  # Codificação padrão do Windows
        linhas = saida.splitlines()

        # Encontrar a linha que contém o gateway padrão
        for linha in linhas:
            if '0.0.0.0' in linha:
                partes = re.split(r'\s+', linha.strip())
                if len(partes) > 2:
                    return partes[2]

        return None

    except Exception as e:
        print(f"Erro ao obter o IP do roteador: {e}")
        return None

# Função para verificar se uma porta está aberta
def verificar_porta(ip_roteador, porta):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout de 1 segundo
        resultado = sock.connect_ex((ip_roteador, porta))  # Tenta conectar ao IP do roteador na porta específica
        sock.close()

        if resultado == 0:
            return porta  # Se a conexão foi bem-sucedida, a porta está aberta
    except:
        return None
    return None

# Função para verificar todas as portas em paralelo


def verificar_portas_abertas(ip_roteador):
    portas_abertas = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=1000) as executor:  # Define o número de threads
        futures = {executor.submit(verificar_porta, ip_roteador, porta): porta for porta in range(1, 65536)}
        for future in concurrent.futures.as_completed(futures):
            porta_aberta = future.result()
            porta = futures[future]  # Obtém o número da porta associado à future
            if porta_aberta:
                print(f"Porta {porta} está aberta.")  # Exibe a porta que está aberta separadamente
                portas_abertas.append(porta)  # Adiciona a porta aberta à lista

    return portas_abertas

# Função principal para verificar portas
def main():
    try:
        ip_roteador = obter_ip_roteador()
        if not ip_roteador:
            print("Não foi possível obter o IP do roteador.")
            return

        print(f"IP do roteador: {ip_roteador}")

        # Verificar todas as portas no roteador
        portas_abertas = verificar_portas_abertas(ip_roteador)

        if portas_abertas:
            print(f"Portas abertas encontradas: {portas_abertas}")
        else:
            print("Nenhuma porta aberta encontrada.")

    except Exception as e:
        print(f"Erro no processo principal: {e}")

# Executar o código
main()