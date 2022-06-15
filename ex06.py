'''
Faça uma função que recebe uma lista de números e retorna a soma dos elementos dessa lista.
'''

def recebe_soma_lista():
    lista = []
    recebe_numero = ""

    print("Vamos criar uma Lista de números - Para encerrar digite 0")

    while recebe_numero != 0:
        recebe_numero = float(input("Insira um número de cada vez: "))

        lista.append(recebe_numero)

    print(lista)

    def somar(lista):
        soma = 0

        for numero in lista:
            soma += numero

        return soma

    resultado = somar(lista)

    return print(f"A soma de todos os valores da lista é: {resultado}")


recebe_soma_lista()
