import os

# Importando cada módulo individualmente
from .logic_components.canal import main as canal
from .logic_components.dns import main as dns
from .logic_components.portas import main as portas
from .logic_components.velocidade import main as velocidade
from .logic_components.aparelhosConectados import main as aparelhosConectados



def lv_01_main(log_file_path):
    score = 0

    # Abrindo o arquivo de log
    with open(log_file_path, 'a') as log_file:
        log_file.write("Modulo 1\n")

        # Executando cada módulo manualmente
        components = {
            'aparelhosConectados': aparelhosConectados,
            'canal': canal,
            'dns': dns,
            'portas': portas,
            'velocidade': velocidade
        }

        for module_name, module in components.items():
            log_file.write(f"Executando o componente: {module_name}\n")

            # Chamando a função do módulo, assumindo que cada módulo tem uma função 'execute'
            if hasattr(module, 'execute'):
                result = module.execute()  # Ajuste conforme a estrutura do seu módulo
                log_file.write(f"Resultado do componente {module_name}: {result}\n")
                score += result
            else:
                log_file.write(f"O módulo {module_name} não tem uma função 'execute'.\n")

    return score
