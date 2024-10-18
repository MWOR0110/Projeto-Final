import os
from Modulo_Nivel_1.module_01 import lv_01_main
from Modulo_Nivel_2.module_02 import lv_02_main
# from Modulo_Nivel_3.module_03 import lv_03_main

def create_log_file():
    log_file_path = os.path.join(os.getcwd(), "log_file.txt")
    
    with open(log_file_path, 'w') as log_file:
        log_file.write("Log iniciado.\n")
    
    return log_file_path

def orchestrator(hostname, password, search_level):
    log_file_path = create_log_file()

    if search_level >= 1:
        score_1 = lv_01_main(log_file_path)
    
    if search_level >= 2:
        score_2 = lv_02_main(log_file_path)
    
    # if search_level >= 3:
    #     score_3 = lv_03_main(log_file_path, hostname, password)
    
    return log_file_path
