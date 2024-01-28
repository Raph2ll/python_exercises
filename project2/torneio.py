from datetime import date
import os
import sqlite3
LargTela = 70

def ExibeClassificacao():
    global Times, Torneio

    MontaClassificacao()
    sfmt = '{:>3} {:<16}' + '{:>6}'*8
    print('-' * LargTela)
    s = 'Pos;Time;PG;J;V;E;D;GP;GC;SG'
    print(sfmt.format(*s.split(';')))
    print('-' * LargTela)
    Pos = 1

    for time in Times:
        dados = (Pos,) + tuple(time)
        print(sfmt.format(*dados))
        Pos += 1
        print('-' * LargTela)

def GravaHTML():
    global Times, Torneio
    hoje = date.today()
    hoje = '{}/{}/{}'.format(hoje.day, hoje.month, hoje.year)

    MontaClassificacao()
    sfmt = '<tr><td>{}</td><td style=’text-align:left’>{}</td>' + \
    '<td>{}</td>'*8 + '</tr>'
    Pos = 1
    tabela = ''

    for time in Times:
        dados = (Pos,) + tuple(time)
        tabela = tabela + sfmt.format(*dados)
        Pos += 1
        arq = open('gabarito.html', 'r', encoding='UTF-8')
        html = arq.read()
        arq.close;
        html = html.replace('<...NomeTorneio...>', Torneio)
        html = html.replace('<...Hoje...>', hoje)
        html = html.replace('<...Tabela...>', tabela)
        arq = open(Torneio+'.html', 'w', encoding='UTF-8')
        arq.write(html)
    arq.close()

def ExcluiTorneio(Torneio):
    print('\n'*3)
    ExibeLinha('Confirma Exclusão do Torneio ' + Torneio, 40)
    print('Opções: ')
    print(' (C) para Confirmar')
    print(' qualquer outra tecla para retornar')
    opc = input('sua opção? >>> ')
    opc = opc.upper()

    if opc == 'C':
        conector = sqlite3.connect('torneios.db')
        cursor = conector.cursor()
        sql = 'delete from torneios where nometorneio = ‘' + \
        Torneio + '’'
        print(Torneio)
        print(sql)
        Pausa('-' * 58)

        cursor.execute(sql)
        conector.commit()
        cursor.close()
        conector.close()
        os.remove(Torneio + '.db')

        return True
    else:
        return False

def LimpaJogo(numjogo):
    global Torneio
    conector = sqlite3.connect(Torneio + '.db')
    cursor = conector.cursor()
    sql = '''
    update jogos set gol1 = NULL, gol2 = NULL
    where numjogo = ?
    '''
    cursor.execute(sql, (numjogo,))
    conector.commit()
    cursor.close()
    conector.close()

def AtualizaJogo(numjogo, gol1, gol2):
    global Torneio
    conector = sqlite3.connect(Torneio + '.db')
    cursor = conector.cursor()

    sql = '''
    update jogos set gol1 = ?, gol2 = ?
    where numjogo = ?
    '''

    cursor.execute(sql, (gol1, gol2, numjogo))
    conector.commit()
    cursor.close()
    conector.close()

def TrataEntrRodada(opc, JogosRodada):
    opc = opc.replace(' ', '') # remove espaços em branco
    L = opc.split(',')
    if len(L) != 2 and len(L) != 3:
        return 'Entrada Invalida'
    
    if len(L) == 2:
        if L[0].isnumeric() and L[1] == 'LIMPA':
            jogo = int(L[0])
        
        if jogo in JogosRodada:
            LimpaJogo(jogo)
            return None
        else:
            return 'Jogo de outra rodada'
    else:
        return 'Entrada Invalida'
    if len(L) == 3:
        try:
            jogo = int(L[0])
            gols1 = int(L[1])
            gols2 = int(L[2])
            if jogo in JogosRodada:
                AtualizaJogo(jogo, gols1, gols2)
            else:
                return 'Jogo de outra rodada'
        except:
            return 'Entrada Inválida'
        finally:
            return None

def ObtemJogosRodada(NRod):
    global Torneio
    conector = sqlite3.connect(Torneio + '.db')
    cursor = conector.cursor()

    sql = 'select * from jogos where numrod = ? order by numjogo'
    cursor.execute(sql, (NRod,))

    J = cursor.fetchall()
    cursor.close()
    conector.close()
    return J

def ExibeJogos(Jogos):
    ExibeLinha('*** Rodada {} ***'.format(Jogos[0][1]), 64)
    s = '{:<6}{:<16}{:<5}x{:>5}{:>16}'
    JRod = []

    for J in Jogos:
        JRod.append(J[0])
        if J[3] == J[5] == None:
            ExibeLinha(s.format(J[0], J[2], ' ', ' ', J[4]), 64)
        else:
            ExibeLinha(s.format(J[0], J[2], J[3], J[5], J[4]), 64)
            print('-' * LargTela)

    return JRod

def GerenciaRodada(NRod):
    global Times, Torneio, Turnos
    Jogos = ObtemJogosRodada(NRod)

    while True:
        TopoTela('Gerenciamento de Torneio')
        ExibeTimes()

        JogosRodada = ExibeJogos(Jogos)
        print('Opções: ')
        print(' (.) Para atualizar o placar de um jogo digite:')
        print(' NºJogo,GolsA,GolsB exemplo: 12,2,1')
        print(' (.) Para limpar o placar de um jogo digite:')
        print(' NºJogo,limpa exemplo: 12,limpa')
        print(' (S) Voltar ao Menu do Torneio')
        opc = input('sua opção? >>> ')
        opc = opc.upper()

        if opc == 'S':
            break
        else:
            msg = TrataEntrRodada(opc, JogosRodada)
        if msg != None:
            Pausa(msg + ' (pressione Enter)')
        else:
            Jogos = ObtemJogosRodada(NRod)

def ConfrontoDireto(a, b):
    global Torneio
    d = {'timeA':a[0], 'timeB':b[0]}
    ptoA = ptoB = 0
    conector = sqlite3.connect(Torneio + '.db')
    cursor = conector.cursor()

    sql = '''
    select * from jogos where gol1 is not null and
    time1 = :timeA and time2 = :timeB
    '''

    cursor.execute(sql, d)
    J = cursor.fetchone()

    if J:
        if J[3] == J[5]:
            ptoA += 1
            ptoB += 1
    elif J[3] > J[5]:
        ptoA += 3
    elif J[5] < J[3]:
        ptoB += 3

    sql = '''
    select * from jogos where gol1 is not null and
    time1 = :timeB and time2 = :timeA
    '''

    cursor.execute(sql, d)

    J = cursor.fetchone()
    if J:
        if J[3] == J[5]:
            ptoA += 1
            ptoB += 1
    elif J[3] > J[5]:
        ptoB += 3
    elif J[5] < J[3]:
        ptoA += 3

    cursor.close()
    conector.close()

    if ptoA > ptoB:
        return -1
    elif ptoA < ptoB:
        return 1
    else:
        return 0

def OrdenaTimes():
# usa BubbleSort para ordenar os times
    global Times
    Trocou = True

    while Trocou:
        Trocou = False
        i = 0

    while i < len(Times)-1:
        if Compara(Times[i], Times[i+1]) < 0:
            Times[i], Times[i+1] = Times[i+1], Times[i]
            Trocou = True
        i += 1
        
def Compara(a, b):
    # 1º Crit. Pontos
    if a[1] < b[1]:
        return -1
    elif a[1] > b[1]:
        return 1
    # 2º Crit. Vitórias
    if a[3] < b[3]:
        return -1
    elif a[3] > b[3]:
        return 1
    # 3º Crit. Saldo Gols
    if a[8] < b[8]:
        return -1
    elif a[8] > b[8]:
        return 1
    # 4º Crit. Gols Pró
    if a[6] < b[6]:
        return -1
    elif a[6] > b[6]:
        return 1
    return ConfrontoDireto(a, b)

def MontaClassificacao():
    global Times, Torneio
    # Primeira parte – Computa os resultados
    ZeraDadosTimes()
    Jogos = LeJogos()

    for jogo in Jogos:
        if jogo[3] == jogo[5]:
            ComputaResultado(jogo[2], 'E', jogo[3], jogo[5])
            ComputaResultado(jogo[4], 'E', jogo[5], jogo[3])
        elif jogo[3] < jogo[5]:
            ComputaResultado(jogo[2], 'D', jogo[3], jogo[5])
            ComputaResultado(jogo[4], 'V', jogo[5], jogo[3])
        elif jogo[3] > jogo[5]:
            ComputaResultado(jogo[2], 'V', jogo[3], jogo[5])
            ComputaResultado(jogo[4], 'D', jogo[5], jogo[3])
        # Segunda parte – Ordena a tabela de classificação
        OrdenaTimes()

def ZeraDadosTimes():
    global Times
    for time in Times:
        for i in range(1, 9):
            time[i] = 0

def LeJogos():
    global Torneio
    conector = sqlite3.connect(Torneio + '.db')
    cursor = conector.cursor()

    sql = '''
    select * from jogos
    where gol1 is not null order by numjogo
    '''

    cursor.execute(sql)
    J = cursor.fetchall()
    cursor.close()
    conector.close()

    return J

def ComputaResultado(QualTime, Res, GP, GC):
    global Times

    for time in Times:
        if time[0] == QualTime:
            time[2] += 1 # qtde jogos
            time[6] += GP # gols pro
            time[7] += GC # gols contra
            time[8] += GP-GC # saldo gols
        if Res == 'V':
            time[1] += 3 # ptos ganhos
            time[3] += 1 # qtde vitorias
        elif Res == 'E':
            time[1] += 1 # ptos ganhos
            time[4] += 1 # qtde empates
        elif Res == 'D':
            time[5] += 1 # qtde derrotas
        
def CalcPramsTorneio():
    global Times, Turnos
    Qtde = len(Times)

    if Qtde % 2 == 0:
        NRod = (Qtde - 1) * Turnos
    else:
        NRod = Qtde * Turnos
        NJog = (Qtde - 1) * Qtde // 2 * Turnos
    return Qtde, NRod, NJog

def ExibeTimes():
    global Times
    Qtde, NRod, NJog = CalcPramsTorneio()
    ExibeLinha('Times deste Torneio ' + Torneio, 64)
    cont = 1
    s = ''

    for t in Times:
        s = s + '{:<15}'.format(t[0])
    if cont % 4 == 0:
        ExibeLinha(s, 64)
        s = ''
        cont += 1
    if s != '':
        ExibeLinha(s, 64)
        ExibeLinha('', 64)
        s = 'Nº de Rodadas: {} - Nº de Jogos: {}'
        ExibeLinha(s.format(NRod, NJog), 64)
        print('-' * LargTela)

def CarregaTimes():
    global Torneio
    T = []
    conector = sqlite3.connect(Torneio + '.db')
    cursor = conector.cursor()

    sql = 'select nometime from times order by nometime'

    cursor.execute(sql)

    for time in cursor.fetchall():
        t = [time[0]] + [0]*8
        T.append(t)
        cursor.close()
        conector.close()
    return T

def GerenciaTorneio(t):
    global Times, Torneio, Turnos
    Torneio = t['nome']
    Turnos = t['turnos']
    Times = CarregaTimes()
    Qtde, NRod, NJog = CalcPramsTorneio()
    while True:
        TopoTela('Gerenciamento de Torneio')
        ExibeTimes()
        ExibeClassificacao()
        print('Opções: ')
        print(' (.) Para ver uma rodada digite seu número.')
        print(' Rodadas Válidas de 1 a {}'.format(NRod))
        print(' (G) Grava o Torneio em HTML')
        print(' (E) Exclui o Torneio')
        print(' (S) Voltar ao Menu Principal')
        opc = input('sua opção? >>> ')
        opc = opc.upper()

        if opc == 'N':
            NovoTorneio()
        elif opc.isnumeric():
            n = int(opc)

        if 1 <= n <= NRod:
            GerenciaRodada(n)
        elif opc == 'G':
            GravaHTML()
        elif opc == 'E':
        
            if ExcluiTorneio(Torneio):
                break
            elif opc == 'S':
                break
        del(Times, Torneio, Turnos)

def GeraGravaJogos(NomeTorneio, QtdeTurnos, ListaTimes):
    # Gera os Jogos
    Jogos = {}
    NJogo = 1
    Qtde = len(ListaTimes)

    if Qtde % 2 == 1:
        ListaTimes.append('FOLGA')
        Qtde += 1

    # Implementa o algoritmo Round-Robin Tournament
        for r in range(Qtde-1):
            for i in range(Qtde//2):
                if ListaTimes[i] == 'FOLGA' or \
                    ListaTimes[Qtde-1-i] == 'FOLGA':
                    continue
    umJogo = {}
    umJogo['rodada'] = r+1
    umJogo['time1'] = ListaTimes[i]
    umJogo['time2'] = ListaTimes[Qtde-1-i]
    Jogos[NJogo] = umJogo
    NJogo += 1
    aux = ListaTimes[1]

    del(ListaTimes[1])
    ListaTimes.append(aux)

    # Insere no banco de dados os jogos gerados
    conector = sqlite3.connect(NomeTorneio + '.db')
    cursor = conector.cursor()
    sql = '''
    insert into jogos (numjogo, numrod, time1, time2)
    values (?, ?, ?, ?)
    '''

    for NJogo, Jogo in Jogos.items():
        cursor.execute(sql, (NJogo, Jogo['rodada'], Jogo['time1'],Jogo['time2']))
                                                         
    if QtdeTurnos == 2:
        for NJogo, Jogo in Jogos.items():
            cursor.execute(sql, (NJogo+(Qtde-1)*Qtde/2,
            Jogo['rodada']+Qtde-1,
            Jogo['time2'], Jogo['time1']))
         
    conector.commit()
    cursor.close()
    conector.close()

def GravaNomeTorneio(NomeTorneio, QtdeTurnos):
    # Insere o nome do torneio no BD de torneios
    conector = sqlite3.connect('torneios.db')
    cursor = conector.cursor()

    sql = 'insert into torneios (nometorneio, turnos) values (?, ?)'
                                                              
    cursor.execute(sql, (NomeTorneio, QtdeTurnos))
    conector.commit()
    cursor.close()
    conector.close()

def CriaBDTorneio(NomeTorneio, ListaTimes):
    # Cria o BD do torneio
    conector = sqlite3.connect(NomeTorneio + '.db')
    cursor = conector.cursor()
    sql = 'create table times (nometime text)'
    cursor.execute(sql)

    # Insere os times na tabela
    sql = 'insert into times (nometime) values (?)'
    for nome in ListaTimes:
        cursor.execute(sql, (nome,))
        conector.commit()

        # Cria a tabela de Jogos
        sql = '''
        create table jogos (
        numjogo int NOT NULL PRIMARY KEY ASC,
        numrod int,
        time1 text, gol1 int,
        time2 text, gol2 int)'''

        cursor.execute(sql)
    cursor.close()
    conector.close()

# Cria a tabela times
def ObtemNomesTimes():
    L = []
    Cont = 1

    while True:
        s = input('Time {:d}: '.format(Cont))
        if s.upper() == 'SAIR': return None
        if s.upper() == 'FIM': break
        L.append(s)
        Cont += 1
  
    return L 

def ValidaTorneio(NomeTorneio):
    if NomeTorneio == '':
        return False
    elif ExisteTorneio(NomeTorneio):
        Pausa(NomeTorneio + ' já existe (pressione Enter)')
        return False
    else:
        return True

def ObtemQtdeTurnos():
    while True:
        print('Digite a quantidade de turnos (1 ou 2): ')
        print('Digite 0 para cancelar.')
        Qtde = input('quantos turnos? >>> ')

        try:
            Qtde = int(Qtde)
        except:
            print('Entrada inválida {}'.format(Qtde))
            print('Digite qtde 1 ou 2. Digite 0 para desistir.')
        else:
            if 0 <= Qtde <= 2:
                return Qtde

def CriaNovoTorneio():
    NomeTorneio = input('\nNome do Novo Torneio: ')

    if not ValidaTorneio(NomeTorneio):
        return None
    
    QtdeTurnos = ObtemQtdeTurnos()

    if QtdeTurnos == 0:
        return None

    TopoTela('Criação de Novo Torneio')

    ExibeLinha('Novo Torneio: ' + NomeTorneio, 64)
    ExibeLinha('(a qualquer momento digite "sair" para desistir)', 64)

    print('-' * LargTela)

    ExibeLinha('Digite os nomes dos times participantes', 70)
    ExibeLinha('Digite "fim" para concluir e salvar os nomes dos times', 70)

    ListaTimes = ObtemNomesTimes()

    if ListaTimes:
        CriaBDTorneio(NomeTorneio, ListaTimes)
        GravaNomeTorneio(NomeTorneio, QtdeTurnos)
        GeraGravaJogos(NomeTorneio, QtdeTurnos, ListaTimes)
         
def ExibeLinha(msg, tam = 0, alinha = '^'):
    borda = (LargTela - tam - 2) // 2
    sfmt = '{:' + alinha + str(tam) + '}'
    print('-'*borda, sfmt.format(msg), '-'*borda)

def Pausa(msg, tam=64):
    if msg != '':
        ExibeLinha(msg, tam)
    input()

def TopoTela(msg = ''):
    print('\n'*2, '-' * LargTela, sep = '')
    ExibeLinha('Programa Torneio', 40, '^')

    if msg != '':
        ExibeLinha(msg, 40, '^')
    print('-' * LargTela)

def PreparaAmbiente():
    ''' Se o B.D. torneios.db existe, então, lê os torneios.
    Caso contrário, cria o B.D. Necessário no primeiro
    uso do programa,'''
    conector = sqlite3.connect('torneios.db')
    cursor = conector.cursor()

    sql = '''
    select name from sqlite_master
    where type='table' and name = 'torneios'
    '''

    cursor.execute(sql)

    R = {}
    N = 1

    if cursor.fetchone() == None:
        sql = 'create table torneios (nometorneio text, turnos int)'
        cursor.execute(sql)
    else:
        sql = 'select * from torneios'
        cursor.execute(sql)

    for x in sorted(cursor.fetchall()):
        item = {}
        item['nome'] = x[0]
        item['turnos'] = x[1]
        R[N] = item
        N+=1

    cursor.close()
    conector.close()

    return R

def MenuPrincipal():
    while True:
        Torneios = PreparaAmbiente()
        TopoTela('Menu Principal')
        print('Opções: ')
        print(' (N) Criar Novo Torneio')
        print(' (.) Gerenciar Torneio Existente')
              
        if len(Torneios) == 0:
            print(' { não há torneios cadastrados }')
        else:
            
            for i, t in Torneios.items():
                print(' ({}) {}'.format(i, t['nome']))
                print(' (S) Sair do programa')
                print('\npara escolher digite o que está entre parênteses')

                opc = input('sua opção? >>> ')
                opc = opc.upper()

                if opc == 'N':
                    CriaNovoTorneio()
                elif opc.isnumeric():
                    n = int(opc)
                if n in Torneios:
                    GerenciaTorneio(Torneios[n])
                elif opc == 'S':
                    break

# Ponto de início da execução
MenuPrincipal()
print('\n'*2)
ExibeLinha('Programa Torneio encerrado', 30)
print('\n')
Pausa('Pressione Enter para sair.', 30)