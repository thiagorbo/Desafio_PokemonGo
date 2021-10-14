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

  Nome : Natalia Marie Decroix dos Santos
  NUSP : 11321350
  Turma: MAC0115
  Prof.: Renata

  Referências: Com exceção das rotinas fornecidas no enunciado
  e em sala de aula, caso você tenha utilizado alguma refência,
  liste-as abaixo para que o seu programa não seja considerado
  plágio ou irregular.
"""
#Entradas (Quantidade de pokebolas(N), gravidade(g) e cordenadas do pokemon(xp e xy)).
N = int(input("Digite o numero N de pokebolas: "))
g = int(input("Digite o valor da gravidade: "))
xp = int(input("Digite a coordenada x (inteiro >= 0) do pokemon: "))
yp = int(input("Digite a coordenada y (inteiro >= 0) do pokemon: "))
cont = 1


#Quando N acabar, o programa para. 
#Coordenadas do treinador (xt,yt) e velocidade inicial da pokebola no eixo y(vy), pois em x será constante. 

while N > 0:    
    print(" ")
    print("Tentativa",cont)
    print(" ")
    xt = int(input("Digite a coordenada x (inteiro >= 0) do treinador: "))
    yt = int(input("Digite a coordenada y (inteiro >= 0) do treinador: "))
    vy = int(input("Digite a componente y da velocidade de lancamento: "))
    xb = xt
    yb = yt
    vyb = vy
    t = 0
    print(" ")
    
#Quando a pokebola estiver em t == 0 estará na mesma posição que o treinador.

    print("> t=%4d"%t," vy=%4d"%vyb," x=%4d"%xb," y=%4d"%yb)
    
#Laço para mostrar de segundo a segundo, as posições (xb e yb) e velocidade inicial da pokebola (vyb).
#O y da pokebola não deve ser menor que 0, e só poderá ser zero para t == 0, pois em instantes posteriores a t == 0 ele terá caido no chão. 
#E a posição x da pokebola não pode ser igual nem maior que a posição x do pokemon. 

    while not ((yb < 0 or xb >= xp) or (yb == 0 and t != 0)):
        t = t + 1
        xb = xt+t
        yb = yt+vy*t-g/2*t**2
        vyb = vy - g*(t)
    
        print("> t=%4d"%t," vy=%4d"%vyb," x=%4d"%xb," y=%4d"%yb)
        
#Se as coordenadas x e y da pokebola e do pokemon forem iguais a pokebola atinge o pokemon, caso contrário não atinge. 

    if xb == xp and yp == yb:
        print ("A pokebola atingiu o pokemon")
    else: 
        print("A pokebola nao atingiu o pokemon")
        
    
    N = N - 1
    cont = cont + 1

    