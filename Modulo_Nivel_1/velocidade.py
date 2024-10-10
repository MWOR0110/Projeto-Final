import subprocess
import re
import speedtest

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

# Função para testar a velocidade da conexão
def testar_velocidade():
    try:
        st = speedtest.Speedtest()
        print("Selecionando o melhor servidor...")
        st.get_best_server()

        print("Testando a velocidade de download...")
        download_speed = st.download() / 1_000_000  # Convertendo para Mbps
        print("Testando a velocidade de upload...")
        upload_speed = st.upload() / 1_000_000  # Convertendo para Mbps

        return download_speed, upload_speed

    except Exception as e:
        print(f"Erro ao testar a velocidade: {e}")
        return None, None

# Função principal para verificar a velocidade da internet
def main():
    try:
        ip_roteador = obter_ip_roteador()
        if not ip_roteador:
            print("Não foi possível obter o IP do roteador.")
            return

        print(f"IP do roteador: {ip_roteador}")

        # Testar a velocidade da conexão
        download_speed, upload_speed = testar_velocidade()

        if download_speed is not None and upload_speed is not None:
            print(f"Velocidade de Download: {download_speed:.2f} Mbps")
            print(f"Velocidade de Upload: {upload_speed:.2f} Mbps")
        else:
            print("Falha ao medir a velocidade.")

    except Exception as e:
        print(f"Erro no processo principal: {e}")

# Executar o código
if __name__ == "__main__":
    main()
