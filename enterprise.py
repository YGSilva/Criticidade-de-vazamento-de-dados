from somar import *
#VALORES INSERIDOS NAS VARIAVEIS
senha = 10000
ajudaSenha = 1000
telefone = 100
nome = 10
email = 1

#CRIANDO LISTA PASSANDO AS VARIAVEIS, LOGO EM SEGUIDA FAZENDO A CHAMADA DA FUNÇÃO PASSANDO COMO PARAMENTRO A PROPRIA LISTA
#E ARMAZENANDO O RETORNO NUMA VARIAVEL
em1 = [senha, ajudaSenha]
sum1 = somar_elementos(em1)
em2 = [senha]
sum2 = somar_elementos(em2)
em3 = [senha, ajudaSenha]
sum3 = somar_elementos(em3)
em4 = [nome, telefone]
sum4 = somar_elementos(em4)
em5 = [nome, telefone, email]
sum5 = somar_elementos(em5)
em6 = [senha, ajudaSenha]
sum6 = somar_elementos(em6)
em7 = [senha]
sum7 = somar_elementos(em7)
em8 = [senha, ajudaSenha]
sum8 = somar_elementos(em8)
em9 = [nome, telefone]
sum9 = somar_elementos(em9)
em10 = [nome, telefone, email]
sum10 = somar_elementos(em10)
em11 = [senha, ajudaSenha]
sum11 = somar_elementos(em11)
em12 = [senha]
sum12 = somar_elementos(em12)
em13 = [senha, ajudaSenha]
sum13 = somar_elementos(em13)
em14 = [nome, telefone]
sum14 = somar_elementos(em14)
em15 = [nome, telefone, email]
sum15 = somar_elementos(em15)
em16 = [senha, ajudaSenha]
sum16 = somar_elementos(em16)
em17 = [senha]
sum17 = somar_elementos(em17)
em18 = [senha, ajudaSenha]
sum18 = somar_elementos(em18)
em19 = [nome, telefone]
sum19 = somar_elementos(em19)
em20 = [nome, telefone, email]
sum20 = somar_elementos(em20)

#GUARDANDO A SOMA DAS VARIAVEIS CORRESPONDENTES A CADA LISTA E ARMAZENANDO EM UMA OUTRA LISTA
points = [sum1, sum2, sum3, sum4, sum5, sum6, sum7, sum8, sum9, sum10, sum11, sum12, sum13, sum14, sum15, sum16, sum17, sum18, sum19, sum20]

#FAZENDO A ORDENAÇÃO CRESCENTE DOS VALORES DA LISTA
points.sort()
#FAZENDO O COM QUE A ORDENAÇÃO FIQUE DECRESCENTE
points.reverse()

#ATRIBUINDO A SOMA DE CADA LISTA EM UMA NOVA VARIAVEL
a = sum1
b = sum2
c = sum3
d = sum4
e = sum5
f = sum6
g = sum7
h = sum8
i = sum9
j = sum10
k = sum11
l = sum12
m = sum13
n = sum14
o = sum15
p = sum16
q = sum17
r = sum18
s = sum19
t = sum20

#CRIAÇÃO DE UMA NOVA LISTA PARA ARMAZENAR O NOMES DAS EMPRESAS
ranking = []

#LAÇO FOR PARA PERCORRER A LISTA POINTS E COLOCAR O NOME DA EMPRESA NA LISTA RANKING
for x in points:
    #VERIFICA SE X É IGUAL A 'A', AMBOS OS VALORES SÃO IGUAIS A 0, COMO B SERÁ 1, C SERÁ 3, E O X SEMPRE SERÁ INCREMENTADO QUANDO O LOOP VOLTAR
    if x == a:
      #IF VERIFICA SE A VARIAVEL JÁ ESTÁ DENTRO DA LISTA RANKING
      if a not in ranking:
        #ADICIONA O VALOR A LISTA RANKING
        ranking.append("Google")
        #VARIAVEL É SETADA COM O VALOR QUE FOI INSERIDO NA LISTA PARA ASSIM EVITAR A DUPLICIDADE DE DADOS
        a = "Google"
    elif x == b:
      if b not in ranking:
        ranking.append("Ares")
        b = "Ares"
    elif x == c:
      if c not in ranking:
        ranking.append("Mozila")
        c = "Mozila"
    elif x == d:
      if d not in ranking:
        ranking.append("Descomplica")
        d = "Descomplica"
    elif x == e:
      if e not in ranking:
        ranking.append("Ifood")
        e = "Ifood"
    elif x == f:
      if f not in ranking:
        ranking.append("Opera")
        f = "Opera"
    elif x == g:
      if g not in ranking:
        ranking.append("Xiaomi")
        g = "Xiaomi"
    elif x == h:
      if h not in ranking:
        ranking.append("MBC")
        h = "MBC"
    elif x == i:
      if i not in ranking:
        ranking.append("Uber")
        i = "Uber"
    elif x == j:
      if j not in ranking:
        ranking.append("BTG")
        j = "BTG"
    elif x == k:
      if k not in ranking:
        ranking.append("Inter")
        k = "Inter"
    elif x == l:
      if l not in ranking:
        ranking.append("NuBank")
        l = "NuBank"
    elif x == m:
      if m not in ranking:
        ranking.append("Visa")
        m = "Visa"
    elif x == n:
      if n not in ranking:
        ranking.append("Next")
        n = "Next"
    elif x == o:
      if o not in ranking:
        ranking.append("C9")
        o = "C9"
    elif x == p:
      if p not in ranking:
        ranking.append("Santander")
        p = "Santander"
    elif x == q:
      if q not in ranking:
        ranking.append("Bradesco")
        q = "Bradesco"
    elif x == r:
      if r not in ranking:
        ranking.append("Banco Pan")
        r = "Banco Pan"
    elif x == s:
      if s not in ranking:
        ranking.append("Crefisa")
        s = "Crefisa"
    elif x == t:
      if t not in ranking:
        ranking.append("Adobe")
        t = "Adobe"

print("==========================================\n\nTABELA DE PONTOS DE DADOS VAZADOS\n")
print("senha = 10000\najudaSenha = 1000\ntelefone = 100\nnome = 10\nemail = 1")
print("\n==========================================")

count = 1
i = 0
for x in ranking:
    print(f"{count}º: A EMPRESA {x} VAZOU UM TOTAL DE {points[i]} PONTOS DE SEUs USUARIOs, PARA SABER QUAIS DADOS FORAM VAZADOS CONSULTE A TABELA.")
    i += 1
    count += 1