import subprocess  # Importa subprocess para executar comandos no terminal
import platform  # Identifica o sistema operacional

def salvar_log(mensagem):
    """ Salva mensagens de log em um arquivo de texto """
    with open("log_execução.txt", "a") as arquivo:  # Abre o arquivo no modo de escrita
        arquivo.write(mensagem + "\n")  # Adiciona a mensagem ao arquivo, com quebra de linha

def monitor_processos():
    """ Obtém a lista de processos ativos no sistema operacional """
    
    sistema = platform.system()  # Identifica o sistema operacional
    print(f"Sistema operacional detectado: {sistema}")  # Exibe no terminal qual SO foi detectado
    
    # Define o comando correto baseado no sistema operacional
    if "Windows" in sistema:
        # Usa PowerShell para listar os 3 processos mais ativos por uso da CPU
        comando = 'powershell "Get-Process | Sort-Object CPU -Descending | Select-Object -First 3 | Format-Table Name, Id, CPU, WorkingSet"'
    
    elif "Linux" in sistema:
        # Usa ps para listar os 3 processos com maior uso de CPU
        comando = "ps -eo pid,%cpu,%mem,cmd --sort=-%cpu | head -3"

    else:
        return "Sistema não suportado"  # Retorna mensagem de erro para sistemas não reconhecidos

    # Executa o comando no terminal e captura a saída
    resultado = subprocess.run(comando, shell=True, stdout=subprocess.PIPE, text=True)
    
    # Retorna os processos ativos ou informa que nenhum foi encontrado
    if resultado.stdout.strip():
        return resultado.stdout
    else:
        return "Nenhuma informação de processos encontrada!"