# Inicializando a pontuação
pontuacao = 0

print("Qual a cor da luva?")
print("(a) azul")
print("(b) verde")
print("(c) vermelho")
print("(d) amarelo")
resposta = input("Digite a resposta (A, B, C, D): ").strip().upper()
if resposta == "A":  # Corrigido para "A"
    pontuacao += 2  # Corrigido para adicionar 2 à pontuação
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    print("Resposta incorreta. Pontuação atual:", pontuacao)

print("Qual a cor da água?")
print("(a) azul")
print("(b) verde")
print("(c) vermelho")
print("(d) amarelo")
resposta = input("Digite a resposta (A, B, C, D): ").strip().upper()
if resposta == "A":  # Corrigido para "A"
    pontuacao += 2  # Corrigido para adicionar 2 à pontuação
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    print("Resposta incorreta. Pontuação atual:", pontuacao)

print("Qual a cor da rede?")
print("(a) azul")
print("(b) verde")
print("(c) vermelho")
print("(d) amarelo")
resposta = input("Digite a resposta (A, B, C, D): ").strip().upper()
if resposta == "A":  # Corrigido para "A"
    pontuacao += 2  # Corrigido para adicionar 2 à pontuação
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    print("Resposta incorreta. Pontuação atual:", pontuacao)

print("Qual a cor da cortina?")
print("(a) azul")
print("(b) verde")
print("(c) vermelho")
print("(d) amarelo")
resposta = input("Digite a resposta (A, B, C, D): ").strip().upper()
if resposta == "A":  # Corrigido para "A"
    pontuacao += 2  # Corrigido para adicionar 2 à pontuação
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    print("Resposta incorreta. Pontuação atual:", pontuacao)

print("Qual a cor da parede?")
print("(a) azul")
print("(b) verde")
print("(c) vermelho")
print("(d) amarelo")
resposta = input("Digite a resposta (A, B, C, D): ").strip().upper()
if resposta == "A":  # Corrigido para "A"
    pontuacao += 2  # Corrigido para adicionar 2 à pontuação
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    print("Resposta incorreta. Pontuação atual:", pontuacao)

print("Qual a cor da lama?")
print("(a) azul")
print("(b) verde")
print("(c) vermelho")
print("(d) amarelo")
resposta = input("Digite a resposta (A, B, C, D): ").strip().upper()
if resposta == "A":  # Corrigido para "A"
    pontuacao += 2  # Corrigido para adicionar 2 à pontuação
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    print("Resposta incorreta. Pontuação atual:", pontuacao)

print("qual a probabilidade de ana ser irmã de beatriz e tia de diana?")
print("(a) azul")
print("(b) verde")
print("(c) vermelho")
print("(d) amarelo")

# Recebendo a resposta do usuário
resposta = input("Digite a resposta (A, B, C, D): ").strip().upper()
if resposta == "A":  # Corrigido para "A"
    pontuacao += 3  # Corrigido para adicionar 2 à pontuação
    print("Resposta correta! Pontuação atual:", pontuacao)
else:
    pontuacao -= 1  # Penalidade por resposta incorreta
    print("Resposta incorreta. Pontuação atual:", pontuacao)

print("\nPontuação total:", pontuacao)