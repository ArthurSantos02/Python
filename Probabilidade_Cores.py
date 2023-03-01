#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# define o tamanho da janela de tempo
WINDOW_SIZE = 3

# lista para armazenar as cores recebidas
colors = []

# função para determinar a próxima cor provavelmente escolhida
def next_color():
    counts = [colors.count('azul'), colors.count('amarelo'), colors.count('vermelho')]
    return ['azul', 'amarelo', 'vermelho'][np.argmax(counts)]

# loop infinito para receber as cores a cada janela de tempo
while True:
    # recebe as três cores
    color1, color2, color3 = input("Digite três cores separadas por vírgula (azul, amarelo, vermelho): ").split(",")
    color1, color2, color3 = color1.strip(), color2.strip(), color3.strip()
    
    # adiciona as cores à lista
    colors.append(color1)
    colors.append(color2)
    colors.append(color3)
    
    # se a lista tiver mais do que WINDOW_SIZE elementos, remove os elementos mais antigos
    if len(colors) > WINDOW_SIZE:
        colors = colors[-WINDOW_SIZE:]
    
    # determina a próxima cor provavelmente escolhida
    next_col = next_color()
    
    # exibe a próxima cor com maior probabilidade de ser escolhida
    print("A próxima cor com maior probabilidade de ser escolhida é:", next_col)

