'''
Crie um programa que leia um valor qualquer e apresente uma mensagem dizendo em qual
dos seguintes intervalos ([0,25], (25,50], (50,75], (75,100]) este valor se encontra. Caso o valor não esteja em nenhum destes intervalos, deverá ser impressa a mensagem “Fora de intervalo”. Veja alguns exemplo abaixo:

💡 Entrada: 25.01 | Saída: (25,50]
   Entrada: 25.00 | Saída: [0,25]
   Entrada: 100.00 | Saída: (75,100]
   Entrada: -25.02 | Saída: Fora de intervalo

📌 Lembrando que o [ ou ] representa que o valor está contido no intervalo, enquanto o ( ou) representa que o valor associado não está contido no intervalo. Em outras palavras, (75, 100] representa o intervalo que vai de maior que 75 (não incluindo o 75) até menor ou igual 100.

'''

variavel = float(input("Insira um valor. Entrada:"))

first = (variavel <= 25) and (variavel >= 0)
second = (variavel <= 50) and (variavel > 25)
third = (variavel <= 75) and (variavel > 50)
fourth = (variavel <= 100) and (variavel > 75)

if first:
    print('Saída: [0,25]')
elif second:
    print('Saída: (25,50]')
elif third:
    print('Saída: (50,75]')
elif fourth:
    print('Saída: (75,100]')
else:
    print('Saída: Fora de intervalo')
