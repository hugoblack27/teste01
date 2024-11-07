numero = int(input("digite um numero: "))
div = numero % 2
divUm = numero % 5
divDois = numero % 10 

if div % 2 == 0:
    print("esse numero é divisivel por 2")
resultado = resultado + '2'

if divUm % 5 == 0:
    print("esse numero é divisivel por 5")
resultado = resultado + '5'

if divDois % 10 == 0:
    print("esse numero é divisivel por 10")
resultado = resultado + '10'

if (div % 2 != 0) and (divUm % 5 != 0) and (divDois % 10 != 0):
    print("esse numero não é divisivel por 2, 5 ou 10")
else:
    print("esse numero é divisivel por ", resultado)