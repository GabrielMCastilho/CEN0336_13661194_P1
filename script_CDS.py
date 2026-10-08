# Nessa primeira parte as variáveis são recebidas do comando pelo usuário e tranformadas. Após isso há um loop de verificação do formato para a string e um para os inteiros. 

import sys

seq = sys.argv[1]
n1 = int(sys.argv[2])
n2 = int(sys.argv[3])
n3 = int(sys.argv[4])
n4 = int(sys.argv[5])
n5 = int(sys.argv[6])
n6 = int(sys.argv[7])
coordenadas = [n1, n2, n3, n4, n5, n6]

if str(seq):
    seq = str(seq)
else:
    print(f'ERRO: Formato de {seq} errado')

contador = 0
for n in coordenadas:
    if int(n):
        n = int(n)
    else:
        print(f'ERRO: Formato de {n} errado')

    if n > len(seq):
        print(f'ERRO: coordenada {n} maior que o tamanho da sequência')
        sys.exit()
    coordenadas[contador]=n
    contador += 1

# Nessa segunda parte há o ajuste das coordenadas segundo o sistema de notação do python e a atribuição das sequências codificantes através das coordenadas aplicadas à sequência principal. Após isso há uma etapa de verificação de códons de início e códons de terminação, culminando na concatenação das regiões codificantes se estiver tudo certo ou em uma mensagem de erro se estiver algo errado. 
n1 -= 1
n3 -= 1
n5 -= 1

CDS1 = seq[n1:n2]
CDS2 = seq[n3:n4]
CDS3 = seq[n5:n6]

if CDS1[0:3] == 'ATG' and (CDS3[-3:] in ('TAG', 'TAA', 'TGA')):
    print(f'Região codificante: {CDS1+CDS2+CDS3}')
else:
    print('ERRO: Sequência não possuí o gene de interesse ou as coordenadas foram inseridas incorretamente')


