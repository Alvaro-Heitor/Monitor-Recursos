import subprocess # Utilizando subprocess para executar comandos no terminal, para não depender de bibliotecas externas

import platform  # Utilizando platform para identificar o sistema operacional

def obter_uso_cpu():

    try : 
        #Define o sistema operacional

        sistema = platform.system()

        # Se for Windows, usa WMIC para obter a carga da CPU

        if sistema == "Windows":
            resultado = subprocess.run(["wmic", "cpu", "get", "loadpercentage"], 
            
            capture_output=True, # Captura a saída do comando
            
            text= True) # Retorna a saída como string, não bytes

            uso_cpu = resultado.stdout.strip().split("\n")[-1] # Processa a saída para obter o valor correto
            return f"Uso da CPU (Windows - WMIC): {uso_cpu}%"

        # Se for Linux, usa MPSTAT para medir o uso da CPU
        elif sistema == "Linux":
            resultado = subprocess.run("mpstat 1 1 | awk '/all/ {print \"\", 100 - $NF, \"%\"}'", 
            
                shell=True, #Permite rodar o comando no shell
           
                capture_output=True , # Captura a saída do comando
           
                text=True) # Retorna a saída como string, não bytes
            
            return f"Uso da CPU (Linux - TOP): {resultado.stdout.strip()}"
        
        # Se o sistema operacional for diferente de Windows ou Linux, retorna um erro

        else:
            return "Sistema Operacional não suportado"
    
        # Se ocorrer algum erro, retorna uma mensagem de erro

    except Exception as e:
        return f"Erro ao obter o uso da CPU: {e}"
