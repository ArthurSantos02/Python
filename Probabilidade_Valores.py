#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
from scipy.stats import norm

# define o tamanho da janela de tempo
WINDOW_SIZE = 3

# lista para armazenar os valores recebidos
values = []

# função para determinar o próximo valor provavelmente será
def next_value():
    mean = np.mean(values)
    std = np.std(values)
    lower_bound = mean - std
    upper_bound = mean + std
    prob_lower = norm.cdf(lower_bound, mean, std)
    prob_upper = norm.cdf(upper_bound, mean, std)
    prob_between = prob_upper - prob_lower
    return mean + (prob_between / 2) * std

# loop infinito para receber os valores a cada janela de tempo
while True:
    # recebe os três valores
    val1, val2, val3 = input("Digite três valores separados por vírgula: ").split(",")
    val1, val2, val3 = float(val1), float(val2), float(val3)
    
    # adiciona os valores à lista
    values.append(val1)
    values.append(val2)
    values.append(val3)
    
    # se a lista tiver mais do que WINDOW_SIZE elementos, remove os elementos mais antigos
    if len(values) > WINDOW_SIZE:
        values = values[-WINDOW_SIZE:]
    
    # determina o próximo valor provavelmente será
    next_val = next_value()
    
    # exibe o próximo valor com maior probabilidade de vir
    print("O próximo valor com maior probabilidade de vir é:", next_val)

