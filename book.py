# Atvidades do Livro do Sérgio Luiz Banin, "Python3: Conceitos e aplicações"

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
import random
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
        
print(cria_lista_aleatoria(10))1