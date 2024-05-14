# TRABALHANDO COM DATAS

from datetime import date, time, datetime, timedelta
import time as tm

hoje = datetime.now()
# print(hoje)
# print(hoje.strftime('%H:%M:%S'))

# # metodo strtime()
# print(date.today().strftime("%d/%m/%Y")) #formato br
# print(date.today()) #formato usa
# # pega o ano
# print(hoje.year) 
# print(date.today().year)

# print(hoje.strftime("%A")) 

# horaSL = time(hour=16, minute=0, second=0)
# horaVL = time(hour=16, minute=15, second=0)
# horaS = time(hour=17, minute=45, second=0)
# print(horaS)

# data_texto = '24/04/2024'
# formato_data = datetime.strptime(data_texto, '%d/%m/%Y')
# print(formato_data)

# data_nascimento = datetime(day=16, month=12, year=1966, hour=12)
# print(f'Data de nascimento: {data_nascimento}')

# aniversario = datetime.now() - data_nascimento 
# print(f'Faltam {aniversario.days} dias para o aniversário!')

# data br (fromisoformat())
# data = date.fromisoformat("2024-04-24")
# print(data.strftime('%d/%m/%Y'))

## timedelta p + ou -
# data_futuro = datetime.today() + timedelta(days=10)
# print(data_futuro.strftime('%d/%m/%Y'))

## modulo dateutil (datas do futuro ou passado)
from dateutil.relativedelta import relativedelta

# data_atual = datetime.today()
# delta = relativedelta(years=+2, months=+3, days=+10)
# data_futura = data_atual + delta
# print(data_futura.strftime("%d/%m/%Y"))

# Que dia era há 180 dias?
data_passada = datetime.today() + timedelta(days=-180)
print(data_passada.strftime("%d/%m/%Y"))


