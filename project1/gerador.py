import datetime
from random import randint

def ExibeApresentacao():
    print('\nGerador de Pedidos em Carteira')
    print('-' * 40)
    print(' Dados necessários a este programa:')
    print(' - data inicial do período')
    print(' - data final do período')
    print(' - quantidade de vendas por dia')
    print(' - arquivo PRODUTOS.TXT disponível')
    print('\n')
    print(' Este programa gera o arquivo VENDAS.TXT')
    print('-' * 40)

def ConverteData(d):
    d = d.split('/')
    data = datetime.date(int(d[2]), int(d[1]), int(d[0]))
    return data

def ObtemEntradas():
    s = input('Digite data inicial (formato: dd/mm/aaaa): ')
    ini = ConverteData(s)
    s = input('Digite data final (formato: dd/mm/aaaa): ')
    fim = ConverteData(s)
    q = int(input('Digite a quantidade de vendas por dia: '))
    
    d = input('Deseja adicionar os sábados ?: [S/n]')

    return ini, fim, q, d

def LeArqProdutos():
    dicProd = {}
    arq = open('PRODUTOS.TXT')

    for S in arq.readlines():
        S = S.rstrip()
        L = S.split(';')
        codigo = int(L[0])
        dicItem = {}
        dicItem['estq'] = int(L[1])
        dicItem['qmin'] = int(L[2])
        dicItem['pcunit'] = float(L[3])
        dicItem['margem'] = float(L[4])
        dicProd[codigo] = dicItem
    arq.close()

    print('Leitura de PRODUTOS.TXT ok. Foram lidas {} linhas'.
    format(len(dicProd)))

    return dicProd

def GeraQtdeVenda(Qtde):
    global Prods

    vendas_min = max(0, Qtde - 10)
    vendas_max = Qtde + 10
    vendas_por_dia = randint(vendas_min, vendas_max)

    return vendas_por_dia

def GeraPcUnitVenda(codprod):
    global Prods

    pccompra = Prods[codprod]['pcunit']
    margem = Prods[codprod]['margem'] / 100
    variacao = randint(0, 10) / 100
    pcvenda = pccompra * (1 + margem + variacao)

    return pcvenda

def GeraDadosDia(dia, qtvendas):
    global Prods, arq
    L = list(Prods.keys()) # carrega a lista L com os cód. prod.

    for x in range(qtvendas):
        # sorteia produto, gera um índice e o utiliza na lista
        iprod = randint(0, len(Prods)-1)
        codprod = L[iprod]
        # randomiza a quantidade vendida
        qtitem = GeraQtdeVenda(Qtde)
        # randomiza o preco de venda
        pcunit = GeraPcUnitVenda(codprod)

        a = str(dia.year)+';'+str(dia.month)+';'+str(dia.day)
        a = a + ';' + str(codprod)
        a = a + ';' + '{:d}'.format(qtitem)
        a = a + ';' + '{:.2f}'.format(pcunit)
        a = a + '\n'
        
        arq.write(a)
    
# Ponto de início da execução
ExibeApresentacao()
DtIni, DtFim, Qtde, D = ObtemEntradas()
Prods = LeArqProdutos()

arq = open('VENDAS.TXT', 'w', encoding='UTF-8')

UmDia = datetime.timedelta(days=1)
Cont = DtIni

if D == 'n':
    day = 5
else:
    day = 6

while Cont <= DtFim:
    if Cont.weekday() < day:
        GeraDadosDia(Cont, Qtde)
    Cont = Cont + UmDia

arq.close()
print('\nO arquivo de dados foi gerado com sucesso')
print('\n\nFim do Programa')