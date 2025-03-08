#**************************************************************************
#Trabalho Computacional – Introdução à Programação - 2024/2
#Grupo: 
#Dennis Francisco Guimarães de Oliveira Baracho
#**************************************************************************

import math
def distancia(x1, y1, x2, y2):
     return math.sqrt((pow((x1 - x2),2)) + pow((y1 - y2),2))

def obterCoordenadas(listaX, listaY, numPontos):
    for i in range(numPontos):
        novoX, novoY = input().split()
        listaX.append(int(novoX))
        listaY.append(int(novoY))

def caminhoMaisCurto(x, y, pontoInicial, pontosVisitados):
    menorDistancia = math.inf
    for i in (range(len(x))):
        if not pontosVisitados[i]:
            novaDistancia = distancia(x[pontoInicial], y[pontoInicial], x[i], y[i])
            if novaDistancia < menorDistancia:
                menorDistancia = novaDistancia
                pontoMaisProximo = i
    return pontoMaisProximo, menorDistancia

def definirCaminho(x, y, pontosVisitados, n):
    pontoInicial = 0
    caminho = str(f"{pontoInicial}")
    distanciaTotal = 0

    for j in range(n - 1):
        pontoMaisProximo, menorDistancia = caminhoMaisCurto(x, y, pontoInicial, pontosVisitados)
        pontosVisitados[pontoMaisProximo] = True
        pontoInicial = pontoMaisProximo
        caminho += str(f" {pontoMaisProximo}")
        distanciaTotal += menorDistancia
    
    pontoMaisProximo = 0
    distanciaTotal += distancia(x[pontoInicial], y[pontoInicial], x[pontoMaisProximo], y[pontoMaisProximo])
    caminho += str(f" {pontoMaisProximo}")
    return distanciaTotal, caminho

def obterPokemon(pokemon, hp, atk, defesa, numPokemon):
    for i in range((numPokemon)):
        novoNome = input()
        novoHP, novoATK, novoDEF = input().split()
        pokemon.append((novoNome))
        hp.append(int(novoHP))
        atk.append(int(novoATK))
        defesa.append(int(novoDEF))

def batalha(hp, atk, defesa, pokemonAtacante, pokemonDefensor):
    danoRecebidoAtacante = 0
    danoRecebidoDefensor = 0
    empate = -1

    while ((hp[pokemonAtacante] - danoRecebidoAtacante) > 0) and ((hp[pokemonDefensor] - danoRecebidoDefensor) > 0):
        danoRecebidoDefensor += max(0, atk[pokemonAtacante] - defesa[(pokemonDefensor)])
        if (hp[pokemonDefensor] - danoRecebidoDefensor) <= 0:
            return pokemonAtacante
        danoRecebidoAtacante += max(0, atk[pokemonDefensor] - defesa[(pokemonAtacante)])
        if (hp[pokemonAtacante] - danoRecebidoAtacante) <= 0:
            return pokemonDefensor
        if (danoRecebidoAtacante <= 0) and (danoRecebidoDefensor <= 0):
            return empate
    
def definirCampeao(pokemon, hp, atk, defesa, vitorias):
    for pokemonAtacante in range(len(pokemon)):
        for pokemonDefensor in range(pokemonAtacante + 1, len(pokemon)):
            vencedor = batalha(hp, atk, defesa, pokemonAtacante, pokemonDefensor)
            if vencedor == -1:
                vitorias[vencedor] += 0
            else:  
                vitorias[vencedor] += 1 

    maiorNdeVitorias = -1
    for l in range(len(pokemon)):
        if vitorias[l] > maiorNdeVitorias:
            maiorNdeVitorias = vitorias[l]
            campeao = pokemon[l]
    return campeao, maiorNdeVitorias 

def saida(caminho, distanciaTotal, campeao, maiorNdeVitorias):
    print(f"Caminho: {caminho}")
    print(f"Distancia: {round(distanciaTotal,6)}")
    print(f"Campeao: {campeao}")
    print(f"Numero de vitorias: {maiorNdeVitorias}", end='')

def main():
    x = []
    y = []

    pokemon = []
    hp = []
    atk = []
    defesa = []

    n = int(input())
    while n <= 0 or n > 400:
        n = int(input())

    obterCoordenadas(x, y, n)

    pontosVisitados = []
    distanciaTotal = 0
    for i in range(n):
        pontosVisitados.append(False)
    pontosVisitados[0] = True

    distanciaTotal, caminho = definirCaminho(x, y, pontosVisitados, n)
    
    obterPokemon(pokemon, hp, atk, defesa, (n-1))

    vitorias = []
    for k in range(len(pokemon)):
        vitorias.append(0)

    campeao, maiorNdeVitorias = definirCampeao(pokemon, hp, atk, defesa, vitorias)

    saida(caminho, distanciaTotal, campeao, maiorNdeVitorias)
main()
