import schedule
import time 
import subprocess
# from datetime import datetime, time
from schedule import repeat, every

# hoje = datetime.now()

# @repeat(every().second)
def tarefa():
    # colocar a tarefa
    subprocess.run(["C:/Users/Kleber/Desktop/teste-py/contacao.exe"])

# Agendando a execução do executável nos horários especificados
def meusHorarios():
    # Agendando a execução do executável nos horários especificados
    schedule.every().day.at("08:00").do(tarefa)
    schedule.every().day.at("12:30").do(tarefa)
    schedule.every().day.at("13:30").do(tarefa)
    schedule.every().day.at("16:00").do(tarefa)
    schedule.every().day.at("16:15").do(tarefa)
    schedule.every().day.at("17:45").do(tarefa)
    # Agendando o encerramento do programa
    schedule.every().day.at("17:46").do(exit)

def exit_program():
    print("Pressione Enter para sair...")
    input()  # Espera o usuário pressionar Enter
    exit()    

print(f'Script em ação..')

while True:
    print('...')
    schedule.run_pending()
    
    time.sleep(1)   

    if __name__ == "__agendador__":
        meusHorarios() 