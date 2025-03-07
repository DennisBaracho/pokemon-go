#**************************************************************************
#Trabalho Computacional – Introdução à Programação - 2024/2
#Grupo: 
#<nome completo do Componente 1>
#<nome completo do Componente 2>

#Os dados de entrada do programa serão o número de pontos (n) seguido de n coordenadas
#x,y separados por espaço. Cada coordenada representa uma cidade, sendo a cidade 0 o seu ponto
#de partida portanto, você não irá capturar um Pokémon na cidade 0. Na sequência haverá o nome do
#Pokémon de cada cidade, na linha seguinte, sua vida (HP), pontos de ataque (ATK) e pontos de
#defesa (DEF), separados por espaço. Assuma que você trabalhará com no máximo 400 pontos de
#cidades e 399 Pokémons como entrada. Esses valores serão lidos pelo seu programa usando o
#redirecionamento de entrada (<). Veja abaixo como funciona o redirecionamento de entrada:
#**************************************************************************

import math
def distancia(x1, y1, x2, y2):
     return math.sqrt((pow((x1 - x2),2)) + pow((y1 - y2),2))

def obterCoordenadas(listaX, listaY, numPontos):
    for i in range(numPontos):
        novoX, novoY = input(f"\nDigite as coordenadas X e Y da cidade {i} na mesma linha: ").split()
        listaX.append(int(novoX))
        listaY.append(int(novoY))

def caminhoMaisCurto(a, b, pontoInicial, pontosVisitados):
    menorDistancia = float('inf')
    for i in (range(len(a))):
        if not pontosVisitados[i]:
            novaDistancia = distancia(a[pontoInicial], b[pontoInicial], a[i], b[i])
            if novaDistancia < menorDistancia:
                menorDistancia = novaDistancia
                pontoMaisProximo = i
    return pontoMaisProximo, menorDistancia

def obterPokemon(pokemon, hp, atk, defesa, numPontos):
    for i in range((numPontos-1)):
        novoNome = input(f"\nDigite o nome do {(i+1)}o Pokemon: ")
        novoHP, novoATK, novoDEF = input(f"\nDigite HP, ATK e DEF do {(i+1)}o Pokemon: ").split()
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
    
def main():
    x = []
    y = []
    pokemon = []
    hp = []
    atk = []
    defesa = []
    pontoInicial = 0
    pontoMaisProximo = 0
    impressao = (f"0")
    distancia_total = 0

    n = int(input("Digite o numero de pontos: "))

    obterCoordenadas(x, y, n)
    pontosVisitados = [False] * n
    pontosVisitados[0] = True

    for i in range(n - 1):
        pontoMaisProximo, menorDistancia = caminhoMaisCurto(x, y, pontoInicial, pontosVisitados)
        pontosVisitados[pontoMaisProximo] = True
        pontoInicial = pontoMaisProximo
        impressao += str(f" {pontoMaisProximo}")
        distancia_total += menorDistancia

    # Voltando para casa
    distancia_total += distancia(x[pontoInicial], y[pontoInicial], x[0], y[0])

    obterPokemon(pokemon, hp, atk, defesa, n)
    vitorias = [0] * (len(pokemon))

    for j in range(len(pokemon)):
        for k in range(j + 1, len(pokemon)):
            vencedor = batalha(hp, atk, defesa, j, k)
            if vencedor == -1:
                # Empate
                vitorias[vencedor] += 0
            else:  
                vitorias[vencedor] += 1 
        
    maiorNdeVitorias = -1
    for l in range(len(pokemon)):
        if vitorias[l] > maiorNdeVitorias:
            maiorNdeVitorias = vitorias[l]
            campeao = pokemon[l]

    print(f"\nCaminho: {impressao} 0")
    print(f"Distancia: {round(distancia_total,6)}")
    print(f"Campeao: {campeao}")
    print(f"Numero de vitorias: {maiorNdeVitorias}")
main()


