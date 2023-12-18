#1. Crie um programa que receba um número e diga se ele é par ou ímpar
def verifica_impaopa(numero: int):
    if numero % 2 == 0:
        return(f'{numero} é par')
    else:
        return(f'{numero} é impar')

print(verifica_impaopa(2))
#2. Crie um programa que printa números ímpares de 0 a 100
def impares_ate(numero: int):
    impares = []
    for index in range(numero):
        if index % 2 != 0:
            impares.append(index)
    return impares
print(f'{impares_ate(100)}')
#3. Crie um programa que printa números primos de 0 a 1000
def primos_ate(numero: int):
    index = 0
    index2 = 2
    primos = []
    while index < numero:
        index += 1
        index2 = 2
        while index2 <= index:
            ret = int(index % index2)
            if ret == 0 and index != index2:
                #print(f'{index} não é primo')
                index2= index
            elif index == index2:
                #print(f'{index} é primo')
                primos.append(index)
                index2 = index
            index2 += 1
    return primos
primos_ate(100)
#4. Crie um programa que calcule a soma de números de 1 a 10
def soma_ate(numero:int):
    ret = 0
    index = 0
    while index <= numero:
        ret += index
        index += 1
    return ret
print(f'{soma_ate(10)}')
#5. Crie um programa que calcule o fatorial de 10
def fatorial_ate(numero:int):
    index = 1
    ret = 1
    while  index <= numero:
        ret = index * ret
        index += 1
    return(ret)
print(f'{fatorial_ate(10)}')
#6. Crie um programa que receba 4 notas e calcule a média
def media(A:int,B:int,C:int,D:int):
    return (A + B + C + D)/ 4
print(f'{media(10,2,1,50)}')
#7. Crie um programa que receba o tempo e a distância e calcule a velocidade
def calcula_velocidade(T:int,D:int):
    V = D / T
    return V
print(f'{calcula_velocidade(2,5)}')
#8. Crie um programa que recebe a idade de uma pessoa e diga se ele é:
#  1. Criança (0-13) 
#  2. Adolescente (14-24)
#  3. Adulto (25-55)
#  4. Idoso (+55)
def calcula_idade(idade:int):
    if idade > 0 and idade <= 13:
        return(f'Criança de {idade} anos')
    elif idade >= 14:
        return(f'Adolescente de {idade} anos')
    elif idade >= 25:
        return(f'Adulto de {idade} anos')
    elif idade >= 56:
        return(f'Idoso de {idade} anos')
    else:
        return'Digite uma idade correta'
print(f'{calcula_idade(40)}')
#9. Crie um programa que receba um número digitado e responda Verdadeiro ou Falso se ele é primo
def primo(numero:int):
    N = 12
    index = 2
    while index <= numero:
        index += 1
        ret = N % index
        if ret == 0 and index == N:
            return True
        elif ret == 0:
            return False
            index = N
print(f'{primo(12)}')
#10. Crie um programa que receba um número de horas e retorne a mesma quantidade em segundos
def transforma_minutos(N:int):
    return(f'{N} Horas são {N * 60} minutos')
print(f'{transforma_minutos(12)}')
#11. Calcule a soma de números ímpares maiores que 10 e menores que 30
def min_max(min:int,max:int):
    while min <= max:
        ret = min % 2
        if ret != 0:
            print(min)
            sum += min
        min += 1
    return sum
print(f'{min_max(10, 30)}')
#12. Calcule a soma dos dígitos de um número recebido
def soma_digitos(numero:int):
    N = 1023
    for index in str(numero):
        ret += int(index)
    return ret
print(f'{soma_digitos(1023)}')
#13. Crie um programa que recebe um texto e retorna o mesmo invertido
def soma_digitos(texto:int):
    index = len(texto)
    ret = ''
    while index >= 1:
        index -= 1
        ret += texto[index]
    return ret
soma = soma_digitos('abacaxi')
print(f'{soma}')
#14. Crie um programa que receba dois números e diga qual é o maior
def receba(A:int,B:int):
    if A > B:
        return('A é maior')
    elif A == B:
        return('Eles são iguais')
    elif B < A: 
        return ('B é menor')
    else: 
        return ('Tem algo errado ae')
print(f'{receba(20,30)}')
#15. Crie um programa que receba três números e diga qual é o maior
# acho que viajei aq
def qual_maior(A:int,B:int,C:int,D:int):
    if A > B and A > C:
        return('A é maior')
    elif B > A and B > C:
        return('B é maior')
    elif C > A and C > B:
        return('C é maior')
    elif A == B == C:
        return('Eles são iguais')
    elif A == B:
        return('A e B são iguais')
    elif A == C:
        return('A e C são iguais')
    elif C == B:
        return('C e B são iguais')
    else: 
        return('Tem algo errado ae')
print(f'{qual_maior(2,2,5)}')    
#16. Desenvolva um programa para verificar se um número é divisível entre 5 e 11.
def devolva(numero:int):
    if (numero % 5 == 0 and numero % 11 == 0):
        return('É ele')
    else:
        return('Não é ele')
print(f'{devolva(55)}')
#17. FizzBuzz
#  1. Neste problema, você deverá exibir uma lista de 1 a 100, um em cada linha, com as seguintes exceções:
#     1. Números divisíveis por 3 deve aparecer como 'Fizz' ao invés do número;
#     2. Números divisíveis por 5 devem aparecer como 'Buzz' ao invés do número;
#     3. Números divisíveis por 3 e 5 devem aparecer como 'FizzBuzz' ao invés do número'.
def fizz_buzz(numero:int):
    for i in range(numero + 1):
        if(i % 3 == 0 and i % 5 == 0):
            return(f'{i} FizzBuzz')
        elif(i % 3 == 0):
            return(f'{i} Fizz')
        elif(i % 5 == 0):
            return(f'{i} Buzz')
print(f'{fizz_buzz(100)}')
#18. Receba um número inteiro e execute as seguintes ações condicionais:
#  1. Se for ímpar, imprima Sol
#  2. Se for par e estiver no intervalo inclusivo de 2 até 5 , imprima Lua
#  3. Se for par e estiver no intervalo inclusivo de 6 até 20 , imprima Sol
#  4. Se for par e maior que 20 , imprima Lua
def receba_inteiro(N:int):
    if N % 2 == 0 and 2 <= N <= 5:
        return('Lua')
    elif N % 2 == 0 and  6 <= N <= 20:
        return('Sol')
    elif N % 2 == 0 and N > 20:
        return('Lua')
    elif N % 2 != 0:
        return('Sol')
print(f'{receba_inteiro(7)}')
#19. Elabore um programa para receber o salário base de um funcionário e calcular o salário bruto de acordo com os seguintes critérios:
#  1. Salário Base <= 10.000 : IR = 20%, INSS = 80%
#  2. Salário Base <= 20.000 : IR = 25%, INSS = 90%
#  3. Salário Base > 20.000 : IR = 30%, INSS = 95%
def receba_lulas(S:float):
    S = 17.890
    if S <= 10.000:
        return('IR = 20%, INSS = 80%')
    elif S <= 20.000:
        return('IR = 25%, INSS = 90%')
    elif S > 20.000:
        return('IR = 30%, INSS = 95%')
print(f'{receba_lulas(17.890)}')