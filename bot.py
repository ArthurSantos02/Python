#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tkinter as tk
import numpy as np

class ColorPickerApp:
    def __init__(self, master):
        self.master = master
        master.title("Color Picker App")

        # lista de cores
        self.colors = ['azul', 'amarelo', 'vermelho']

        # contador de respostas
        self.count = 0

        # lista de respostas
        self.responses = []

        # botões das cores
        self.blue_button = tk.Button(master, text="Azul", command=lambda: self.add_response('azul'))
        self.yellow_button = tk.Button(master, text="Amarelo", command=lambda: self.add_response('amarelo'))
        self.red_button = tk.Button(master, text="Vermelho", command=lambda: self.add_response('vermelho'))

        # botão para calcular a cor mais provável
        self.calculate_button = tk.Button(master, text="Calcular", command=self.calculate_most_common)

        # contador de respostas
        self.count_label = tk.Label(master, text="Respostas: 0")

        # posicionamento dos widgets
        self.blue_button.grid(row=0, column=0, padx=10, pady=10)
        self.yellow_button.grid(row=0, column=1, padx=10, pady=10)
        self.red_button.grid(row=0, column=2, padx=10, pady=10)
        self.calculate_button.grid(row=1, column=1, padx=10, pady=10)
        self.count_label.grid(row=2, column=1, padx=10, pady=10)

    def add_response(self, color):
        self.responses.append(color)
        self.count += 1
        self.count_label.config(text="Respostas: {}".format(self.count))

    def calculate_most_common(self):
        if len(self.responses) >= 15:
            counts = [self.responses.count(color) for color in self.colors]
            index = np.argmax(counts)
            most_common = self.colors[index]
            result_window = tk.Toplevel(self.master)
            result_label = tk.Label(result_window, text="A cor mais provável é {}".format(most_common))
            result_label.pack()
        else:
            error_window = tk.Toplevel(self.master)
            error_label = tk.Label(error_window, text="Você precisa responder pelo menos 15 vezes!")
            error_label.pack()

root = tk.Tk()
app = ColorPickerApp(root)
root.mainloop()

