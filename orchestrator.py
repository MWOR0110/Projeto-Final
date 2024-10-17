import os
from Modulo_Nivel_1.module_01 import lv_01_main
from Modulo_Nivel_2.module_02 import lv_02_main

def orchestrator(hostname, password, search_level):
    
    if search_level == 1:
        score, log_file_path = lv_01_main(hostname, password)
    if search_level == 2:
        score, log_file_path = lv_02_main(hostname, password)
    
    return score, log_file_path
