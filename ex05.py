'''
Vamos fazer um programa para verificar quem é o assassino de um crime. Para descobrir o
assassino, a polícia faz um pequeno questionário com 5 perguntas onde a resposta só pode ser sim ou não:

1. Mora perto da vítima?
2. Já trabalhou com a vítima?
3. Telefonou para a vítima?
4. Esteve no local do crime?
5. Devia para a vítima?

Cada resposta sim dá um ponto para o suspeito. A polícia considera que os suspeitos com 5
pontos são os assassinos, com 4 a 3 pontos são cúmplices e 2 pontos são apenas suspeitos,
necessitando de outras investigações. Valores abaixo de 2 são liberados.
No seu programa, você deve fazer essas perguntas e, de acordo com as respostas do usuário, você vai informar como a polícia o considera.
'''


def question():
    print("Pesquisa de caso da polícia")
    pontos = 0

    # Questionário & Soma dos Pontos
    for variavel in range(1, 6):
        if variavel == 1:
            pergunta1 = str(
                input("1. Mora perto da vítima? Responda com 'sim' ou 'não'").upper())
            if pergunta1 == "SIM":
                pontos = pontos + 1
        elif variavel == 2:
            pergunta2 = str(
                input("2. Já trabalhou com a vítima? Responda com 'sim' ou 'não'").upper())
            if pergunta2 == "SIM":
                pontos = pontos + 1
        elif variavel == 3:
            pergunta3 = str(
                input("3. Telefonou para a vítima? Responda com 'sim' ou 'não'").upper())
            if pergunta3 == "SIM":
                pontos = pontos + 1
        elif variavel == 4:
            pergunta4 = str(
                input("4. Esteve no local do crime? Responda com 'sim' ou 'não'").upper())
            if pergunta4 == "SIM":
                pontos = pontos + 1
        elif variavel == 5:
            pergunta5 = str(
                input("5. Devia para a vítima? Responda com 'sim' ou 'não'").upper())
            if pergunta5 == "SIM":
                pontos = pontos + 1

    # Classificação
    class1 = (pontos == 5)
    class2 = (pontos == 4) or (pontos == 3)
    class3 = (pontos == 2)
    class4 = (pontos == 1) or (pontos == 0)

    # Consideração
    resposta1 = "Consideração: Possível Assassino"
    resposta2 = "Consideração: Possível Cúmplice"
    resposta3 = "Consideração: Possível Suspeito"
    resposta4 = "Consideração: Não Suspeito"
    resposta5 = "Consideração: Não Identificado, refazer pesquisa"

    # Exibição do Resultado
    if class1:
        return (print(resposta1))
    elif class2:
        return (print(resposta2))
    elif class3:
        return (print(resposta3))
    elif class4:
        return (print(resposta4))
    else:
        return (print(resposta5))


question()
