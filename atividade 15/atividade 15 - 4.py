'''
Escreva um programa que imprima um triângulo de números, 
onde cada linha tem um número a mais que a anterior, 
até um número n fornecido pelo usuário. Exemplo: Se digitar 5 precisa exibir
'''

forma = int(input("diga quantos numeros precisa ter seu triangulo: "))
print(f"seu programa vai ter a quantidade de {forma}")

quantidade = 1

while quantidade <= forma:
    linha = ""
    numero = 1 


    while numero <= quantidade:
        linha += str(numero) + " "
        numero += 1 

    print(linha.strip())

    quantidade += 1