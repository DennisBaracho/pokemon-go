import math
def distancia(x1, y1, x2, y2):
     return math.sqrt((pow((x1 - x2),2)) + pow((y1 - y2),2))

def main():

     i = 0
     while i < 10:     
          distanciaPeF = distancia(a, b, 1, 2)
          distanciaPeP2 = distancia(a, b, c, d)
          if distanciaPeF == distanciaPeP2:
               print(f"{distanciaPeF} igual a {distanciaPeP2}")

