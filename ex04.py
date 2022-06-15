'''
Faça um programa que peça 2 números inteiros e um número real, calcule e mostre:
a) o produto entre o dobro do primeiro e a metade do segundo.
b) a soma entre o triplo do primeiro e o terceiro.
c) o terceiro elevado ao cubo.
'''

int1 = int(input("1) Insira um número inteiro:"))
int2 = int(input("2) Insira um número inteiro:"))
float1 = float(input("3) Insira um número real:"))

count1 = (2*int1) * (int2/2)
count2 = (3*int1) * (float1)
count3 = (float1) ** 3

print(count1, count2, count3)
