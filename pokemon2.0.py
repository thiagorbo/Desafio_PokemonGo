"""
  AO PREENCHER ESSE CABEÇALHO COM O MEU NOME E O MEU NÚMERO USP, 
  DECLARO QUE SOU O ÚNICO AUTOR E RESPONSÁVEL POR ESSE PROGRAMA. 
  TODAS AS PARTES ORIGINAIS DESSE EXERCÍCIO PROGRAMA (EP) FORAM 
  DESENVOLVIDAS E IMPLEMENTADAS POR MIM SEGUINDO AS INSTRUÇÕES
  DESSE EP E QUE PORTANTO NÃO CONSTITUEM DESONESTIDADE ACADÊMICA
  OU PLÁGIO.  
  DECLARO TAMBÉM QUE SOU RESPONSÁVEL POR TODAS AS CÓPIAS
  DESSE PROGRAMA E QUE EU NÃO DISTRIBUI OU FACILITEI A
  SUA DISTRIBUIÇÃO. ESTOU CIENTE QUE OS CASOS DE PLÁGIO E
  DESONESTIDADE ACADÊMICA SERÃO TRATADOS SEGUNDO OS CRITÉRIOS
  DIVULGADOS NA PÁGINA DA DISCIPLINA.
  ENTENDO QUE EPS SEM ASSINATURA NÃO SERÃO CORRIGIDOS E,
  AINDA ASSIM, PODERÃO SER PUNIDOS POR DESONESTIDADE ACADÊMICA.

  Nome :Natalia Marie Decroix dos Santos 
  NUSP : 11321350
  Turma: 221
  Prof.: Renata

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""

import math

DELTA_T = 0.1
GRAVIDADE = 2

# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente neste bloco as funções obrigatórias do EP3.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================

def leArquivo(nomeArquivo = 'entrada.txt'):
    '''
    Esta função lê um arquivo ('entrada.txt' por default) e
    retorna uma lista de listas.
    Entrada: arquivo cujo nome está armazenado em nomeArquivo.
             Por default, é 'entrada.txt'
    Saída: uma lista de listas, onde o primeiro elemento é uma
           lista de inteiros [m, n] (dimensões da matriz) e os
           elementos subsequentes são listas que representam as
           característica lidas dos Pokémons na forma:
                [nome, raio, x, y]
    '''
    A = []
    B = []
    
    Arquivo = open(nomeArquivo)
    for line in (Arquivo):
        A = line.split()
        B.append(A)
        
    Arquivo.close()
    
    return B
    


def criaMatriz(m, n):
    '''
    Esta função cria e retorna uma lista de listas.
    Entrada: dois inteiros que representam o número de linhas e
             o número de colunas da matriz.
    Saída: uma lista de m listas, cada uma com n elementos, todos
           inicializados com zeros.
    '''
    Matriz = []
    for i in range(m):
        linha = []
        for j in range(n):
            linha.append(0)
        Matriz.append(linha)
    return Matriz


def populaMatriz(matriz, pokemons):
    '''
    Esta função recebe uma matriz e uma lista contendo listas que
    representam os pokémons na forma [nome, raio, x, y] e preenche-a
    os pokémons conforme a representação retangular considerando os
    raios da representação.
    Entrada: matriz representada por uma lista de listas
    Saída: A matriz fornecida é modificada.
    '''
    for i in range(len(pokemons)):
        raio = int(pokemons[i][1])
        x = int(pokemons[i][2])
        y = int(pokemons[i][3])
        id = i + 1
        matriz = preenchePokemon(matriz, id, x, y, raio)
    return matriz
            
    

def preenchePokemon(matriz, id, x, y, raio):
    '''
    Esta função é auxiliar da função populaMatriz. Ela insere
    um Pokémon na matriz de acordo com sua representação retangular
    baseada no raio ao redor do ponto central (x,y)
    Entrada: matriz representada por uma lista de listas
             id é o número a preencher a matriz; para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente.
             x,y são as coordenadas do ponto central
             raio é a distância a ser guardada a partir do
             ponto central.
    Saída: A matriz fornecida é modificada.
    '''
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if x-raio<= j <= x+raio and y-raio <= i <= y + raio:
                matriz[i][j]=id
    return matriz
          

def removePokemon(matriz, id, pokemons):
    '''
    Esta função recebe uma matriz, o numeral que representa o pokémon
    a ser removido da matriz (id) e a lista contendo as listas que
    representam pokémons, substituindo os numerais id por zero
    Entrada: matriz representada por uma lista de listas;
             id é o número a preencher a matriz, para o
             primeiro pokémon na lista (de índice zero),
             usa-se 1 e assim subsequentemente;
             pokemons lista contendo as listas que representam pokémons.
    Saída: A matriz fornecida é modificada.
    '''
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == id:
                matriz[i][j] = 0
    return matriz


def imprimeMatriz(matriz):
    '''
    Esta função imprime a matriz dada.
    Note que a matriz deve ser impressa com espelhamento vertical, 
    pois a primeira linha representa o chão.
    Entrada: matriz representada por uma lista de listas.
    '''
    
    for linha in matriz:
        for x in linha:
            if x == 0:
                x = '.'
            print("%2s"%x, end = "")
        print()


def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''
    x = x + vx*dt
    y = y + (vy*dt) - (GRAVIDADE/2*dt**2)
    return (x,y)


def atualizaVelocidade(vx, vy, dt=DELTA_T):
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''
    vx = vx
    vy = vy - GRAVIDADE*(dt)
    return (vx,vy)
    

def grau2Radiano(theta):
    '''
    Esta função converte o ângulo theta em graus para radianos.
    Entrada: ângulo theta.
    Saída: ângulo theta em radianos.
    '''
    x = (theta * PI) / 180
    return x



def main():
    nome = input("Digite o nome do arquivo: ")
    pokemons = leArquivo(nome)
    N = int(input("Digite o numero N de pokebolas: "))
    xt= int(input("Digite a coordenada x do treinador: "))
    
    m = int(pokemons[0][0])
    n = int(pokemons[0][1])
    pokemons = pokemons[1:]
    pegouTodos = False
    matriz = criaMatriz(m, n)
    matriz = populaMatriz(matriz, pokemons)
    resultado = imprimeMatriz(matriz)
    
    while N > 0 and pegouTodos == False:
        print ("pokebolas disponiveis =", N)
        print("Estado atual do jogo: ")
        print(resultado)
    
        v = float(input("Digite a velocidade de lancamento em m/s: "))
        tetha = float(input("Digite o angulo de lancamento em graus: ")) 
        while y<0 and x <0 or x > n-1:
            xpokebola, ypokebola = atualizaPosicao(xpokebola, ypokebola, vx, vy, dt=DELTA_T)
            vx, vy = atualizaVelocidade(vx, vy, dt=DELTA_T)
            matriz = populaMatriz(matriz, pokemons)
            resultado = imprimeMatriz(matriz)
            
        N = N - 1    
        print("Representacao grafica do lancamento: ", resultado)
    #atualizavelocidade
    #atualizapokemon
    #imprimematriz
    #simetria pois no EP conta de baixo para cima e não de cima para baixo

 
 #listapokemons = learquivo()
 #learquivo sai 15,40 como string preciso transformar string em inteiro. 
    ''' 
    if 
        print("O lancamento nao capturou pokemon algum")
        print("\n")
        print("Jogo encerrado")
    elif:
        print("Um", pokemon[id][0], "foi capturado!")
        print("\n")
        print("Parabens! Todos pokemons foram capturados")
    '''

main()