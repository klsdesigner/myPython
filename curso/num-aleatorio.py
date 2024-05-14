import random

# valor = random.randint(1, 60)
# print(valor)

# print('Gerar 6 números aleatórios entre 1 e 60: \n')
# for i in range(6):
#     n = random.randint(1,60)
#     print(f'Números gerados: {n}')

# valor = random.random()
# print(f'Número gerado: { round(valor * 10, 2)}')

# valor = random.uniform(1, 100)
# print(f'Número: {round(valor, 4)}')

L = [2,4,6,19,20,54,65,30,9, 31,]
# n = random.choice(L)
# print(f'Número escolhido: {n}')

# n = random.sample(L,3)
# print(f'Lista de números escolhidos: {n}')

# EMBARALHAR
print(f'\nLista Original: {L}')
print(f'Lista embaralhada: ', end='')
n = random.shuffle(L)
print(L)