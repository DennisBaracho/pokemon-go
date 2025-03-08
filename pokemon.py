#**************************************************************************
#Trabalho Computacional – Introdução à Programação - 2024/2
#Grupo: 
#Dennis Francisco Guimarães de Oliveira Baracho
#**************************************************************************

import math
def distancia(x1, y1, x2, y2):
     # Calculo da distancia entre 2 pontos usando a formula da distancia euclidiana.
     return math.sqrt((pow((x1 - x2),2)) + pow((y1 - y2),2))

def obterCoordenadas(listaX, listaY, numPontos):
    # Obtendo os valores x e y de cada ponto.
    for i in range(numPontos):
        novoX, novoY = input().split()
        listaX.append(int(novoX))
        listaY.append(int(novoY))

def caminhoMaisCurto(x, y, pontoInicial, pontosVisitados):
    # Calculando a distancia entre um pontoInicial fixado anteriormente e todos os outros pontos disponíveis.
    menorDistancia = math.inf
    for i in (range(len(x))):
        # Caso o ponto não tenha sido visitado, calcula a distância entre o pontoInicial e ele.
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

    # Executa a função de caminhoMaisCurto repetidas vezes, o PontoInicial se torna o PontoMaisProximo a cada execução. Na lista de pontosVisitados, o pontoMaisProximo é marcado como True para não ser utilizado novamente na função CaminhoMaisCurto.
    for j in range(n - 1):
        pontoMaisProximo, menorDistancia = caminhoMaisCurto(x, y, pontoInicial, pontosVisitados)
        pontosVisitados[pontoMaisProximo] = True
        pontoInicial = pontoMaisProximo
        caminho += str(f" {pontoMaisProximo}")
        distanciaTotal += menorDistancia
    
    # No caminho de volta, o pontoMaisProximo se torna 0. E o pontoInicial é o último utilizado.
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
    # Enquanto ambos os pokémon estiverem com HP maior que 0, calcula-se o dano recebido por cada um. Caso o dano total recebido pelo defensor seja maior que seu HP, o atacante ganha, e vice-versa. 
    while ((hp[pokemonAtacante] - danoRecebidoAtacante) > 0) and ((hp[pokemonDefensor] - danoRecebidoDefensor) > 0):
        # Para evitar casos em que a defesa é maior que o ataque e o dano é negativo, utiliza-se a função max, escolhendo o 0 no lugar do valor negativo.
        danoRecebidoDefensor += max(0, atk[pokemonAtacante] - defesa[(pokemonDefensor)])
        if (hp[pokemonDefensor] - danoRecebidoDefensor) <= 0:
            return pokemonAtacante
        danoRecebidoAtacante += max(0, atk[pokemonDefensor] - defesa[(pokemonAtacante)])
        if (hp[pokemonAtacante] - danoRecebidoAtacante) <= 0:
            return pokemonDefensor
        # Caso o dano recebido seja 0 tanto para o atacante quanto para o defensor, será empate, pois a batalha será infinita e nenhum pokémon vencerá.
        if (danoRecebidoAtacante <= 0) and (danoRecebidoDefensor <= 0):
            return empate
    
def definirCampeao(pokemon, hp, atk, defesa, vitorias):
    # Na primeira execução, o pokémon atacante 0 batalha com todos os outros. Após a primeira execução, cada pokemon atacante batalha contra todos, exceto os que já enfrentou anteriormente, atacando ou defendendo.
    for pokemonAtacante in range(len(pokemon)):
        for pokemonDefensor in range(pokemonAtacante + 1, len(pokemon)):
            vencedor = batalha(hp, atk, defesa, pokemonAtacante, pokemonDefensor)
            # Caso a função receba -1 (Empate), não há aumento nem decremento de vitórias.
            if vencedor == -1:
                vitorias[vencedor] += 0
            # Do contrário, o pokémon vencedor recebe +1 vitória
            else:  
                vitorias[vencedor] += 1 
        
    # Somadas as vitórias de cada pokémon, percorre-se a lista em busca de quem teve o maior número de vitória, definido como campeão.
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
    # Criando listas x e y, coordenadas dos pontos
    x = []
    y = []

    # Criando listas que armazenam os dados dos pokémon. O primeiro pokémon tem seu nome, hp, atk e def armazenado no índice 0 de cada lista, e assim por diante.
    pokemon = []
    hp = []
    atk = []
    defesa = []

    # Obtendo o número de pontos e verificando se é menor/igual a 0 ou maior que o máximo de 400.
    n = int(input())
    while n <= 0 or n > 400:
        n = int(input())

    # Executando a função obterCoordenadas, que recebe coordenadas de pontos de acordo com o número de pontos.
    obterCoordenadas(x, y, n)

    # Criando uma lista de pontos visitados com base no número de pontos, os que já foram visitados são definidos como True, os que ainda não foram são definidos como False. Como iniciamos em 0, pontosVisitados[0] é verdadeiro.
    pontosVisitados = []
    distanciaTotal = 0
    for i in range(n):
        pontosVisitados.append(False)
    pontosVisitados[0] = True

    # Obtendo a distância total e a impressão final do caminho por meio da função definirCaminho. As listas x, y e pontosVisitados são utilizadas para calcular os caminhos mais curtos e a volta para casa, pontosVisitados serve para ignorar pontos por onde o jogador já passou. n define o número de pontos a visitar.
    distanciaTotal, caminho = definirCaminho(x, y, pontosVisitados, n)
    
    # Obtendo o nome e os status de HP, ATK, DEFESA de cada pokémon, o número de pokémon é com base no número de pontos, desconsiderando o ponto 0, onde não se captura nenhum (n-1).
    obterPokemon(pokemon, hp, atk, defesa, (n-1))

    # Criando uma lista de vitórias de acordo com o número de pokémon, onde cada índice equivale a um pokémon. Todos iniciam com 0 vitórias.
    vitorias = []
    for k in range(len(pokemon)):
        vitorias.append(0)

    # Executando a função definirCampeao, as batalhas ocorrem apenas entre pokémon que não batalharam entre si. O campeao é definido a partir de quem teve mais vitórias. A função retorna o campeao e seu numero de vitorias.
    campeao, maiorNdeVitorias = definirCampeao(pokemon, hp, atk, defesa, vitorias)

    # Exibindo os resultados finais: o caminho, a distancia percorrida, o campeão e o seu número de vitórias.
    saida(caminho, distanciaTotal, campeao, maiorNdeVitorias)
main()


