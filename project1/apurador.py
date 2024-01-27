def ExibeApresentacao():
    print('\nApurador de Pedidos em Carteira')
    print('-' * 40)
    print(' Dados necessários a este programa:')
    print(' - arquivo PRODUTOS.TXT disponível')
    print(' - arquivo VENDAS.TXT disponível')
    print('\n')
    print(' Este programa grava o arquivo APURA.TXT')
    print('-' * 40, '\n')

def LeArqProdutos():
    arq = open('PRODUTOS.TXT') 
    dicProd = {} 


    for S in arq.readlines():
        dicItem = {}
        S = S.rstrip()
        L = S.split(';')
        codigo = int(L[0])
        dicItem['estq'] = int(L[1])
        dicItem['qmin'] = int(L[2])
        dicItem['pcunit'] = float(L[3])
        dicItem['margem'] = float(L[4])
        dicProd[codigo] = dicItem

    print('Leitura de PRODUTOS.TXT ok. Foram lidas {} \
    linhas'.format(len(dicProd)))

    arq.close()

    return dicProd

def LeArqVendas():
    arq = open('VENDAS.TXT')
    V = [] 
               
    for s in arq.readlines():
        s = s.rstrip()
        L = s.split(';')
                    
    for i in range(6):
        if i < 5:
            L[i] = int(L[i])
        else:
            L[i] = float(L[i])

    V.append(tuple(L))

    print('Leitura de VENDAS.TXT ok. Foram lidas {} \
    linhas'.format(len(V)))

    arq.close()

    return V

def ApuraDemandaEstoque():
    global Prods, Vendas, arqsai
    dicEstq = {}
    
    for codprod in Prods.keys():
        dicItem = {}

        dicItem['estq'] = Prods[codprod]['estq']
        dicItem['qmin'] = Prods[codprod]['qmin']
        dicItem['demanda'] = 0
        dicEstq[codprod] = dicItem

    for v in Vendas:
        codprod = v[3]

        dicEstq[codprod]['demanda'] += v[4]

        arqsai.write('-'*52 + ' Início de Bloco -' + '\n')
        arqsai.write('NECESSIDADE DE ESTOQUE NO PERÍODO\n')
        arqsai.write('-'*70 + '\n')
        arqsai.write(' '*9 + 'Estoque '+ ' '*14 + 'Estoque' + ' '*4 +
        'Estoque' + ' '*6 + 'Neces.\n')
        arqsai.write('Prod. Inicial Demanda' + ' '*6 +
        'Final Mínimo Compra\n')

        sgrava = '{:<5} {:>10d} {:>10d} {:>10d} {:>10d} {:>10d}\n'

    for codprod, dados in dicEstq.items():

        EstqFinal = dados['estq'] - dados['demanda']

        if EstqFinal < 0:
            EstqFinal = 0
    
        NecCompra = dados['demanda'] - dados['estq'] + dados['qmin']

        if NecCompra < 0:
            NecCompra = 0

        arqsai.write(sgrava.format(
        codprod,
        dados['estq'],
        dados['demanda'],
        EstqFinal,
        dados['qmin'],
        NecCompra))

    arqsai.write('-'*55 + ' Fim de Bloco -' + '\n\n\n')

def ApuraTotaisPorProduto():
    global Prods, Vendas, arqsai # linha 2
    dicTotais = {} # linha 3

    for codprod in Prods.keys():
        dicItem = {}
        dicItem['totval'] = 0
        dicItem['totqtd'] = 0
        dicTotais[codprod] = dicItem # linha 8
    
    for v in Vendas: # linha 9
        codprod = v[3]
        dicTotais[codprod]['totval'] += v[4] * v[5]
        dicTotais[codprod]['totqtd'] += v[4] # linha 12
        arqsai.write('-'*52 + ' Início de Bloco -' + '\n')
        arqsai.write('TOTAIS DE PEDIDOS EM CARTEIRA\n')
        arqsai.write('-'*70 + '\n') # linha 16
        arqsai.write('Prod. Valor Tot Qtde ' +
        'Pç Médio Pç Custo Margem Méd\n')
        sgrava = '{:<5} {:>11.2f} {:>8d} {:>10.2f} {:>10.2f} \{:>10.1f}%\n'
        TotVendas = 0 # linha 21

        for codprod, dados in dicTotais.items():
            try:
                TotVendas += dados['totval']
                pcmedio = dados['totval'] / dados['totqtd']
                lucrat = (pcmedio / dados['pcunit'] - 1) * 100
            except:
                pcmedio = lucrat = 0
                arqsai.write(sgrava.format(
                codprod,
                dados['totval'],
                dados['totqtd'],
                pcmedio,
                Prods[codprod]['pcunit'],
                lucrat))
    arqsai.write('-'*70 + '\n')
    arqsai.write('Total {:>11.2f}\n'.format(TotVendas))
    arqsai.write('-'*55 + ' Fim de Bloco -' + '\n\n\n')

# Ponto de início da execução
ExibeApresentacao() 
Prods = LeArqProdutos() 
Vendas = LeArqVendas() 

arqsai = open('APURA.TXT', 'w', encoding='UTF-8')
ApuraDemandaEstoque() 
ApuraTotaisPorProduto()
arqsai.close()
print('\n\nFim do programa')