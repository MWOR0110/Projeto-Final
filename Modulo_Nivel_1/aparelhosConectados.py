import os
import platform
import subprocess
import re

# Função para obter o IP do roteador (Gateway padrão)
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

# Função para pingar um IP
def pingar_ip(ip):
    # Comando de ping depende do sistema operacional
    comando = ['ping', '-n', '1', '-w', '1000', ip] if platform.system().lower() == "windows" else ['ping', '-c', '1', '-W', '1', ip]

    # Executar o comando de ping
    resultado = subprocess.run(comando, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Verificar se o ping foi bem-sucedido
    return resultado.returncode == 0

# Função para escanear a rede e encontrar dispositivos conectados
def escanear_rede(ip_roteador):
    # Definir a faixa de IPs baseada no IP do roteador (assumimos uma máscara de sub-rede /24)
    ip_base = ip_roteador.rsplit('.', 1)[0]  # Ex: se o IP do roteador é 192.168.0.1, base é 192.168.0
    dispositivos = []

    print(f"Escaneando a rede {ip_base}.0/24 ...")

    # Iterar pelos possíveis endereços IP (de 1 a 254)
    for i in range(1, 255):
        ip = f"{ip_base}.{i}"
        if pingar_ip(ip):
            print(f"Dispositivo encontrado: {ip}")
            dispositivos.append(ip)

    return dispositivos

# Função principal
def main():
    ip_roteador = obter_ip_roteador()
    if not ip_roteador:
        print("Não foi possível obter o IP do roteador.")
        return

    print(f"IP do roteador: {ip_roteador}")

    # Escanear a rede para encontrar dispositivos conectados
    dispositivos_conectados = escanear_rede(ip_roteador)

    if dispositivos_conectados:
        print("Dispositivos conectados encontrados:")
        for ip in dispositivos_conectados:
            print(f"IP: {ip}")
    else:
        print("Nenhum dispositivo conectado encontrado.")

# Executar o código
if __name__ == "__main__":
    main()