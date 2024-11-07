'''
Faça um Programa que leia um vetor de 10 caracteres,
 e diga quantas consoantes foram lidas. Imprima as consoantes
'''
vetor = []
for i in range (10):
    caractere = input(f"digite o {i + 1}°  caractere: ")
    vetor.append(caractere)

vogais = "aeiouAEIOU"

consoantes = []

for caractere in vetor:
     if caractere.isalpha() and caractere not in vogais:
        consoantes.append(caractere)

print(f"Total de consoantes lidas: {len(consoantes)}")
print(f"Consoantes: {', '.join(consoantes)}")