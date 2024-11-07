#sem while, está rodando bem

# valo1 = 0
# valo2 = 0
# valo3 = 0 
# valo4 = 0
# valo5 = 0
# contadorneg = 0

# print ("insira 5 tipos de valores diferentes")
# valo1 = float(input("insira o primeiro valor: "))
# valo2 = float(input("insira o segundo valor: "))
# valo3 = float(input("insira o terceiro valor: "))
# valo4 = float(input("insira o quarto valor: "))
# valo5 = float(input("insira o quinto valor: "))

# if valo1 < 0:
#     contadorneg += 1
# if valo2 < 0:
#     contadorneg += 1
# if valo3 < 0:
#     contadorneg += 1
# if valo4 < 0:
#     contadorneg += 1
# if valo5 < 0:
#     contadorneg += 1

# print("Quantidade valores negativos: ", contadorneg)

#########################################################

#com while tambem está rodando bem

contadorneg = 0
valores = 0

print("Insira 5 tipos de valores diferentes")

#while valores < 5 faz que repita o insira o valor apareça 5 vezes

while valores < 5:
    valor = float(input("Insira o valor: "))
    if valor < 0:
        contadorneg += 1
    valores += 1

print("Quantidade de valores negativos:", contadorneg)

