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