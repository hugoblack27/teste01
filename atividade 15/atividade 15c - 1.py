'''
Crie um programa que solicite ao usuário um número inteiro n e imprima um quadrado de asteriscos (*) de tamanho n x n.


'''




forma = int(input("diga quantos numeros precisa ter seu triangulo: "))

quantidade = 0

while quantidade < forma:
    numero = 0
    linha = ""
    

    while numero < forma:
        linha += "* "
        numero += 1 

    print(linha.strip())

    quantidade += 1

