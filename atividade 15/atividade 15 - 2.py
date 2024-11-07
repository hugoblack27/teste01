'''
Faça um programa que peça ao usuário quantos valores ele deseja somar, 
depois solicite a entrada desses números e em seguida exiba a soma e a média entre eles.
'''

valores = 0 
soma = 0
contador = 0 

valores = int(input("quantos valores você deseja somar?: "))

if valores > 0:

    while contador < valores:

        valor = int(input(f"digite o valor {contador + 1}: "))
        contador += 1
        soma += valor

        media = soma / valor

    print(f"essa é a soma entre eles {soma} e esse é o valor da média {media:.2f} ")
else:
    print("coloque um valor positivo")

