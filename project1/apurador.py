# Ponto de início da execução
ExibeApresentacao() 
Prods = LeArqProdutos() 
Vendas = LeArqVendas() 

arqsai = open('APURA.TXT', 'w', encoding='UTF-8') # 4
ApuraDemandaEstoque() 
ApuraTotaisPorProduto()
arqsai.close()
print('\n\nFim do programa')

def ExibeApresentacao():
    print('\nApurador de Pedidos em Carteira')
    print('-' * 40)
    print(' Dados necessários a este programa:')
    print(' - arquivo PRODUTOS.TXT disponível')
    print(' - arquivo VENDAS.TXT disponível')
    print('\n')
    print(' Este programa grava o arquivo APURA.TXT')
    print('-' * 40, '\n')