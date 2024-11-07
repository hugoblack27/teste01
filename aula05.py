# criando uma lista =>[]
#essa lista tem 5 itens e 4 posições (0 a 4)

# print('lista: ', idade)

# print('posição 0:')
# print(idade[0])#exibe a posição 0 elemento da lista

# print('posição 2:')
# print(idade[2])#exibe a posição 2 elemento da lista

# print('posição 4:')
# print(idade[4])#exibe a posição 4 elemento da lista

# idade[2] = 25 #alterando valor de um item na lista

# print(idade)
# #len() <= determina o tamanho da lista, onde n é o nome da lista analisada
# print(len(idade)

# #inserindo um novo item no final da lista
# idade.append(50)
# print("append(50): ", idade)  

# #inserindo um novo item em uma posição dejesada, onde o primeiro valor
# # é a posição e o segundo é o item a ser inserido 
# idade.insert(3, 1)
# print("insert(0, 1): ", idade)

# #remove item por valor da lista
# idade.remove(30)
# print("remover(30): ", idade)

# #remove um item por posição da lista 
# del idade[1]
# print("del idade[1]: ", idade)

# #somar todos os valores da lista
# soma = sum(idade)
# print("soma todos os valores dentro da lista", soma)

# #slicing: fatia a lista em uma menor com base no intervalo
# novalista = idade[2:5]
# print("idade[2:5]: ", novalista)

# posição inversa
# print("idade [-1]: ", idade[-1])
# print("idade [-5]: ", idade[-5])
# print("idade [-4]: ", idade[-4])
# #print("idade [-6]: ", idade[-6])

# #invertendo uma lista
# idade_inversa = idade[::-1]
# print("idade inversa: ", idade_inversa)

#ordenando uma lista
# idades_ordenadas = sorted(idade_inversa)
# print("idades ordemadas => sorted(idade_inversa): ", idades_ordenadas)

# nova_lista = [30, 20, 80, 1, 50]
# print("lista: ", nova_lista)

# crescente = sorted(nova_lista)
# print("crescente: ", crescente)

# decrescente = sorted(nova_lista, reverse=True)
# print("decrescente: ", decrescente)