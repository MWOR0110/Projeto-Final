import subprocess
import re

# Função para obter informações sobre redes Wi-Fi usando o comando netsh
def obter_info_wifi():
    try:
        # Executar o comando netsh para listar as redes Wi-Fi
        resultado = subprocess.run(['netsh', 'wlan', 'show', 'networks', 'mode=bssid'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if resultado.returncode != 0:
            print("Erro ao executar o comando netsh.")
            print(resultado.stderr)
            return None

        # Processar a saída
        saida = resultado.stdout

        # Dicionário para armazenar as informações sobre as redes Wi-Fi
        redes_wifi = []

        # Expressões regulares para capturar os detalhes relevantes
        regex_ssid = re.compile(r'SSID \d+ : (.+)')
        regex_bssid = re.compile(r'BSSID \d+ : ([0-9A-Fa-f:]+)')
        regex_canal = re.compile(r'Canal\s+: (\d+)')
        regex_sinal = re.compile(r'Sinal\s+: (\d+)%')
        regex_velocidade = re.compile(r'Taxas.*: ([\d\s]+)')
        regex_seguranca = re.compile(r'Autenticaç.* : (.+)')
        regex_criptografia = re.compile(r'Criptografia\s+: (.+)')

        # Variáveis temporárias para armazenar os dados de cada rede
        ssid_atual = None
        bssid_atual = None
        canal_atual = None
        sinal_atual = None
        velocidade_atual = None
        seguranca_atual = None
        criptografia_atual = None

        # Analisar cada linha da saída
        for linha in saida.splitlines():
            # Exibir a linha para depuração
            print(f"Processando linha: {linha}")

            ssid_match = regex_ssid.search(linha)
            bssid_match = regex_bssid.search(linha)
            canal_match = regex_canal.search(linha)
            sinal_match = regex_sinal.search(linha)
            velocidade_match = regex_velocidade.search(linha)
            seguranca_match = regex_seguranca.search(linha)
            criptografia_match = regex_criptografia.search(linha)

            # Se encontrar um SSID, finalize a rede anterior (se houver) e inicie uma nova
            if ssid_match:
                if ssid_atual is not None:
                    redes_wifi.append({
                        'SSID': ssid_atual,
                        'BSSID': bssid_atual,
                        'Canal': canal_atual,
                        'Sinal': sinal_atual,
                        'Velocidade': velocidade_atual,
                        'Segurança': seguranca_atual,
                        'Criptografia': criptografia_atual
                    })

                ssid_atual = ssid_match.group(1)
                bssid_atual = None
                canal_atual = None
                sinal_atual = None
                velocidade_atual = None
                seguranca_atual = None
                criptografia_atual = None

            # Processar o restante das informações
            if bssid_match:
                bssid_atual = bssid_match.group(1)

            if canal_match:
                canal_atual = canal_match.group(1)

            if sinal_match:
                sinal_atual = sinal_match.group(1) + "%"

            if velocidade_match:
                velocidade_atual = velocidade_match.group(1).strip() + " Mbps"

            if seguranca_match:
                seguranca_atual = seguranca_match.group(1).strip()
                print(f"Autenticação capturada: {seguranca_atual}")

            if criptografia_match:
                criptografia_atual = criptografia_match.group(1)

        # Adicionar a última rede processada, se houver
        if ssid_atual is not None:
            redes_wifi.append({
                'SSID': ssid_atual,
                'BSSID': bssid_atual,
                'Canal': canal_atual,
                'Sinal': sinal_atual,
                'Velocidade': velocidade_atual,
                'Segurança': seguranca_atual,
                'Criptografia': criptografia_atual
            })

        return redes_wifi

    except Exception as e:
        print(f"Erro ao obter as informações do Wi-Fi: {e}")
        return None

# Função principal
def main():
    redes_wifi = obter_info_wifi()

    if redes_wifi:
        print(f"{len(redes_wifi)} redes Wi-Fi encontradas:\n")
        for rede in redes_wifi:
            print(f"SSID: {rede['SSID']}")
            print(f"  BSSID: {rede['BSSID']}")
            print(f"  Canal: {rede['Canal']}")
            print(f"  Sinal: {rede['Sinal']}")
            print(f"  Velocidade: {rede['Velocidade']}")
            print(f"  Segurança: {rede['Segurança']}")
            print(f"  Criptografia: {rede['Criptografia']}")
            print("-" * 40)
    else:
        print("Nenhuma rede Wi-Fi encontrada.")

# Executar o código
if __name__ == "__main__":
    main()
