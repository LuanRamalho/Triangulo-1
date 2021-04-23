from turtle import *
def  triângulo(lado):
    #Desenha um triangulo de lado.
    color('black', 'blue')
    begin_fill()
    for i in range(3):
        forward(lado)
        left(120)
    end_fill()
triângulo(150)
done()
