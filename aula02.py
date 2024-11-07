#variaveis e tipos
'''
para criar variaveis no python, basta digitar o nome do identificador 
e usar o simbolo de igualdade (=) para fazer a atribuição, apos isso 
é só colocar o valor que deseja armazenar

Em python, as variaveis são dinamicamente tipadas ou seja, não precisamos
dizer o tipo dela quando a criamos, o que determina essa tipagem é o que
irá ser atribuido. Sendo assim., uma variavel pode guardar um texto (str)
e depois guardar um numero inteiro (int) por exemplo.
'''
# vairavel do tipo caractere --> string(str)
produto = "banana" # a string pode ser atribuida usando aspas smples ('') ou duplas("")

#variavel do tipo real --> float
valor = 4.3 #p/ tipo flutuante (float), usamos o ponto (.) para separar as casas descimais

#variavel do tipo inteiro --> intenger (int)
quantidade = 12 #p/ o tipo inteiro (int), basta escrever o valor sem as aspas

#variavel do tipo logica --> boolean (bool)
#True --> verdadeiro
#False --> falso
temEstoque = True # variaveis do tipo logico(bool) sempre guardam o valores true ou false

#para saber o tipo de variavel usamos a função type(), dentro dos parenteses passsamos
#a variaveç que queremos saber o tipo
#print("tipo da variavel produto: ", type(produto))
#print("tipo da variavel valor: ", type(valor))
#print("tipo da variavel quantidade: ", type(quantidade))
#print("tipo da variavel temEstoque: ", type(temEstoque))

#-------------------------------------------------------------------------------------------------------------------------------------------

#operadores aridimeticos
'''
soma -->   | + |
------------------------------------
subtração -->  | - |
------------------------------------
multiplicação -->  | * |
------------------------------------
divisão --> | / |
------------------------------------
divisão truncada (inteira)--> | // |
------------------------------------
potencia -->        | **  |
------------------------------------
módulo -->          |  %  |
------------------------------------


'''
#por default (padrão), todo input é uma string
n1 = int(input ("digite um numero ")) # int() transforma o valor para inteiro

#float() transforma o valor para real
n2 = input ("digite outro numero ")
n2 = float(n2) 

# o mais é usado para somar (quando usado para numeros)
#e para concatenar (quando usados em strings)
soma = n1 + n2
sub= n1 - n2
mult = n1 * n2
div = n1 / n2
divTrun = n1 // n2
mod = n1 % n2
pot = n1 ** n2

# print("soma: ", n1, "+", n2, "=", soma)#forma conatenada
# print(f"subtração: , {n1} - {n2} = {sub}")#forma interpoada5
# print(f"multiplicação: {n1} * {n2} = {mult}")
# print(f"divisão: {n1} / {n2} = {div}")
# print(f"divisão truncada: {n1} * {n2} = {divTrun}")
# print(f"módulo: {n1} * {n2} = {mod}")
# print(f"potencia: {n1} ** {n2} = {pot}")

#---------------------------------------------------------------------

#operadores relacionadas

'''
igual -->   | == |
------------------------------------
diferente -->  | != |
------------------------------------
maior que  -->  | > |
------------------------------------
menor que --> | < |
------------------------------------
menor igual --> | <= |
------------------------------------
maior igual -->        | >= |
------------------------------------
'''
#operadores logicos 

'''
E -->   | and |
------------------------------------
OU -->  | or |
------------------------------------
NÂO -->  | not |
------------------------------------
'''