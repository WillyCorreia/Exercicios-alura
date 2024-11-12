#Primeiro Quadrante: os valores de x e y devem ser maiores que zero;
#Segundo Quadrante: o valor de x é menor que zero e o valor de y é maior que zero;
#Terceiro Quadrante: os valores de x e y devem ser menores que zero;
#Quarto Quadrante: o valor de x é maior que zero e o valor de y é menor que zero;
#Caso contrário: o ponto está localizado no eixo ou origem.

coordenadasX = int(input("Coloque as coordenadas do eixo X: "))
coordenadasY = int(input("Coloque as coordenadas do eixo Y: "))

if (coordenadasX > 0 and coordenadasY > 0):
    # X positivo Y positivo = primeiro quadrante
    print (" Coordenadas do primeiro quadrante!")
elif (coordenadasX > 0 and coordenadasY < 0):
    # X positivo Y negativo = terceiro quadrante
    print ("Coordenadas do terceiro quadrante!")
elif (coordenadasX < 0 and coordenadasY > 0):
    # X negativo Y positivo = segundo quadrante
    print ("Coordenadas do segundo quadrante!")
elif (coordenadasX < 0 and coordenadasY < 0):
    # X negativo Y negativo = quarto quadrante
    print ("Coordenadas do quarto quadrante!")
else:
    # X=0 ou Y=0 = localizada no eixo central
    print ("Coordenadas localizadas no eixo ou origem!")