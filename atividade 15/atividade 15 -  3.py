'''
Peça ao usuário para inserir um número e um limite 
e mostre a tabuada de multiplicação desse número até o limite.
'''

numero = int(input("digite um valor: "))
limite = int(input("agora decreta um limite: "))

print (f"a tabuada será do numero{numero} ao limte {limite}")

contador = 1 

while contador <= limite :
    resultado = numero * contador
    print(f"{numero} x {limite} = {resultado}")
    contador += 1 
