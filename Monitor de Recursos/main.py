import monitor_cpu  # Importa módulo para monitoramento de CPU
import gerenciador_processos  # Gerencia processos simulados
import monitor_memoria  # Importa módulo para monitoramento de memória
import time  # Usado para pausas e controle de execução
import monitor_processos  # Importa módulo para monitoramento de processos do sistema
import monitor_rede  # Importa módulo para análise de rede

def salvar_log(mensagem):
    """ Salva mensagens de log em um arquivo de texto """
    with open("log_execução.txt", "a") as arquivo:  # Abre o arquivo em modo de anexação
        arquivo.write(mensagem + "\n")  # Adiciona a mensagem ao arquivo, com quebra de linha

def main():
    """ Função principal que executa o monitoramento do sistema e simulações de processos """
    
    print("Iniciando monitoramento do Sistema...")  

    # Coleta dados do sistema antes das simulações
    uso_cpu = monitor_cpu.obter_uso_cpu()  # Obtém uso da CPU
    uso_memoria = monitor_memoria.uso_memoria()  # Obtém uso da memória
    processos = monitor_processos.monitor_processos()  # Lista processos ativos
    ip_local = monitor_rede.obter_ip_local()  # Obtém IP da máquina
    ping_resultado = monitor_rede.obter_ping()  # Testa conectividade via ping
    pacotes_rede = monitor_rede.obter_pacotes()  # Obtém estatísticas de rede

    # Exibe informações no terminal e salva no log
    print(uso_cpu)  
    print(uso_memoria)
    
    log_inicio = f"\n---EXECUCAO INICIADA ----\nUso da CPU: {uso_cpu}\nUso da Memória: {uso_memoria}\nProcessos Ativos do Sistema: {processos}\n"
    print(log_inicio)
    salvar_log(log_inicio)

    time.sleep(1)  # Pausa de 1 segundo antes de iniciar simulações

    print("\nIniciando gerenciamento de processos...")

    # Inicia simulação de processos
    gerenciador_processos.iniciar_processos()

    print("\nIniciando Monitor de Redes ...")

    # Coleta dados de rede após simulações
    ip_local = monitor_rede.obter_ip_local()
    ping_resultado = monitor_rede.obter_ping()
    pacotes_rede = monitor_rede.obter_pacotes()

    # Salva os resultados da rede no log
    log_mensagem = f"\nMonitoramento de Rede - {time.ctime()}\nIp Local: {ip_local}\n\nTeste de Ping:\n{ping_resultado}\n\nEstatísticas de Rede:\n{pacotes_rede}"
    salvar_log(log_mensagem)

    print(log_mensagem)

    # Finaliza o monitoramento e registra no log
    log_fim = "\nTodos os Processos foram concluídos corretamente!\n--- EXECUCAO FINALIZADA ---\n"
    print(log_fim)
    salvar_log(log_fim)  

# Executa o programa principal
if __name__ == "__main__":
    main()