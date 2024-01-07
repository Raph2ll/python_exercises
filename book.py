# Atvidades do Livro do Sérgio Luiz Banin, "Python3: Conceitos e aplicações"
import random
import time
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
#9. O programa deverá ler dois inteiros chamados Min e Max. Min pode ser qualquer valor e Max, obrigatoriamente, deve ser maior que Min. Em seguida, preencher uma lista com todos os valores divisíveis por 7 contidos no intervalor fechado [Min, Max]. Exibir a lista resultante n tela.
def min_max(MIN:int,MAX:int):
    L = []
    if MIN > MAX:
        return f'max: {MAX} deve ser maior que min: {MIN}'
    while MIN < MAX:
        if MIN % 7 == 0:
            L.append(MIN)
        MIN += 1
    return L
print(min_max(2,1))
#10. Escreva um programa que leia do teclado uma lista com N elementos. Em seguida, o programa deve eliminar os elementos que estiverem repetidos, mantendo apenas a primeira ocorrência de cada. Apresentar a lista resultante na tela. Os valores eliminados devem ser armazenados em outra lista que também deve ser exibida.
def lista_repetida(size:int):
    L , L2 = [], []
    while len(L) < size:
        N = int(input('Digite um número'))
        if N in L:
            L2.append(N)
        else:
            L.append(N)
    return L2, L
print(lista_repetida(10))
#11. Faça um programa que leia um número inteiro N bem grande (acima de 5.000). Preencha uma lista de tamanho N com números inteiros aleatórios positivos. Em seguida, inicie um laço de pesquisa, no qual o valor a ser pesquisado deve ser lido do teclado, e o programa deve dizer se tal valor está ou não contido na lista, bem como dizer sua posição. No caso de várias ocorrências, exibir todas. O laço de pesquisa termina quando for digitado o zero. Use o algoritmo de busca sequencial.
#random
def bem_grande(N:int):
    L = []
    if N <= 5000:
        print('Por favor, digite um número maior que 5000.')
        return
    for index in range(N):
        L.append(int(random.randint(1, 50)))
    while True:
        pesquisa = int(input('Digite o valor a ser pesquisado (ou 0 para sair): '))
        if pesquisa == 0:
            print('Pesquisa encerrada')
            return
        elif pesquisa in L:
            indices_encontrados = [i for i, valor in enumerate(L) if valor == pesquisa]
            print(f'O valor {pesquisa} foi encontrado nas posições: {indices_encontrados}')
print(bem_grande(5003))
#12. Escreva um programa que leia do teclado duas matrizes de dimensões 2×2 e mostre na tela a soma dessas duas matrizes.
def matrizes(size1:int,size2:int):
    matriz1, matriz2 = [], []
    for _ in range(size1):
        l1 = int(input('Digite l1'))
        l2 = int(input('Digite l2'))
        matriz1.append([l1,l2])
    for _ in range(size2):
        l1 = int(input('Digite l1'))
        l2 = int(input('Digite l2'))
        matriz2.append([l1,l2])
    return matriz1 + matriz2
print(matrizes(4,4))
#13. Escreva um programa que leia do teclado duas matrizes de dimensões 2×2 e mostre na tela a multiplicação dessas duas matrizes.
def matrizes2(size: int):
    matriz1, matriz2, ret = [], [], []

    for _ in range(size):
        l1 = int(input('Digite l1'))
        l2 = int(input('Digite l2'))
        matriz1.append([l1, l2])

    for _ in range(size):
        l1 = int(input('Digite l1'))
        l2 = int(input('Digite l2'))
        matriz2.append([l1, l2])


    for i in range(size):
        for j in range(size):
                ret.append(matriz1[i][j] * matriz2[i][j])
    return ret
print(matrizes2(2))
#14. A matriz a seguir mostra o custo unitário de cada produto e a quantidade de cada um dos produtos no estoque de três lojas de uma rede. Escreva um programa que exiba na tela as respostas para as perguntas. Na solução desse problema, elabore uma maneira de armazenar seus dados utilizando lista e sublistas. Os dados da matriz devem ser lidos do teclado.
def matriz_produtos():
    M = [
    [72.35, 373, 558, 358],
    [43.93, 1228, 1448, 907],
    [17.84, 4135, 2059, 3122],
    [23.19, 1139, 1450, 843]
    ]

    loja1, loja2, loja3 = 0, 0, 0

    produtoA = M[0][0] * (M[0][1] + M[0][2] + M[0][3])
    produtoB = M[1][0] * (M[1][1] + M[1][2] + M[1][3])
    produtoC = M[2][0] * (M[2][1] + M[2][2] + M[2][3])
    produtoD = M[3][0] * (M[3][1] + M[3][2] + M[3][3])

    for linha in M:
        loja1 += linha[0] * linha[1]
        loja2 += linha[0] * linha[2]
        loja3 += linha[0] * linha[3]
       
    print(f'Valor total de estoque da loja 1: R${loja1}, loja 2: R${loja2}, loja 3: R${loja3}')
    
    print(f'Valor de estoque do produto A: R${produtoA}, produto B: R${produtoB}, produto C: R${produtoC}, produtoD: R${produtoD}')

    print(f'Valor de estoque de todos os produtos{loja1 + loja2 + loja3}')
print(matriz_produtos())
#5.1 Escreva uma função que receba como parâmetro de entrada um número inteiro N. Ela deve retornar 1 se N for primo ou 0, caso não seja. Esse problema já foi discutido no Exercício resolvido 3.4. Considerações para a solução: na função serão considerados apenas números maiores que 1. O número 2 é o único par que é primo.
def numeros_primos(N:int):
    if N <= 1:
        return 0
    elif N == 2:
        return 1
    elif N % 2 == 0:
        return 0
    else:
        # Verifica divisibilidade a partir de 3 até a raiz quadrada do número
        for i in range(3, int(N**0.5) + 1, 2):
            if N % i == 0:
                return 0
        return 1
print(numeros_primos(int(input('Digite um número'))))
#5.2 Escreva uma função que receba duas listas L1 e L2 como parâmetro de entrada e retorne uma lista que seja a interseção de L1 e L2, em que uma lista interseção é aquela que contém os elementos que estejam presentes em ambas, L1 e L2.
def intersecao_listas(L1,L2):
    L = []
    for index in L1:
        if index in L2:
            L.append(index)
    return L
print(intersecao_listas([2,3,4,5,6], [2,3,5,6,7]))
#5.3 Suponha que uma lista está carregada com diversos números inteiros. Escreva uma função recursiva que calcule a soma desses valores. Para testar essa função, use a lista L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], cuja soma resulta = 55.
def soma_lista_recursiva(L):
    if not L:
        return 0
    else:
        return L[0] + soma_lista_recursiva(L[1:])
print(soma_lista_recursiva([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]))
#5.4 Escreva uma função que recebe dois parâmetros: uma lista L contendo números inteiros e organizada em ordem crescente; um número inteiro N. Essa função deve verificar se N está contido em L utilizando o algoritmo de busca binária e retornar à posição em que ele se encontra ou retornar 0 caso N não esteja na lista.
def busca_binaria_recursiva(lista, alvo, inicio, fim):
    if inicio <= fim:
        meio = (inicio + fim) // 2
        valor_meio = lista[meio]

        if valor_meio == alvo:
            return meio 
        elif valor_meio < alvo:
            return busca_binaria_recursiva(lista, alvo, meio + 1, fim)
        else:
            return busca_binaria_recursiva(lista, alvo, inicio, meio - 1)
    return 0  
lista_ordenada = [3,8,11,14,16,19,25,29,31,37,42,46,53,58,60,63,71,82]
numero_alvo = 7

print(busca_binaria_recursiva(lista_ordenada, numero_alvo, 0, len(lista_ordenada) - 1))
#Exercícios propostos
#1. Escreva uma função que recebe um número inteiro como parâmetro de entrada e retorna o texto “PAR” ou “ÍMPAR”
def par_impar(N:int):
    if N % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'
print(par_impar(2))
#2. Utilize a função EPrimo desenvolvida no Exercício resolvido 5.1 para carregar uma lista contendo os N primeiros números primos, em que N é um número inteiro fornecido pelo usuário.
def numeros_primos(N, L):
    ret = []
    for num in L:
        if num <= 1:
            continue
        elif num == 2:
            ret.append(num)
        elif num % 2 == 0:
            continue
        else:
            is_prime = True
            for i in range(3, int(num**0.5) + 1, 2):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                ret.append(num)
            if len(ret) == N:
                break
    return ret
print(numeros_primos(5, [2, 2, 2, 2, 2, 2, 3, 2, 2, 2]))
#3. Escreva uma função que receba dois números inteiros A e B como parâmetros de entrada e retorne 1 se A for divisível por B e 0 caso contrário.
def divide(A, B):
    if A % B == 0:
        return 1
    return 0
print(divide(5,2))
#4. Escreva uma função que receba um número inteiro N e retorne uma lista com os bits 0 e 1, que representam N convertido para binário. Não use nenhuma função Python de conversão para binários. Em vez disso, elabore uma lógica baseada no processo de divisões sucessivas.
def converte_binario(N:int):
    if N == 0:
        return [0]

    bits = []

    while N > 0:
        bits += [N % 2]
        N = N // 2

    return bits
print(converte_binario(5))
#5. Escreva uma função que receba como parâmetro de entrada uma lista L de números inteiros e um valor. A função deve retornar quantas vezes o valor está contido na lista. Caso ele não esteja em L, retorne 0.
def contar_ocorrencias(lista, valor):
    return lista.count(valor)
print(contar_ocorrencias([2,2,2,2], 2))
#6. Escreva um programa que receba como parâmetro de entrada um número inteiro de 5 dígitos no intervalo fechado [10000, 30000] que represente códigos de produtos vendidos em uma loja. A função deve calcular e retornar o dígito verificador utilizando regra de cálculo explicada a seguir. Considere o código 21853, em que cada dígito é multiplicado por um peso começando em 2, os valores obtidos são somados, e do total obtido calcula-se o resto de sua divisão por 7.
def base_7(N:int):
    ret = 0
    if N < 10000 or N > 30000:
        return 'Digite um valor entre 10000 e 30000'
    for index, digito in enumerate(str(N), start=2):
        ret += index * int(digito)
    return ret % 7
print(base_7(21853))
#7. Escreva uma função que receba como parâmetro de entrada dois números reais Min e Max. Essa função deve ler do teclado um número real e retorná-lo caso esteja dentro do intervalo fechado [Min, Max]. Caso contrário, a função deve exibir uma mensagem de erro e ler um novo valor.
#Não faço ideia do pq o N dps de digitar um valor errado retorna none.
def min_max2(min:int,max:int):
    N = int(input('Digite um número'))
    if N > max or N < min:
        print('erro')
        min_max2(min,max)
    else:
        return N
print(min_max2(2,5))
#8. Escreva uma função que receba uma lista como parâmetro de entrada e retorne uma tupla contendo quatro valores na seguinte ordem: a soma, a média, o menor e o maior valor dentre todos os elementos nela contidos. Considere que nessa lista ocorram apenas números reais. Escreva um programa para testar essa função, exibindo na tela os resultados. Neste exercício, evite utilizar as funções prontas existentes no Python, como sum, min e max.
def retorna_tupla(L:list):
    soma,media,menor,maior = 0, 0, L[0], L[0]

    for index in L:
        soma += index
        if index < menor:
            menor = index
        if index > maior:
            maior = index

    return (soma,media,menor,maior)
print(retorna_tupla([2,3,4,5,6]))
#9. Escreva uma função que receba uma lista L e elimine os eventuais elementos repetidos contidos na mesma, deixando na lista resultante apenas uma ocorrência de cada elemento. Escreva um programa para testar essa função, o qual deve ler do teclado os elementos que farão parte da lista. (veja o Exercício proposto 4.10)
def recebe_lista(L:list):
    return list(set(L))
print(recebe_lista([2,2,2,3,4,5]))
#10. Escreva uma função que receba duas listas L1 e L2 como parâmetro de entrada e retorne uma lista contendo todos os elementos de L1 que não estão em L2. Escreva um programa para testar essa função.
def nao_contem(L1:int,L2:int):
    L = []
    for index in L1:
        if index not in L2:
            L.append(index)
    return L
print(nao_contem([2,2,2,2,2,3,4,5], [6,6,6,6,6,3,4,5]))
#11. Escreva uma função que receba como parâmetro de entrada uma lista L e retorne uma lista organizada em ordem crescente. Para fazer a ordenação, use o Algoritmo de Ordenação Bolha (Bubble Sort). Crie uma segunda versão dessa função que retorne uma lista organizada em ordem decrescente.
def crescente(L:list):
    return sorted(L)
def decrescente(L:list):
    return sorted(L, reverse=True)
# Escreva um programa para testar essas duas funções. Esse programa deve ler um número inteiro N e gerar uma lista com N números inteiros aleatórios utilizando a função randint(). Use as duas funções de ordenação e exiba na tela as listas ordenadas crescente e decrescente.
#random
def testa_lista():
    size = input('Insira o tamanho da lista')
    L = []
    for _ in range(size):
        L.append(random.randint(1, 50))
    
    ret = input('Deseja ordenar a lista de forma crescente?[S/n]')
    if ret != 'S':
        return decrescente(L)
    else:
        return crescente(L)
print(testa_lista())
#12. Escreva um programa que leia um número inteiro Q e exiba na telaos Q primeiros termos da sequência de Fibonacci, utilizando umafunção recursiva para determinar o elemento da sequência a serexibido. A sequência de Fibonacci, já vista nos Exercícios resolvidos3.7 e 4.7, caracteriza-se por um termo ser a soma dos dois anteriores,sendo que os dois primeiros termos são 0 e 1. Assim, os dez primeirostermos são: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34.
def fibonacci(Q: int, L=None):
    if L is None:
        L = [0, 1]
    if Q <= 0:
        return []
    elif Q == 1:
        return [0]
    elif Q == 2:
        return L
    else:
        L.append(L[-1] + L[-2])
        return fibonacci(Q - 1, L)

Q = int(input("Digite o número de termos da sequência de Fibonacci: "))
result = fibonacci(Q)
print(result)

#13. Dada uma lista contendo números inteiros, escreva uma funçãorecursiva para calcular a multiplicação de todos os elementos. Exiba o resultado na tela.
def multiplica(L: list):
    if not L:
        return 1
    else:
        return L[0] * multiplica(L[1:])

print(multiplica([2, 3, 4, 5, 6]))

#14. Faça uma pesquisa sobre o Algoritmo de Ordenação Quicksort. Implemente uma função recursiva que use esse algoritmo para organizar a lista L de forma crescente. Escreva um programa para testar a função.
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

def test_quicksort():
    test_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    sorted_list = quicksort(test_list)
    print("Lista Original:", test_list)
    print("Lista Organizada:", sorted_list)

print(test_quicksort())
#15. Escreva um programa que contenha duas funções de ordenaçãodiferentes: uma que implemente o algoritmo Bubble Sort (criada noExercício 11) e outra que implemente o algoritmo Quicksort (criada no Exercício 14). Escreva um programa que gere uma lista com um tamanho bem grande e utilize-a para testar o desempenho das duas funções.
#random
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"A função {func.__name__} levou {elapsed_time:.6f} segundos para ser executada.")
        return result
    return wrapper


@timing_decorator
def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = [x for x in arr[1:] if x <= pivot]
        greater = [x for x in arr[1:] if x > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)

@timing_decorator 
def crescente(L:list):
    return sorted(L)
#Faça esse programa gerar a lista grande contendo Q elementos, na qual Q é digitado pelo usuário.
def gera_lista(size:int):
    L = []
    for _ in range(size):
        L.append(random.randint(1, 100))
    return L
#Esse valor de Q deve ser bem grande, por exemplo, de 10 a 50 mil elementos, ou mais, dependendo da capacidade de seu computador.
quicksort(gera_lista(8000))
crescente(gera_lista(8000))
#6.1 Escreva um programa que leia do teclado dois conjuntos de números inteiros digitados pelo usuário. Exiba na tela a união e a interseção desses conjuntos. Nessa solução, os conjuntos C1 e C2 foram carregados com os valores lidos do teclado, e ao término os operadores união (|) e interseção (&) foram utilizados para produzir o resultado pedido.
def C1_C2():
    C1, C2 = set(), set()
    N1 , N2 = 1, 1
    while N1 != 0:
        N1 = int(input('Digite um valor para C1'))
        C1.add(N1)
    while N2 != 0:
        N2 = int(input('Digite um valor para C2'))
        C2.add(N2)
    return f'União entre C1 e C2: {C1 | C2}, Interseção: {C1 & C2}'
print(C1_C2())
#6.2 Considere que todos os valores no intervalo fechado [1, 30] devam serdivididos em dois grupos, A e B, de 15 valores cada, de maneira aleatória. Éimportante que um valor que está em A não esteja em B, e vice-versa, bem como que todos os valores do intervalo estejam em algum grupo. Escreva um programa que use os recursos de conjuntos para atingir esse resultado.
#random
def A_B():
    A, B = set(), set()
    while len(A) < 15:
        A.add(random.randint(1, 30))
    while len(B) < 15:
        N = random.randint(1,30)
        if N not in A:
            B.add(N)
    return A, B
print(A_B())
#6.3 Escreva um programa que leia do teclado o código de uma peça e a quantidade disponível no estoque. Esses dois dados de entrada são números inteiros. Acrescente o par código:quantidade em um dicionário apenas se o código não estiver presente. Caso esteja, dê uma mensagem informando essa situação e descarte os dados. O laço termina quando for fornecido 0 para o código. Exibir na tela os dados do dicionário, um membro por linha.
def dicionario():
    pecas = {}
    cod = 1
    while True:
        cod = int(input('Digite o código'))
        if cod == 0:
            break
        elif cod in pecas:
            print(f'O código já existe')
            continue
        estoque = (int(input('Digite quantidade em estoque')))
        pecas[cod] = estoque
        
    return pecas
print(dicionario())
#6.4 Escreva um programa que permaneça em laço efetuando a leitura dos seguintes dados: número de matrícula, nome do aluno, idade e curso. O número de matrícula é a chave, e os demais dados constituem o valor. Faça a leitura desses dados e construa o dicionário enquanto não for digitado zero para o número de matrícula. Nesse problema, têm-se múltiplos dados como valor para cada membro do dicionário, sendo necessário agrupá-los de alguma maneira. Para esse agrupamento pode-se utilizar uma lista, uma tupla, um conjunto ou outro dicionário aninhado. No Exercício resolvido 6.4 será apresentada, inicialmente, uma solução na qual se utiliza uma tupla. No final apresenta-se a mudança necessária para utilizar lista no lugar da tupla e discute-se um pouco sobre a escolha de uma ou outra alternativa. No Exercício resolvido 6.5 será apresentada uma solução com dicionários aninhados. Assim, nesta primeira solução a tupla será organizada de modo que seu primeiro elemento seja o Nome, o segundo seja a Idade e o terceiro seja o Curso do aluno. Veja o código do programa a seguir.
def aluno():
    Alunos = {}
    while True:
        matr = int(input('Digite o número da matricula'))
        if matr == 0:
            break
        elif matr in Alunos:
            print(f'A matricula {matr} já está no cadastro')
            continue
        nome = input('Nome: ')
        idade = input('Idade: ')
        curso = input('Curso: ')
        Alunos[matr] = (nome, idade, curso)
        #Alunos[matr] = [nome, idade, curso]
    #return Alunos
    print('Fim da leitura dos dados\n')
    print('Cadastro de Alunos') # 2ª parte – apresentação dos dados
    for matricula, dados in Alunos.items():
        print(f'Aluno {nome}')
        print(f'Matricula {matr}')
        print(f'Idade {idade}')
        print(f'Curso {curso}')
        print('\nFim do programa')
aluno()
#6.5 Nessa segunda solução nada muda com relação ao número de matrícula, aopasso que os dados passam a ser armazenados em um dicionário aninhado aodicionário Alunos.
def aluno():
    Alunos = {}
    while True:
        matr = int(input('Digite o número da matricula'))
        if matr == 0:
            break
        elif matr in Alunos:
            print(f'A matricula {matr} já está no cadastro')
            continue
        dicItem = {}
        dicItem['nome'] = input(' Nome: ')
        dicItem['idade'] = int(input(' Idade: ')) 
        dicItem['curso'] = input(' Curso: ')
        Alunos[matr] = dicItem 
    #return Alunos
    print('Fim da leitura dos dados\n')
    print('Cadastro de Alunos') 
    for matricula, dados in Alunos.items():
        print(f'Aluno {dados["nome"]}')
        print(f'Matricula {matricula}')
        print(f'Idade {dados["idade"]}')
        print(f'Curso {dados["curso"]}')
        print('\nFim do programa')
aluno()
#1. Escreva um programa que leia do teclado dois conjuntos de nomes de frutas. Em seguida, apresente na tela a união (operador | ), a interseção (&) e a diferença simétrica (^). Utilizando a função len, verifique qual dos conjuntos tem mais elementos e apresente a diferença entre o maior e o menor (–).
def duas_frutas():
    frutas1, frutas2 = set(), set()
    N1 , N2 = 1, 1
    while N1 != '0':
        N1 = str(input('Digite o nome de uma fruta[1]'))
        if N1 == '0':
            continue
        frutas1.add(N1)
    while N2 != '0':
        N2 = str(input('Digite o nome de uma fruta[2]'))
        if N2 == '0':
            continue
        frutas2.add(N2)
    print(frutas1, frutas2)
    print(f'União entre os conjuntos: {frutas1 | frutas2}')
    print(f'Interseção entre os conjuntos: {frutas1 & frutas2} ')
    print(f'Diferença simétrica entre os conjuntos: {frutas1 ^ frutas2}')
    print(f'União entre os conjuntos: {frutas1 | frutas2}')
    if len(frutas1) > len(frutas2):
        print (f'Diferença entre os conjuntos: {frutas1 - frutas2}')
    else: 
        print (f'Diferença entre os conjuntos: {frutas2 - frutas1}')
print(duas_frutas())
#2. Altere o programa do Exercício resolvido 6.2 da seguinte maneira: leia um número inteiro N (N < 30) e faça que o conjunto A tenha tamanho N e o conjunto B tenha tamanho 30-N.
#random
def N_A_B():
    A, B = set(), set()
    
    N = int(input('Digite um número inteiro maior que 1 e menor que 30: '))

    while N <= 1 or N >= 30:
        N = int(input('Digite um número inteiro maior que 1 e menor que 30: '))

    while len(A) < N:
        A.add(random.randint(1, 30))
    ret = 30 - N
    while len(B) < ret:
        num = random.randint(1, 30)
        if num not in A:
            B.add(num)

    return A, B

print(N_A_B())
#3. Escreva um programa que permaneça em laço lendo números inteiros do teclado. Esse laço termina quando for digitado zero ou qualquer valor negativo. O programa deve contar quantas vezes cada valor positivo foi digitado. Ao término do laço de leitura o programa deve mostrar quais valores foram digitados e quantas vezes cada um. Use um dicionário para resolver esse problema.
def dicionario():
    N, ret = 1, dict()

    while N != 0:
        N = int(input('Digite um número: '))
        
        if N in ret:
            ret[N] += 1
        else:
            ret[N] = 1

    return ret

print(dicionario())
#4. Considere o seguinte conjunto de dados: Nome + (N1, N2, N3, N4). Nome representa o nome de um aluno e deve ser usado como chave. N1, N2, N3, N4 representam as notas de provas desse aluno. Escreva um programa que leia os dados de Q alunos e apresente na tela se foram aprovados ou reprovados. O critério que garante a aprovação é que a média aritmética das 4 notas seja maior ou igual 6,0. Q é a quantidade de alunos, e esse valor deve ser lido do teclado no começo do programa. As notas devem ser exibidas com uma casa decimal.
def notas():
    dic = dict()
    while True:
        name = str(input('Digite um nome para o aluno: '))
        if name == '0':
            break
        N1 = int(input('Digite a primeira nota: '))
        N2 = int(input('Digite a segunda nota: '))
        N3 = int(input('Digite a terceira nota: '))
        N4 = int(input('Digite a quarta nota: '))
        dic[name] = [N1, N2, N3, N4]
    for key, value in dic.items():
        if (sum(value) / 4) == 6.0:
            print(f'Aluno:{key}, foi aprovado')
        else: 
            print(f'Aluno:{key}, foi reprovado')
    return dic
print(notas())
#5. Refaça o exercício 4 alterando o critério de aprovação para o seguinte: das quatro notas, despreze a menor e calcule a média aritmética das outras três. Será considerado aprovado o aluno que tiver essa média maior ou igual a 6,0.
def notas2():
    dic = dict()
    while True:
        name = str(input('Digite um nome para o aluno: '))
        if name == '0':
            break
        N1 = int(input('Digite a primeira nota: '))
        N2 = int(input('Digite a segunda nota: '))
        N3 = int(input('Digite a terceira nota: '))
        N4 = int(input('Digite a quarta nota: '))
        dic[name] = [N1, N2, N3, N4]
    for key, value in dic.items():
        if (sum(value) - min(value) / 3) <= 6.0:
            print(f'Aluno:{key}, foi aprovado')
        else: 
            print(f'Aluno:{key}, foi reprovado')
    return dic
print(notas2())
#6. Leia e armazene em um dicionário o nome, a idade e o número do telefone de seus contatos, sendo que a chave deve ser o nome. Ao digitar um string vazio para o nome, o programa interrompe a leitura. Apresente na tela os dados lidos em ordem alfabética pelo nome dos contatos. Em seguida, armazene os contatos em dois dicionários, utilizando como critério a idade: menores de 18 anos em um e os maiores em outro dicionário, eliminando o original. Apresente na tela os dois dicionários resultantes da separação.
def telefone():
    contatos = dict()
    maioridade = dict()
    menoridade = dict()
    while True:
        name = str(input('Digite o nome: '))
        if name == '':
            break
        idade = int(input('Digite a idade: '))
        numero = int(input('Digite o número do telefone: '))
        contatos[name] = [name, idade, numero]

    for key, value in contatos.items():
        if value[1] > 18:
            maioridade[key] = value
        else:
            menoridade[key] = value

    print(f'Pessoas de maior idade: {maioridade}')
    print(f'Pessoas de menor idade: {menoridade}')
    return contatos

print(telefone())
#7.1a Escreva um programa que permaneça em laço lendo números reais até que seja digitado 0. Todos os valores digitados, exceto o zero, devem ser gravados em um arquivo em disco, um por linha, com três casas decimais.
def arquivo_real():
    arq = open('exemplo.txt', 'w')
    while True:
        N = int(input('Digite um número'))
        if N == 0:
            break
        arq.write(f'{N}\n')
    arq.close()
print(arquivo_real())
#7.1b Serão criadas duas soluções para esse exercício. Na primeira será utilizado o método write, e na segunda será utilizado o método writelines.
def arquivo_real2():
    arq, L = open('exemplo.txt', 'w'), []
    while True:
        N = int(input('Digite um número'))
        if N == 0:
            break
        L.append(f'{N}\n')
    arq.writelines(L)
    arq.close()
print(arquivo_real2())
#7.2a Escreva um programa que leia um arquivo texto contendo um número inteiro em cada linha. Exiba na tela e faça a totalização dos valores lidos. Esse exercício será resolvido de duas maneiras diferentes. Na primeira, Exercício resolvido 7.2a, será utilizado um laço while. A leitura da primeira linha do arquivo é feita fora do laço. Caso seu retorno seja diferente de string vazio, o laço é iniciado e prosseguirá até que o final do arquivo seja alcançado. O método readline retorna um string vazio quando a leitura do arquivo chega ao final. A cada repetição do laço o string lido é convertido para inteiro e totalizado no objeto Soma.
def le_arquivo():
    arq, soma = open('./exemplo.txt', 'r'), 0
    S = arq.readline()
    while S != '':
        soma += int(S)
        S = arq.readline()
    arq.close()
    return soma
print(le_arquivo())
#7.2b Essa solução funcionará perfeitamente, porém, existe outra solução bem melhor no que diz respeito ao uso dos recursos da linguagem Python. O Exercício resolvido 7.2b mostra essa outra solução, na qual foi utilizado o conceito de iterador de arquivo (file iterator).
def le_arquivo2():
    arq, soma = open('./exemplo.txt', 'r'), 0
    for S in arq:
        soma += int(S)
    arq.close()
    return soma
print(le_arquivo2())
#7.3 Escreva um programa que leia um arquivo texto que contém diversas linhas que representam uma lista de compras. Em cada linha há três informações: nome de um produto, quantidade e preço unitário, separados pelo caractere “;”. Pede-se que cada item da lista seja exibido na tela, incluindo o valor total do item. Ao final, exiba o total da compra.
def le_csv():
    L, ret = [], 0
    for S in open('exemplo.csv', 'r'):
        S.rstrip()
        L = S.split(',')
        L[1],L[2] = int(L[1]), float(L[2])
        print(f'{L[0]}: {L[1]} x {L[2]} = {L[1]*L[2]}')
        ret += L[1]*L[2]
    return ret
print(le_csv())
#7.4  Escreva um programa que leia um número inteiro N (10 < N < 10.000) e grave um arquivo com N linhas com os dados listados na tabela seguinte. O arquivo deve ter o nome “Estoque.csv” e deve usar o caractere “;” (ponto e vírgula) como delimitador. Não é necessário que o arquivo esteja ordenado.
#random
def estoque_csv():
    arq = open('estoque.csv', 'w')
    cproduto = 0
    while True:
            N = int(input('Digite um valor para N: '))
            if 10 < N < 10000:
                break
            else:
                print('Digite um valor entre 10 e 10.000')
    with open('estoque.csv', 'r') as arquivo:
        linhas = arquivo.readlines()
        while cproduto <= N:
            linhas = arquivo.readlines()
            cproduto += 1
            quantidade = random.randint(1, 3800)
            estoque = random.randint(0, 2500)
            preco = random.uniform(1.80, 435.90)
            aliquota = random.choice([7,12,18])
            arq.write(f'{cproduto};{quantidade};{estoque};{preco:.2f};{aliquota}\n')
    arq.close()
    return 'Estoque criado com sucesso'
print(estoque_csv())
#7.5 Escreva um programa que leia um arquivo com o layout especificado no Quadro 7.3 e apresente os seguintes resultados:
#valor total das mercadorias em estoque;
#valor total do imposto ICMS pago referente a essas mercadorias.
def le_estoque_csv():
    L = []
    valorTotal = 0
    valorTotalICMS = 0
    print('Produto Val.Compra ICMS Mercadoria')
    with open('estoque.csv', 'r') as arquivo:
        linhas = arquivo.readlines()
        for S in linhas:
            S.rstrip()
            L = S.split(';')
            L[0] = int(L[0])
            L[1] = int(L[1])
            L[2] = float(L[2])
            L[3] = float(L[3])/100
            compra = L[1] * L[2]
            icms = compra * L[3]
            merc = compra - icms
            valorTotalICMS += icms
            valorTotal += merc
            print(f'{L[0]}, {compra:.2f}, {icms:.2f}, {merc:.2f}')

    return f'Totais: {valorTotal + valorTotalICMS}, {valorTotal:.2f}, {valorTotalICMS:.2f}'
print(le_estoque_csv())
#7.6 O objetivo desse programa é mostrar como a codificação conflitante em arquivos texto pode causar problemas. É incorreto misturar ANSI com UTF-8, que são as codificações mais empregadas no Brasil, de modo que o programador deve estar atento a isso. No Exercício resolvido 7.6 é apresentado um menu com as quatro opções a seguir, além da opção de sair do programa (essa opção nem será usada, veja o porquê na Figura 7.6).
#Tenho é medo desse código
def GravaLe(grava, le):
    print('\n--', grava, ' para ', le, '-'*29)
    arq = open('arquivo.txt', 'w', encoding=grava)
    arq.write(S)
    arq.close()
    arq = open('arquivo.txt', 'r', encoding=le)
    L = arq.readlines()
    arq.close()
    for x in L:
        print(x)
        print('-'*50)
        # A execução do programa começa por aqui
        print('\nDemonstra os conflitos de codificação de arquivos\n\n')
        S = '''Uma boa porção de caracteres com acento
        Maiúsculas: Á É Í Ó Ú Ã Õ Â Ê Ô À Ç
        Minúsculas: á é í ó ú â ô â ê ô à ç'''
        while True:
            print('O que deseja fazer?')
            print('para gravar ANSI e ler ANSI digite 1' )
            print('para gravar UTF8 e ler UTF8 digite 2')
            print('para gravar UTF8 e ler ANSI digite 3')
            print('para gravar ANSI e ler UTF8 digite 4')
            print('para sair digite 0')
            opc = int(input(' ...opc = '))
            if opc == 0:
                break
            elif opc == 1:
                GravaLe('ANSI', 'ANSI')
            elif opc ==2:
                GravaLe('UTF-8', 'UTF-8')
            elif opc == 3:
                GravaLe('UTF-8', 'ANSI')
            elif opc ==4:
                GravaLe('ANSI', 'UTF-8')
                print('Fim do Programa')