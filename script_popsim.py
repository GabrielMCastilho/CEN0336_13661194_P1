#A primeira parte do script recebe as informações do usuário e identifica se estão no formato correto


Pi = int(input('Digite o tamanho inicial da população: '))
r = float(input('Digite a taxa de crescimento anual (em decimal): '))
t = int(input('Digite o número de anos: ')) 

if int(Pi):
    Pi = Pi
else: 
    print('ERRO: Formato da população inválida')

if int(t):
    t+=1
else: 
    print('ERRO: Formato da taxa errado')

if float(r):
    r=r
else:
    print('ERRO: Formato do número de anos inválido')

# A segunda parte utiliza loop para fazer o cálculo de população de um determinado ano considerando a população incial, a taxa de crescimento e o ano por um determinado número de anos

Pt=0

for t in range(t):
    Pt = Pi * (1+r)**t
    if t>0:
        print(f'População no ano {t}: {Pt}')





