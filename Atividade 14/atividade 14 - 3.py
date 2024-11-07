'''
Crie um algoritmo que, dado um número informado pelo usuário, imprima a tabuada dele de 1 a 10, 
de maneira que sejam impressos somente as multiplicações cujo resultado seja um número par.
'''

numero =  int(input("informe um numero: ")) 
somas = 1

print("a tabuada do numero", numero, "somente aparecerá o resultado em par")
while somas <= 10:
    resultado = numero * somas
    if resultado % 2 == 0:
      print(numero,"x",somas,"=",resultado)
    somas += 1 
