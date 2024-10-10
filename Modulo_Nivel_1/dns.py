import subprocess
import re

# Função para obter os servidores DNS configurados no sistema
def obter_servidor_dns():
    try:
        # Executa o comando para obter as informações de rede
        proc = subprocess.Popen("ipconfig /all", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        saida, erro = proc.communicate()

        if erro:
            print(f"Erro ao executar o comando: {erro.decode('utf-8')}")
            return None

        saida = saida.decode('cp437')  # Codificação padrão do Windows
        linhas = saida.splitlines()

        # Procura as linhas que contêm o servidor DNS
        servidores_dns = []
        capturando_dns = False  # Para detectar se estamos capturando DNS

        for linha in linhas:
            # Verifica se a linha contém "Servidores DNS"
            if "Servidores DNS" in linha:
                capturando_dns = True  # Inicia a captura de servidores DNS
                continue

            # Quando capturando, procurar por IPs válidos
            if capturando_dns:
                # Verifica se a linha contém um endereço IP válido (IPv4 ou IPv6)
                ip_match = re.search(r'(\d{1,3}\.){3}\d{1,3}|([a-fA-F0-9:]+:+)+[a-fA-F0-9]{1,4}', linha)
                if ip_match:
                    servidores_dns.append(ip_match.group())  # Adiciona o IP à lista de servidores DNS
                else:
                    # Se encontrar uma linha sem IP válido, termina a captura de DNS
                    capturando_dns = False

        return servidores_dns

    except Exception as e:
        print(f"Erro ao obter os servidores DNS: {e}")
        return None

# Função principal para exibir os servidores DNS
def main():
    try:
        servidores_dns = obter_servidor_dns()
        if not servidores_dns:
            print("Não foi possível obter os servidores DNS.")
            return

        print("Servidores DNS configurados:")
        for dns in servidores_dns:
            print(f"- {dns}")

    except Exception as e:
        print(f"Erro no processo principal: {e}")

# Executar o código
if __name__ == "__main__":
    main()
