# Atvidades do Livro do Sérgio Luiz Banin, "Python3: Conceitos e aplicações"
import random
#4.1 Escreva um programa que leia um string que deve conter,obrigatoriamente, um número inteiro e, caso isso não aconteça, emita uma mensagem de erro.
def validando_entrada_numerica(num1:int):
    if num1.isnumeric():
        return num1
    else: 
        print('Erro: digite apenas números')
print(validando_entrada_numerica('a'))
#4.2 Faça a leitura de uma linha de dados que contenha quatro números separados por espaços em branco e carregue os objetos A, B, C com os valores individuais.
def leitura_varios_numeros(text1):
    splitext = text1.split(' ')
    A = int(splitext[0])
    B = int(splitext[1])
    C = int(splitext[2])
    return (f'A = {A}, B = {B}, C = {C}')
print(leitura_varios_numeros('355 22 87'))
#4.3 Escreva um programa que leia três dados de entrada: o primeiro termo, a razão e a quantidade de termos de uma P.A., todos números inteiros. O programa deve calcular todos os termos, colocando-os em uma lista, e exibila no final.
def criando_pa(P:int,R:int,Qtde:int):
    lista = []
    index = 0
    while index > Qtde:
        lista.append(P)
        P += R
        index +=1
    return lista
print(criando_pa(2, 10, 20))
#4.4 Escreva um programa que permaneça em laço lendo números inteiros enquanto os valores digitados forem diferentes de zero. Cada número não zero digitado deve ser incluído em uma lista. Ao final, exiba a lista e seu tamanho.
def lista_com_numeros(num1:int):
    index = 0
    lista = []
    while index < num1:
        N = input('Digita ae')
        if N == 0:
            break
        else:
            lista.append(N)
print(lista_com_numeros(10))
#4.5 Escreva um programa que leia um número inteiro N e gere uma lista com N elementos aleatórios (utilize a função randint explicada no Exercício resolvido 3.7) entre 10 e 50. Exiba a lista gerada e exiba também a mesma lista com seus elementos ordenados em ordem crescente.
# random
def cria_lista_aleatoria(num1):
    try:
        N = int(num1)
    except ValueError:
        print('Digite um número inteiro')
        return
    L = []
    while len(L) < N:
        item = random.randint(1, 50)
        if item not in L:
            L.append(item)
    L.sort()
    return L       
print(cria_lista_aleatoria(10))
#4.6 Escreva um programa que leia dois números inteiros Lin e Col, que representam, respectivamente, a quantidade de linhas e colunas em uma matriz. Utilizando listas aninhadas, crie uma representação para essa matriz, utilizando a função randint para gerar números para cada posição da matriz. Apresente-a na tela com uma aparência matricial.
# random
def matrix(Lin:int,Col:int):
    M = []
    i = 0
    while i < Lin:
        M.append([])
    j = 0
    while j < Col:
        M[i].append(random.randint(0, 20))
        j += 1
        i += 1
    # return M
    i = 0
    while i < Lin:
        j = 0
        print('|', end='')
    while j < Col:
        print('{0:4}'.format(M[i][j]), end='')
        j+=1
        print(' |')
        i+=1
print(matrix(6,4))
#4.7 A sequência de Fibonacci já foi explicada no Exercício resolvido 3.7. Escreva um programa que gere os N primeiros termos dessa sequência utilizando uma lista para armazená-los. N é um número inteiro a ser lido do teclado e deve, obrigatoriamente, ser maior ou igual a 2.
def lista_fibonacci(N:int):
    L = [0, 1]
    IN = int(N)
    if (IN) < 2:
        print("Digite um número maior que 2")
    for I in range(IN):
        L.append(L[I] + L[I + 1])
    return L
print(lista_fibonacci(10))
#4.8 Escreva um programa que permaneça em laço lendo números inteiros enquanto os valores digitados forem diferentes de zero. Para cada valor digitado, adicione-o a uma lista na posição imediatamente anterior ao primeiro elemento da lista que seja maior ou igual a ele. Exiba a lista no final.
def gerador_lista():
    L = []
    while True:
        N = int(input('Digite um número: '))
        if N == 0:
            break
        else:
            L.append(N)
    return L
print(gerador_lista())
#4.9 Escreva um programa que leia um número inteiro N e gere uma lista com números pares de 2 até N. Se N for par, deve estar incluído na lista. Em seguida, inicie um laço que deve permanecer em execução enquanto x for diferente de zero. Para cada valor de x fornecido, o programa deve informar se x está ou não na lista.
def busca_sequencial(N:int):
    L = list(range(2,N+1,2))
    num1 = 1
    while num1 != 0:
        num1 = int(input('Digite um número'))
        if num1 in L:
            print(f'{num1} está na lista')
        elif num1 not in L:
            print(f'{num1} não está na lista')
    return L
print(busca_sequencial(20))
#4.10 O algoritmo de busca binária é significativamente mais rápido que o de busca sequencial quando aplicado a grandes conjuntos de dados. Porém, ele requer que a lista esteja ordenada. A ideia básica implementada nesse algoritmo é verificar se o valor procurado “x” está na posição central da lista. Se estiver, então, o valor foi encontrado e o algoritmo termina. Caso não esteja e x seja menor que o valor central, então, a busca prossegue na metade à esquerda do centro; caso seja maior, a busca prossegue na metade à direita.
def busca_binaria(N: int):
    L = list(range(2, N + 1, 2))
    num1 = int(input('Digite um número'))
    ini = 0
    fim = len(L) - 1
    while ini <= fim:
        meio = (ini + fim) // 2
        if num1 == L[meio]:
            print(f'{num1} está na lista')
            return
        elif num1 < L[meio]:
            fim = meio - 1
        else:
            ini = meio + 1
    print(f'{num1} não está na lista')
print(busca_binaria(20))
#4.11 Escreva um programa que ordene uma lista não ordenada utilizando o algoritmo Bubble Sort. Em Python, para ordenar uma lista de qualquer tamanho, basta utilizar o método sort ou a função sorted, que estão prontos e já foram mencionados neste capítulo. Portanto, o objetivo deste exercício é mostrar e explicar a lógica do algoritmo para o leitor que está iniciando
def ordena_bolha():
    L = [17, 4, 23, 8, 19, 12]
    Trocou = 1
    while Trocou:
        Trocou = 0
        i = 0
        while i < len(L) - 1:
            if L[i] > L[i+1]:
                L[i],L[i+1] = L[i+1],L[i]
                Trocou = 1
            i+=1
    return L
print(ordena_bolha())
#Exercícios propostos
#1. Escreva um programa que leia do teclado uma lista com tamanho de 10 elementos e exiba-a na tela na ordem inversa à ordem de leitura.
def ordem_leitura():
    L = []
    for index in range(10):
        L.append(input('Digite um número'))
    L.reverse() # L[::-1]
    return L
print(ordem_leitura())
#2. Escreva um programa que leia do teclado duas listas com tamanho 10, com números inteiros. Em seguida, o programa deve juntar as duas listas em uma única com o tamanho 20.
def lista_dupla():
    L1, L2 = [], []
    for index in range(10):
        L1.append(int(input('Digite um número')))
    for index in range(10):
        L2.append(int(input('Digite um número')))
    return L1 + L2
print(lista_dupla())
#3.Escreva um programa que preencha com números inteiros duas listas denominadas A e B com diferentes tamanhos nA e nB,respectivamente. Em seguida, o programa deve juntar as duas em uma única lista com o tamanho nA + nB. Exibir na tela a lista resultante.
#random
def preenche_lista(size1:int,size2:int):
    L1, L2 = [], []
    for index in range(size1):
        L1.append(int(random.randint(1, 50)))
    for index in range(size2):
        L2.append(int(random.randint(1, 50)))
    return L1 + L2
print(preenche_lista(5,7))
#4. Escreva um programa que leia uma lista com N números inteiros, em que N é um número inteiro previamente digitado pelo usuário. O programa não deve aceitar um número digitado que já esteja inserido na lista, sendo que, quando essa situação ocorrer, uma mensagem deve ser dada ao usuário. Por fim, exibir na tela a lista resultante.
def lista_unica():
    L = []
    index = 0
    while index < 10:
        N = int(input('Digite um número'))
        if N in L:
            print('Número já inserido')
            index = index
        else:
            L.append(N)
            index += 1
    return L
print(lista_unica())
#5. Escreva um programa que leia do teclado dois números inteiros nA e nB e leia também duas listas denominadas A e B com os tamanhos nA e nB, respectivamente. Na leitura de cada uma das listas é obrigatório que não sejam aceitos valores repetidos. Em seguida, o programa deve juntar as duas em uma única lista R (resultante), tomando o cuidado de que R não tenha valores duplicado.
def lista_unica(nA:int,nB:int):
    A, B = [], []
    index = 0
    while index < nA:
        N = int(input('Digite um número'))
        if N in A:
            print('Número já inserido')
            index = index
        else:
            A.append(N)
            index += 1
    index = 0
    while index < nB:
        N = int(input('Digite um número'))
        if N in B:
            print('Número já inserido')
            index = index
        else:
            B.append(N)
            index += 1
    return A + B
print(lista_unica(2,5))
#6. Escreva um programa que leia três dados de entrada: o primeiro termo, a razão e a quantidade de termos de uma P.A., todos números inteiros. O programa deve calcular todos os termos, colocando-os em uma lista, e exibi-la no final. Esse exercício já foi resolvido e explicado no Capítulo 3 (veja Exercício resolvido 3.2). A diferença, aqui, é que se pede para utilizar uma lista para armazenar os diversos termos antes de exibi-los.
def razao_pa(size:int):
    L, index = [], 0
    while index < size:
        A = int(input('Digite o valor de A'))
        B = int(input('Digite o valor de B'))
        index += 1
        if B == 0:
            print('Não é possível calcular a divisão')
        else:
            L.append(A/B)
    return L
print(razao_pa(2))
#7. Escreva um programa que leia um número N obrigatoriamente entre 0 e 50 e, em seguida, leia N números reais em uma lista A. O programa deve separar os valores lidos em A em outras duas listas NEG e POS:a primeira contendo somente os valores negativos e a segunda contendo os valores positivos e zero. Apresentar na tela as listas NEG e POS e a quantidade de valores contidos em cada uma.
#random
def valores_contidos():
    N, A, L, NEG, POS = [], [], [], [], []
    while len(N) < 10:
        N.append(int(random.randint(0, 50)))
    while len(A) < 10:
        A.append(int(input('Digite um valor para A')))
    L = N + A
    for index in range(len(L)):
        print(L[index])
        if L[index] > 0:
            POS.append(L[index])
        elif L[index] < 0:
            NEG.append(L[index])
        else:
            print('Número zero. Ignorando.')
    return f'Numeros positivos: {POS}\nNumeros negativos: {NEG}'
print(valores_contidos())
#8. Escreva um programa que leia um número N (entre 0 e 50) e, em seguida, defina uma lista V preenchendo-a com N números inteiros aleatórios (utilizar a função randint). Exiba-a na tela. Inicie um laço no qual será feita a leitura de um número X e que termina quando X for zero. Pesquise se X está ou não na lista V e, caso esteja, elimine todas as suas ocorrências.
def ocorrencias(X:int):
    V = []
    while len(V) < 10:
        V.append(int(random.randint(0, 50)))
    for index in range(len(V)):
        #print(f'{V}')
        if V[index-2] == X:
            print(f'Achamos o numero {X} na posição {index}')
            V.remove(X)
    return V
print(ocorrencias(2))