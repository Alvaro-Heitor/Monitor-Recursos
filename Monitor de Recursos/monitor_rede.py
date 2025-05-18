import subprocess  # Importa subprocess para executar comandos do sistema
import platform  # Permite detectar o sistema operacional

def salvar_log(mensagem):
    """ Salva mensagens de log em um arquivo de texto """
    with open("log_execucao.txt", "a") as arquivo:  # Abre o arquivo no modo de escrita
        arquivo.write(mensagem + "\n")  # Adiciona a mensagem ao arquivo, com quebra de linha

def obter_ip_local():
    """ Obtém o endereço IP local da máquina """
    
    if platform.system() == "Windows":
        comando = "ipconfig"  # No Windows, usa ipconfig para exibir informações da rede
    elif platform.system() == "Linux":
        comando = "hostname -I"  # No Linux, usa hostname -I para obter o IP local
    else:
        return "Sistema não suportado!"
    
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    return resultado.stdout  # Retorna o IP local

def obter_ping(site="google.com"):
    """ Realiza um teste de conectividade via ping """
    
    if platform.system() == "Windows":
        comando = f"ping -n 4 {site}"  # No Windows, usa "-n" para definir o número de pacotes
    elif platform.system() == "Linux":
        comando = f"ping -c 4 {site}"  # No Linux, usa "-c" para definir o número de pacotes
    else:
        return "Sistema não suportado!"
    
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    return resultado.stdout  # Retorna o resultado do teste de ping

def obter_pacotes():
    """ Obtém estatísticas de pacotes de rede enviados e recebidos """
    
    if platform.system() == "Windows":
        comando = "netstat -e"  # No Windows, usa netstat -e para exibir estatísticas de rede
    elif platform.system() == "Linux":
        comando = "ip -s link"  # No Linux, usa ip -s link para exibir estatísticas de interface de rede
    else:
        return "Sistema não suportado!"
    
    resultado = subprocess.run(comando, shell=True, capture_output=True, text=True)
    return resultado.stdout.strip()  # Retorna estatísticas de pacotes de rede