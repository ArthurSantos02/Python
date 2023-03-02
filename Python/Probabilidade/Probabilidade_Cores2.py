#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

# lista de cores do sorteio
colors = ['azul', 'amarelo', 'vermelho']

# função para determinar a cor com maior probabilidade
def most_common_color(draws):
    counts = [draws.count(color) for color in colors]
    index = np.argmax(counts)
    return colors[index]

# exemplo de lista de registros de sorteios
draws = ['azul', 'amarelo', 'vermelho', 'vermelho', 'amarelo', 'azul', 'amarelo']

# determina a cor com a maior probabilidade
most_common = most_common_color(draws)

# exibe a cor com a maior probabilidade
print("A cor com a maior probabilidade de ser escolhida é:", most_common)

*Para(criar, um, aplicativo, Android, que, permita, que, o, usuário, selecione, uma, cor, a, cada, resposta, e,, em, seguida,, mostre, a, cor, com, maior, probabilidade, de, ser, escolhida, com, base, nas, respostas, anteriores,, você, precisará, de, uma, interface, de, usuário, que, permita, que, o, usuário, selecione, as, cores, e, um, componente, de, lógica, para, processar, as, respostas, do, usuário.)

A interface do usuário pode ser criada usando as ferramentas de interface do usuário do Android, como o Android Studio. Você pode criar uma tela com três botões, cada um correspondendo a uma cor, e um contador para exibir quantas respostas foram recebidas. Você pode usar uma variável para manter a lista de respostas do usuário.

A lógica para determinar a cor com a maior probabilidade de ser escolhida com base nas respostas anteriores pode ser implementada como uma função em Python, como mostrado no exemplo anterior. Você pode integrar essa função ao seu aplicativo Android usando uma biblioteca Python para Android, como o Kivy ou o BeeWare. Essas bibliotecas permitem que você escreva aplicativos Android usando a linguagem Python.

Uma vez que o usuário tenha respondido a 15 perguntas, você pode chamar a função para determinar a cor com a maior probabilidade de ser escolhida e exibir o resultado na tela.

Espero que essas orientações sejam úteis para você implementar essa funcionalidade em um aplicativo Android!*/

