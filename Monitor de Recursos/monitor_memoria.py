import subprocess  # Importa subprocess para executar comandos no sistema
import platform  # Permite identificar o sistema operacional

def uso_memoria():
    """ Obtém informações sobre o uso da memória no Windows e Linux """
    
    try:
        sistema = platform.system()  # Identifica o sistema operacional
        
        # Se for Windows, usa WMIC para obter a quantidade de memória livre
        if sistema == "Windows":
            resultado = subprocess.run(
                ["wmic", "OS", "get", "FreePhysicalMemory"],  # Comando WMIC para capturar a memória disponível
                capture_output=True,  # Captura a saída do comando
                text=True  # Retorna a saída como string (texto)
            )
            memoria_livre_kb = int(resultado.stdout.strip().split("\n")[-1])  # Processa a saída e obtém o valor correto
            memoria_livre_mb = memoria_livre_kb / 1024  # Converte de KB para MB
            
            return f"Memória Livre (Windows - WMIC): {memoria_livre_mb:.2f} MB"

        # Se for Linux, usa o comando `free` para obter os valores de memória
        elif sistema == "Linux":
            resultado = subprocess.run(
                "free -m | grep 'Mem'",  # Comando para obter dados de memória em MB
                shell=True,  # Permite rodar o comando no shell
                capture_output=True,  # Captura a saída do comando
                text=True  # Retorna a saída como string
            )

            # Processa a saída do comando e captura os valores corretos
            dados_memoria = resultado.stdout.strip().split()  # Divide a saída em partes
            memoria_total_mb = dados_memoria[1]  # Memória total disponível
            memoria_usada_mb = dados_memoria[2]  # Memória atualmente em uso
            memoria_livre_mb = dados_memoria[3]  # Memória livre disponível
            
            return f"Memória (Linux - Free): Total: {memoria_total_mb} MB | Livre : {memoria_livre_mb} MB | Usada {memoria_usada_mb} MB"

        # Se o sistema operacional não for suportado
        else:
            return "Sistema operacional não suportado"

    # Captura e retorna erros caso ocorram
    except Exception as e:
        return f"Erro ao obter o uso da memória: {e}"