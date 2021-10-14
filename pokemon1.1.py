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
  NUSP :11321350
  Turma:221
  Prof.:Renata 

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""

# ======================================================================
# FUNÇÕES OBRIGATÓRIAS
# Implemente neste bloco as funções obrigatórias do EP2.
# NÃO modifique os nomes e parâmetros dessas funções.
# ======================================================================

#Constantes Globais 

GRAVIDADE = 9.81
EPSILON = 0.01
DELTA_T = 0.01
PI = 3.14159265358979323846

#Funções fatorial e absoluto que adicionei

def fatorial(n):
    '''
    Esta função recebe n e retorna a multiplicação de n e seus
    antecessores. 
    '''
    # Escreva aqui o corpo da função
    fat = 1
    cont = 2
    while cont <= n:
        fat = fat * cont
        cont = cont + 1
    return fat
    
def absoluto(t):
    '''
    Essa função recebe t e devolve seu módulo.
    '''
    # Escreva aqui o corpo da função
    if t >= 0:
        return t
    else:
        return (-1)*t
        
def seno(theta):
    '''
    Esta função aproxima o valor da função seno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do seno do ângulo theta.
    '''
    # Escreva aqui o corpo da função
    x = (theta * PI) / 180
    sen_x = x
    n = 3
    xm = 1
    i = 1
    while absoluto(xm) >= 0.0000000001:
        xm = (-1)**i*(x**n)/fatorial(n)
        sen_x = sen_x + xm
        n = n + 2
        i = i + 1
    return sen_x
    
def cosseno(theta):
    '''
    Esta função aproxima o valor da função cosseno para o ângulo theta
    usando a série de Taylor até que o módulo do próximo termo da
    série calculada seja menor 1e-10.
    Entrada: O ângulo theta que deve ser informado em graus.
    Saída: A aproximação do cosseno do ângulo theta.
    '''
    # Escreva aqui o corpo da função
    x = (theta * PI) / 180
    cos_x = 1
    n = 2
    i = 1
    xm = 1
    while absoluto(xm) >= 0.0000000001:
        xm = (-1)**i*(x**n)/fatorial(n)
        cos_x = cos_x + xm
        n = n + 2
        i = i + 1
    return cos_x

def raizQuadrada(x):
    '''
    Esta função aproxima o valor da raiz quadrada de x, através da
    fórmula de recorrência r_0 = x e r_{n+1} = 1/2 (r_n+ x/r_n)
    enquanto o módulo da diferença entre os dois últimos valores
    calculados for maior que 1e-10.
    Entrada: O valor de x
    Saída: A aproximação da raiz quadrada de x.
    '''
    # Escreva aqui o corpo da função

    r_0 = x
    r_1 = (1/2)*(r_0 + (x/r_0))
    if x > 0:
        while absoluto(r_1 - r_0) >= 0.0000000001:
            r_0 = r_1
            r_1 = (1/2)*(r_0 + (x/r_0))
            
    return r_1

def atualizaPosicao(x, y, vx, vy, dt=DELTA_T):
    '''
    Esta função calcula as atualizações das posições de x e y usando
    as velocidades escalares respectivamente dadas por vx e vy.
    Entrada: As posições x e y dadas em metros, as velocidades vx e
    vy em metros por segundo e o intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de x e o valor atualizado de y.
    '''
    # Escreva aqui o corpo da função
    x = x + vx*dt
    y = y + (vy*dt) - (GRAVIDADE/2*dt**2)
    return x,y

def atualizaVelocidade(vx, vy, dt=DELTA_T):
    '''
    Esta função calcula e atualiza as velocidades vx e vy para o
    próximo intervalo de tempo.
    Entrada: As velocidades vx e vy em metros por segundo e o
    intervalo de tempo em segundos.
    Saída: Dois valores: o valor atualizado de vx e o valor atualizado de vy.
    '''
    # Escreva aqui o corpo da função
    vx = vx
    vy = vy - GRAVIDADE*(dt)
    return vx,vy

def distanciaPontos(x1, y1, x2, y2):
    '''
    Esta função calcula a distância entre dois pontos dados por
    (x1, y1) e (x2, y2).
    Entrada: As coordenadas de dois pontos no plano, x1, y1, x2, y2,
    em metros.
    Saída: A distância entre (x1, y1) e (x2, y2) em metros.
    '''
    # Escreva aqui o corpo da função
    dist = raizQuadrada((x2-x1)**2+(y2-y1)**2)
    return dist

def houveColisao(xpokebola, ypokebola, xpokemon, ypokemon, r):
    '''
    Esta função calcula se houve ou não colisão entre a pokebola e o
    pokemon considerando-se um raio r.
    Entrada: posição x e y da pokebola, posição x e y do pokemon
    e o raio r, todas medidas em metros.
    Saída: Retorna True caso haja colisão, e False caso contrário.
    '''
    # Escreva aqui o corpo da função
    if distanciaPontos(xpokebola, ypokebola, xpokemon, ypokemon) <= r:
        return True
    else:
        return False
    
def simula_lancamento (xpokebola, ypokebola,
                       vlancamento, angulolancamento,
                       xpokemon, ypokemon, r):
    '''
    Esta função simula o lançamento da bola até que ela atinja o
    pokemon, ou o solo a menos de EPSILON.
    Na simulação, considere as seguintes constantes:
    EPSILON é uma constante de precisão de 1.0e-2 metro.
    DELTAT é uma constante de precisão de 1.0e-2 segundo.
    Entrada: Posição inicial da pokebola (xpokebola e ypokebola)
    em metros.
    Posição do pokemon (xpokemon e ypokemon) em metros.
    Velocidade escalar em metros por segundo
    e ângulo de lançamento em graus.
    O raio r em metros.
    Saída: Três valores: Um booleano (True se o lançamento teve sucesso 
    e acertou o pokemon, ou False caso contrário) e as coordenadas finais
    x e y da pokébola.
    '''
    # Escreva aqui o corpo da função

    vy = vlancamento * seno(angulolancamento) 
    vx = vlancamento * cosseno(angulolancamento)
    xpokebola, ypokebola = atualizaPosicao(xpokebola, ypokebola, vx, vy, dt=DELTA_T)
    vx, vy = atualizaVelocidade(vx, vy, dt=DELTA_T)
    a = houveColisao(xpokebola, ypokebola, xpokemon, ypokemon, r)
    t = 0
    while a  == False and not (ypokebola <= EPSILON and t != 0):
        xpokebola, ypokebola = atualizaPosicao(xpokebola, ypokebola, vx, vy, dt=DELTA_T)
        vx, vy = atualizaVelocidade(vx, vy, dt=DELTA_T)
        t = 1
        a = houveColisao(xpokebola, ypokebola, xpokemon, ypokemon, r)
    return a, xpokebola, ypokebola

def main():
    xpokemon = float(input("Digite a coordenada x do pokemon: "))
    ypokemon = float(input("Digite a coordenada y do pokemon: "))
    r  = float(input("Digite o raio do pokemon (> 0) em metros: "))
    # Complete aqui o corpo da função
    n = 1
    while n <= 3:
        print("\n")
        print("Tentativa", n)
        xpokebola = float(input("Digite a coordenada x do treinador: "))
        ypokebola = float(input("Digite a coordenada y do treinador: "))
        vlancamento = float(input("Digite a velocidade de lancamento em m/s: "))
        angulolancamento = float(input("Digite o angulo de lancamento em graus: "))
        atingiu, xpokebola, ypokebola = simula_lancamento (xpokebola, ypokebola, vlancamento, angulolancamento, xpokemon, ypokemon, r)
        if atingiu == False:
            b = (distanciaPontos(xpokebola, ypokebola, xpokemon, ypokemon)-r)
            print("A pokebola nao atingiu o pokemon por %.4f metros."%(b))
        else:
            print("A pokebola atingiu o pokemon")
    
        n = n + 1
    
# ======================================================================
# FIM DO BLOCO DE FUNÇÕES OBRIGATÓRIAS
# ======================================================================



# ======================================================================
# CHAMADA DA FUNÇÃO MAIN
# NÃO modifique os comandos deste bloco!
# ======================================================================
if __name__ == "__main__":
    main()
# ======================================================================
# FIM DO BLOCO DE CHAMADA DA FUNÇÃO MAIN 
# ======================================================================

