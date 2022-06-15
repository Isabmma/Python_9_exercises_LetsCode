'''
Faça um programa que leia as coordenadas de 2 (dois) pontos em um plano cartesiano 2D: a
coordenada x do primeiro ponto (x_1), a coordenada y do primeiro ponto (y_1), a coordenada x do segundo ponto (x_2) e a coordenada y do segundo ponto (y_2). 
Em seguida, calcule a distância euclidiana entre os pontos, utilizando a equação abaixo:
d = raiz[(x2 - x1)² + (y2 - y1)²]
'''
import math

ponto1 = []
ponto2 = []

x1 = float(input("Insira a coordenada X1: "))
ponto1.append(x1)

y1 = float(input("Insira a coordenada Y1: "))
ponto1.append(y1)

x2 = float(input("Insira a coordenada X2: "))
ponto2.append(x2)

y2 = float(input("Insira a coordenada Y2: "))
ponto2.append(y2)

print(ponto1, ponto2)

distancia_euclidiana = math.sqrt(
    ((ponto2[0] - ponto1[0])**2) + ((ponto2[1] - ponto1[1])**2))
print(distancia_euclidiana)
