# Importa a biblioteca Turtle como 't' e a biblioteca Math como 'm'
import turtle as t
import math as m
# Importa todas as funções da biblioteca Turtle e Math para facilitar o acesso
from turtle import *
from math import *

def desenha_creeper(x, y, tamanho_quadrado):
    # Calcula as coordenadas dos pontos para desenhar o Creeper
    def draw_dot(c1, c2, d):
        t.penup()
        t.goto(x - c1 + tamanho_quadrado / 2, y + c2 - tamanho_quadrado / 2)
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        for _ in range(2):
            t.forward(d)
            t.left(90)
            t.forward(d)
            t.left(90)
        t.end_fill()
        t.penup()

    # Define as coordenadas do Creeper em relação ao centro do quadrado
    draw_dot(-0.2 * tamanho_quadrado, 0.2 * tamanho_quadrado, 0.15 * tamanho_quadrado)
    draw_dot(0.1 * tamanho_quadrado, 0.2 * tamanho_quadrado, 0.15 * tamanho_quadrado)
    draw_dot( -0.05 * tamanho_quadrado, 0.05 * tamanho_quadrado, 0.15 * tamanho_quadrado)
    draw_dot(0.025 * tamanho_quadrado, -0.025 * tamanho_quadrado, 0.15 * tamanho_quadrado)
    draw_dot(-0.125 * tamanho_quadrado, -0.025 * tamanho_quadrado, 0.15 * tamanho_quadrado)
    draw_dot(0.1 * tamanho_quadrado, -0.175 * tamanho_quadrado, 0.075 * tamanho_quadrado)
    draw_dot(-0.125 * tamanho_quadrado, -0.175 * tamanho_quadrado, 0.075 * tamanho_quadrado)

# Função que calcula a distância entre dois pontos
def distancia(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return m.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Função recursiva para desenhar o fractal
def quadrado_T_recursivo(nivel_inicial, nivel_final, anterior_da_anterior_coordenada, anterior_coordenada, atual_coordenada, tamanho_quadrado, angulo):
    if nivel_inicial > nivel_final:
        return
    else:
        for i in range(len(anterior_coordenada)):
            retirar = i
            t.penup()
            t.setpos(anterior_coordenada[i])
            t.setheading(90)
            t.forward(floor(tamanho_quadrado/2))
            t.pendown()
            t.left(angulo)
            t.forward(floor(tamanho_quadrado/2))

            t.begin_fill() 
            for _ in range(4):
                if nivel_inicial == 0:
                    anterior_coordenada.append(t.pos())
                    t.left(angulo)
                    t.forward(tamanho_quadrado)
                else:
                    atual_coordenada.append(t.pos())
                    t.left(angulo)
                    t.forward(tamanho_quadrado) 
            t.end_fill()

            # Chama a função para desenhar o Creeper no quadrado atual
            desenha_creeper(t.xcor(), t.ycor(), tamanho_quadrado)
            t.fillcolor("green")

        # Caso nivel inicial 0, separa as coordenadas anteriores das atuais
        if nivel_inicial == 0:
            for _ in range(-1, retirar, +1):
                anterior_da_anterior_coordenada.append(anterior_coordenada[0])
                anterior_coordenada.pop(0)

        # Caso nivel inicial acima de 1, cria um vetor de vetores de 4 elementos com as coordenadas dos vertices dos quadrados, comparando cada vetor com o seu 
        # ponto de refência anterior_ao_anterior mais próximo. A coordenada do vetor que estiver mais próxima a esse ponto de referência será eliminada, não 
        # podendo ser desenhado quadrado nela.
        else:
            vetor_de_vetores = [atual_coordenada[i:i+4] for i in range(0, len(atual_coordenada), 4)]

            for j in range(len(anterior_da_anterior_coordenada)):
                quadrados_existentes = 4
                if nivel_inicial >= 2:
                    quadrados_existentes = 3

                for _ in range(quadrados_existentes):
                    if vetor_de_vetores:
                        vertices = vetor_de_vetores[0]
                        vetor_de_vetores.pop(0)
                    
                    ponto_referencia = anterior_da_anterior_coordenada[j]
                    menor_distancia = float('inf')
                    ponto_mais_proximo = None

                    for vertice in vertices:
                        d = distancia(ponto_referencia, vertice)
                        if d < menor_distancia:
                            menor_distancia = d
                            ponto_mais_proximo = vertice

                    for k in range(len(atual_coordenada) - 1):
                        if atual_coordenada[k] == ponto_mais_proximo:
                            atual_coordenada.pop(k)
            
            # Coordenadas são atualizaas para a próxima passagem
            anterior_da_anterior_coordenada.clear()
            anterior_da_anterior_coordenada.extend(anterior_coordenada)
            anterior_coordenada.clear()
            anterior_coordenada.extend(atual_coordenada)
            atual_coordenada.clear()
            
        # Nivel inicial soma 1 e o tamanho do quadrado é dividido por 2
        quadrado_T_recursivo(nivel_inicial + 1, nivel_final, anterior_da_anterior_coordenada, anterior_coordenada, atual_coordenada, floor(tamanho_quadrado / 2), angulo)

# Configurações estéticas
t.Screen().title("Fractal Quadrado T")
t.pencolor("black")
t.fillcolor("green")
t.hideturtle()
t.speed(100)

# Define as variáveis que serão utilizadas
nivel_inicial = 0
nivel_final = t.numinput("Fractal Quadrado T", "Por favor, insira até qual nível deseja ir:")
anterior_da_anterior_coordenada = []
anterior_coordenada = [(0.0, 0.0)]
atual_coordenada = []
tamanho_quadrado = 250
angulo = 90

# Chama a função recursiva
quadrado_T_recursivo(nivel_inicial, nivel_final, anterior_da_anterior_coordenada, anterior_coordenada, atual_coordenada, tamanho_quadrado, angulo)

t.Screen().exitonclick()