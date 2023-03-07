#importação das biblioteca.
from ast import Break
import Funcoes_matematicas as fm

#Declaração de variáveis.
i = 'S'

#Estrutura de loop para a calculadora.
while (i == 'S' or i== 's'):
    
    #Solicitação do tipo de calculo que será realizado.
    calculo = input(
        ' A para Adiçao \n M para multipicação \n S para subtração \n D para divisão \n\n Diga qual operação deseja realizar: ')
    print('\n') 
    
    #Estrutura para verificar a resposta.
    while (calculo != 'A' or calculo !='a' or calculo != 'S' or calculo !='s' or calculo != 'M' or calculo !='m' or calculo != 'D' or calculo !='d'): 
        if (calculo == 'A' or calculo == 'a'):
            break
        elif (calculo == 'S' or calculo == 's'):
            break
        elif (calculo == 'M' or calculo == 'm'):
            break
        elif(calculo == 'D' or calculo == 'd'):
            break
        else:
            print('Digite uma resposta valida!\n')
            calculo = input ('Tente novamente: '); print('\n')   
            
    #Inclusão dos valores que serão calculados e verificação dos tipos de dados inseridos
    num1 = input('Digite um valor:')
    
    while not num1.isdigit():
            print ('Erro: Digite um numeral!')
            num1 = input('Tente novamente:')

    num2 = input('Digite outro valor:'); print('\n')
    
    while not num2.isdigit():
            print ('Erro: Digite um numeral!')
            num2 = input('Tente novamente:')
    n1= float(num1)
    n2= float(num2)

    #Laço de repetição para realizar o calculo definido.
    if (calculo == 'A' or calculo == 'a'):
        print ('O Resultado da sua operação é:', (fm.adc(n1, n2)),'\n')
    elif (calculo == 'S' or calculo == 's'):
        print ('O Resultado da sua operação é:', (fm.sub(n1, n2)),'\n')
    elif (calculo == 'M' or calculo == 'm'):
        print ('O Resultado da sua operação é:', (fm.mult(n1, n2)),'\n')
    elif(calculo == 'D' or calculo == 'd'):
        print ('O Resultado da sua operação é:', (fm.div(n1, n2)),'\n')
 
    # Condicional para execução do loop da calculadora      
    contin = str(input ('Deseja realizar outro calculo? (S/N): \n' ))
    
    #Estrutura de formatação da resposta
    while (contin != 'S' or contin !='N' or contin != 's' or contin !='n'): 
        if (contin == 'N' or contin == 'n'): 
            break                  
        elif (contin == 'S' or contin == 's'):
            break
        else:
            print('Digite uma resposta valida!\n')
            contin = str(input ('Tente novamente: '))
            
    i = contin


