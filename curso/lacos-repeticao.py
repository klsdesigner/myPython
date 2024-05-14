# while
# num = 1

# while (num <= 10):
#     print(num)
#     num += 1

# print('Laço encerrado!')    

# nome = None

# while True:
#     print('Digite seu nome ou x para parar:')
#     nome = input()
#     if nome == 'x' or nome == 'X':
#         break
#     print(f'Bem-vindo, {nome}')
# print('Até logo!')    

# LAÇO FOR
# lista = [2,6,9,4,0,12,3,7]
# for item in lista:
#     print(item)

# palavra = 'kleber'
# for letra in palavra:
#     print(letra)

# for numero in range(10):
#     print(numero)

# for numero in range(1, 11):
#     print(numero)

# nome = input('Digite seu nome: ')
# for x in range(10):
#     print(f'{x+1} {nome}')

# for x in range(2,21,3):
#     print(x)

# for x in range(20,1,-2):
#     print(x)

# pedras = ('Rubi', 'Esmeralda', 'Laranja', 'Safira', 'Diamante', 'Turmalina')
# for pedra in pedras:
#     if pedra == 'Laranja':
#         continue
#     print(pedra)

# LAÇOS ENCADEADOS
# for cont_ex in range(1,6):
#     print(f'\nRodada: {cont_ex}')
#     for cont_in in range(5,0,-1):
#         print(f'valor: {cont_in}')
# print('Fim dos laços!')        

# import random

# for A in range(1,7):
#     print(f'\nRodada: {A}')
#     for B in range(6):
#         num = random.randint(1, 60)
#         print(f'Números: {num}')
# print('\nFim dos laços!\n')       

# import datetime
# data = datetime.datetime.now().time()
# horas = data.strftime("%H:%M:%S") + ".{:02d}".format(data.second)
# print(data)