'''
Faça um programa que peça ao usuário um número e imprima todos os números de um até o número que o usuário informar.
💡 Exemplo: Se o usuário informar o número 5, seu programa deverá imprimir: 1 2 3 4 5.
'''

inputNumero = int(input ('Insira um número de 1 a 10: '))

contador = 1 

while contador <= inputNumero:
  print(contador) 

  contador = contador + 1

# Ou

inputNumero = int(input ('Insira um número de 1 a 10: '))

numero = inputNumero + 1

for variavel in range(1, numero):
  print(variavel)