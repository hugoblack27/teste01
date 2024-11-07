numero0_25 = 0
numero26_50 = 0
numero51_75 = 0
numero76_100 = 0

print("Insira valores entre 0 a 100 diferentes (negativo para parar)")

valor = 0

while valor >= 0:
    valor = int(input("insira um valor: "))
    
    if 0 <= valor <= 25:
        numero0_25 += 1

    elif 16 <= valor <= 50:
        numero26_50 += 1

    elif 51 <= valor <= 75:
        numero51_75 += 1

    elif 76 <= valor <= 100:
        numero76_100 += 1

print("Intervalo [0 à 25]:", numero0_25)
print("Intervalo [26 à 50]:", numero26_50)
print("Intervalo [51 à 75]:", numero51_75)
print("Intervalo [76 à 100]:", numero76_100)      