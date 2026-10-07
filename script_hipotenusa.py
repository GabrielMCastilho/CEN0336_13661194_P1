#Importa a biblioteca sys, possibilitando receber inputs do terminal, e criar os argumentos que serão recebidos e transforma eles em inteiros. Se não for possível transformá-los em inteiros, será dado um código de erro.
import sys

a = sys.argv[1]
b = sys.argv[2]

if int(a):
   a = int(a) 
else:
    print('ERRO: A primeira entrada fornecida não é um número inteiro')

if int(b):
    b = int(b)
else: 
    print('ERRO: A segunda entrada fornecida não é um número inteiro')

# Nessa parte o script realiza a operação que irá descobrir o quadrado da hipotenusa e armazena em Z. Após isso, gera uma saída de texto padrão com os devidos valores das variáveis a, b e Z
Z = (a**2)+(b**2)

print(f'O quadrado da hipotenusa para o triângulo retângulo com lados a={a} e b={b}, é {Z}')


