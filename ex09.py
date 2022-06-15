'''
Crie (manualmente ou sorteando os números) uma lista de 10 números e imprima:
1. uma lista com os 4 primeiros números;
2. uma lista com os 5 últimos números;
3. uma lista contendo apenas os elementos das posições pares;
4. uma lista contendo apenas os elementos das posições ímpares;
5. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro);
6. uma lista inversa dos 5 primeiros números;
7. uma lista inversa dos 5 últimos números.
'''

import random

randomlist = []
for i in range(0, 10):
    n = random.randint(1, 100)
    randomlist.append(n)

print(randomlist)

# 1. uma lista com os 4 primeiros números;
first_4 = randomlist[:4]
print(first_4)

# 2. uma lista com os 5 últimos números;
last_5 = randomlist[5:10]
print(last_5)

# 3. uma lista contendo apenas os elementos das posições pares;
position_even = randomlist[1:10:2]
print(position_even)

# 4. uma lista contendo apenas os elementos das posições ímpares;
position_odd = randomlist[0:10:2]
print(position_odd)

# 5. a lista inversa da lista sorteada (isto é, uma lista que começa com o último elemento da lista sorteada e termina com o primeiro);
invert_list = randomlist[::-1]
print(invert_list)

# 6. uma lista inversa dos 5 primeiros números;
first_5 = randomlist[:5]
first_5_invert = first_5[::-1]
print(first_5_invert)

# 7. uma lista inversa dos 5 últimos números.
last_5_invert = last_5[::-1]
print(last_5_invert)
