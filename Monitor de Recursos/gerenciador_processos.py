import subprocess  # Importa subprocess para executar comandos no terminal
import time  # Utilizado para simulações com temporizações
import monitor_processos  # Importa função para monitorar processos do sistema
import sys  # Permite identificar o sistema operacional

def salvar_log(mensagem):
    """ Salva mensagens de log em um arquivo de texto """
    with open("log_execução.txt", "a") as arquivo:  # Abre o arquivo no modo de escrita
        arquivo.write(mensagem + "\n")  # Adiciona a mensagem ao arquivo, com quebra de linha

def iniciar_processos():
    """ Inicia processos simulados e monitora antes e depois da execução """
    
    # Define o comando correto para rodar Python dependendo do sistema operacional
    python_cmd = "python3" if sys.platform != "win32" else "python"

    # Obtém processos ativos antes das simulações
    processos_antes = monitor_processos.monitor_processos()
    
    print("⏳ Iniciando processos...")  
    print("\nMonitoramento dos processos nativos antes das simulações:\n", processos_antes)
    salvar_log(f"\nMonitoramento dos processos nativos antes das simulações:\n{processos_antes}\n")

    print("\nIniciando simulações")
    salvar_log("\nSimulações:")

    # Processo 1 - Simulação de uma tarefa simples com delay
    p1 = subprocess.Popen([python_cmd, "-c", "import time; print('[Processo 1] Iniciando...'); time.sleep(3); print('[Processo 1] Finalizado!' )"])
    print(f"Processo 1 iniciado! (PID: {p1.pid})")
    salvar_log(f" Processo 1 Iniciado! (PID: {p1.pid})")
    p1.wait()  # Aguarda a conclusão do processo
    salvar_log(f" Processo 1 Concluído! (PID: {p1.pid})")
    print(f"Processo 1 concluído! (PID: {p1.pid})\n")

    # Processo 2 - Simulação de um contador que imprime valores sequenciais
    p2 = subprocess.Popen([python_cmd, "-c", "import time; print('[Processo 2] Contagem iniciada...'); [print(f'[Processo 2] Contador: {i}') or time.sleep(1) for i in range (5)]; print('[Processo 2] Finalizado!')"])
    print(f"Processo 2 Iniciado! (PID: {p2.pid})")
    salvar_log(f" Processo 2 iniciado! (PID: {p2.pid})")
    p2.wait()
    salvar_log(f" Processo 2 Concluído! (PID: {p2.pid})")
    print(f"Processo 2 concluído! (PID: {p2.pid})\n")

    # Processo 3 - Simulação de execução de uma tarefa simples
    p3 = subprocess.Popen([python_cmd, "-c", "import time; print('[Processo 3] Executando uma tarefa...'); time.sleep(2); print('[Processo 3] Finalizado!')"])
    print(f"Processo 3 Iniciado! (PID: {p3.pid})")
    salvar_log(f" Processo 3 iniciado! (PID: {p3.pid})")
    p3.wait()
    salvar_log(f" Processo 3 Concluído! (PID: {p3.pid})")
    print(f"Processo 3 concluído! (PID: {p3.pid})\n")

    # Obtém processos ativos após as simulações
    processos_depois = monitor_processos.monitor_processos()

    print("\nMonitoramento de processos nativos após as simulações:\n", processos_depois)
    salvar_log(f"\nMonitoramento de processos nativos depois das simulações:\n{processos_depois}\n")
    
    print("\nTodas as simulações concluídas!")