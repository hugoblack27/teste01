'''
Faça um Programa que leia um vetor de 5 números inteiros, 
mostre a soma, a multiplicação e os números
'''

numeros = [ ]

for i in range (5):
    vetor = int(input("digite um numero: "))
    numeros.append(vetor)

soma = sum(numeros)
multiplicação = 1 
for num in numeros:
    multiplicação *= num

print("numeros: ", numeros)
print("soma: ", soma)
print("multiplicação: ", multiplicação)