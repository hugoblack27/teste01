# numero = 0
# limite = int(input("digite qual numero você quer contar: "))
# while numero <=  limite: #enquanto o numero for menor ou igual que 5 ou baseado na quantidade que a pessoa colocou nos numeros
#     print(numero)#exibe o numero

#     #o simbolo de += serve para fazer uma soma com atribuição
#     #numero += 1 ==> numero = numero + 1
#     numero += 1 #soma 1 na variavel numero


#.lower() transforma para minusculo
#print (nome.lower())
#.upper() transforma para maiusculo
#print (nome.upper())

#starswith(string buscada) faz uma busca no inicio da palavra
#print(nome.startswith('a')) #busca palavras que iniciam com 'a'

#endswith (string buscada) faz uma busca no final da palavra
#print(nome.endswith('a'))# busca palavras que termina com 'a'

while True:
    nome = input("digite um nome: ")

    if nome.lower().startswith('a'):
        print("nome: ",nome)
    else:
        print("Nome não aceito!")