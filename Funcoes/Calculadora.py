#importação das biblioteca.
from ast import Break
from re import S
import numpy as np
import Funcoes_matematicas as fm
#Declaração de variáveis.
num1 = 0
n1=0
S =1
#Estrutura de looping para a calculadora.
def calculo():
 while S == 1:
    #Solicitação do tipo de calculo que será realizado.
    calculo = input(' A para Adiçao \n M para multipicação \n S para subtração \n D para divisão \n Diga qual operação deseja realizar: ')

    #Inclusão dos valores que serão calculados everificação dos tipos de dados inseridos
    num1 = input('Digite um valor:')

    while not num1.isdigit():
            print ('Erro: Digite um numeral!')
            num1 = input('Tente novamente:')
        

    num2 = input('Digite outro valor:')

    while not num2.isdigit():
            print ('Erro: Digite um numeral!')
            num2 = input('Tente novamente:')
    n1= float(num1)
    n2= float(num2)

    #Laço de repetição para realizar o calculo definido.
    if (calculo == 'A'):
        print ('O Resultado da sua operação é:', (fm.adc(n1, n2)))
    elif (calculo == 'S'):
        print ('O Resultado da sua operação é:', (fm.sub(n1, n2)))
    elif (calculo == 'M'):
        print ('O Resultado da sua operação é:', (fm.mult(n1, n2)))
    elif(calculo == 'D'):
        print ('O Resultado da sua operação é:', (fm.div(n1, n2)))


    input ('Deseja realizar outro calculo? (S/N): ' )




