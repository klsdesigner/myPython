import sched
import time
from datetime import datetime, timedelta
import subprocess

# Função para executar o arquivo .exe
def execute_script():
    try:
        subprocess.run(['C:\\caminho\\para\\seu\\arquivo.exe'], check=True)
        print('Script executado com sucesso.')
    except subprocess.CalledProcessError as e:
        print(f'Erro ao executar o script: {e}')

# Função para executar o arquivo .py
# def execute_script():
#     try:
#         subprocess.run(['python', '/caminho/para/seu/script.py'], check=True)
#         print('Script executado com sucesso.')
#     except subprocess.CalledProcessError as e:
#         print(f'Erro ao executar o script: {e}')

# Função para agendar o envio diário
def schedule_daily_tasks(hours):
    s = sched.scheduler(time.time, time.sleep)
    
    def schedule_next_task():
        now = datetime.now()
        for hour, minute in hours:
            next_run = now.replace(hour=hour, minute=minute, second=0, microsecond=0)
            
            if now >= next_run:
                next_run += timedelta(days=1)
            
            delay = (next_run - now).total_seconds()
            s.enter(delay, 1, execute_script)
            print(f'Tarefa agendada para {next_run}')
        
        # Reagendar para o próximo dia
        next_day = now.replace(hour=0, minute=0, second=0, microsecond=0) + timedelta(days=1)
        delay_until_next_day = (next_day - now).total_seconds()
        s.enter(delay_until_next_day, 1, schedule_next_task)
    
    schedule_next_task()
    s.run()

# Lista de horários (hora, minuto)
horarios = [(8, 0), (12, 30), (13, 30), (16, 0), (16, 15), (17, 45)]

# Chamada principal para iniciar o agendamento
if __name__ == "__main__":
    schedule_daily_tasks(horarios)
