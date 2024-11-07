'''
laço for: usamos esse tipo de interação quando sabemos quantas
vezes será necessárias o laço acontecer, ou seja, não dependenmos
de uma condição como no while
'''
# lista_nomes = ["ana","joão","antonia","marcio"]

# for nome in lista_nomes:#para cada nome na lista_nomes
#     print(nome)#exibe o nome
'''
1- receba nomes dos usuario até que o usuario digite 0, 
depois exiba quais desses nomes iniciam com a letra A
'''
lista_nomes = []#cria uma lista vazia
n=input("digite um nome: ")#solicita um nome ao usuário

while n != "0":#enquanto o nome digitado for diferente de 0
    lista_nomes.append(n)#adiciona o nome digitado na lista
    print(lista_nomes)#exibe nova lista
    n =  input("digite um nome:")#pede outro nome

# print("lista final: ",lista_nomes)#mostra a lista final

# for nome in lista_nomes:
#     nome = nome.upper()
#     if nome.startswith("A"):
#         print(nome)

'''
2- faça um programa que receba 10 numeros e ao final, 
exiba o dobro do valor digitado, se esse numero for maior que 8 
'''
# lista_valores = []

# for n in range(3):
#     v = int(input("digite um número"))
#     lista_valores.append(v)
#     print(lista_valores)

# print(range(10))#a função range cria um intervalo
# print(list(range(10)))

# print("#"*30)

# print(range(2, 10))#determinando o inicio e o fim do intervalo
# print(list(range(2,  10)))

# print("#"*30)

# #determinando o inicio e o fim do intervalo e o passo
# print(range(1, 11, 3))
# print(list(range(1, 11, 3)))
