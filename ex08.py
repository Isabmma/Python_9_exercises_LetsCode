'''
Calcule a soma de mil termos dos inversos dos fatoriais: 1/(1!) + 1/(2!) + 1/(3!) + 1/(4!) + ...
Dica: Use três variáveis:
● um contador;
● uma variável para soma;
● e uma variável para os termos.
Lembre-se de que 4! = 4 * *3 ** 2 * *1, que também é igual a 4 ** 3!.
'''

contador = 1
termo = 0
soma = 0

while contador < 1001:

    # Calculo do fatorial
    base = contador
    fatorial = 1
    while base > 0:
        fatorial = fatorial * base
        base = base - 1

    # Calculo dos termos inversos dos fatoriais
    termo = 1/fatorial

    # Soma dos termos
    soma = soma + termo

    contador = contador + 1

print(soma)
