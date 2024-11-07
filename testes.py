# Inicializa um vetor vazio
vetor = []

# Lê 10 caracteres do usuário
for i in range(10):
    caractere = input(f"Digite o {i + 1}º caractere: ")
    vetor.append(caractere)

# Define as vogais
vogais = 'aeiouAEIOU'

# Inicializa a lista de consoantes
consoantes = []

# Conta as consoantes
for caractere in vetor:
    if caractere.isalpha() and caractere not in vogais:
        consoantes.append(caractere)

# Exibe o resultado
print(f"Total de consoantes lidas: {len(consoantes)}")
print(f"Consoantes: {', '.join(consoantes)}")
