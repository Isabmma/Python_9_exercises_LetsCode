'''
Crie uma função que recebe o valor do raio de um círculo como parâmetro e retorna o valor da área desse círculo. Lembrando que a área de círculo é dada pela equação: 
A = ℼ r^2.

💡 Dica: Para utilizar um valor mais preciso do pi (ℼ), você pode importar a biblioteca math, e utilizar o math.pi, como ilustrado no código abaixo: 
import math
print(math.pi)
'''

import math

def circle_area(radius_circle):
  area_circle = math.pi * ((radius_circle)**2)
  return print(f'A área do circulo é de: {area_circle}')

input_radius_circle = int(input('Insira o valor do raio de um círculo:'))
print(circle_area(input_radius_circle))
