# nome = input(str("qual o seu nome? "))
# idade = int(input("qual sua idade"))

# print = ("qual o seu nivel de emergencia")
# if emergencia_preferencial (input("1 - emergencia preerencial (febre alta, )")):

# elif emergencia_grave (input("2 - emergencia grave (sangramento, fraturas visiveis ...)")):

# if  emergencia (input("3 - emergencia (dor intensa dificuldade respiratotia, ....)")):

# Solicita o nome do paciente
nome = input("Digite seu nome: ")
 
# Solicita a idade do paciente
idade = int(input("Digite sua idade: "))
 
# Solicita os sintomas do paciente
print("Informe seus sintomas: dor intensa, dificuldade respiratória, fratura, sangramentos, febre, dores leves ")
sintomas = input("Sintomas: ").split(", ")
 
# Inicializa a variável de classificação
classificacao = ""
 
# Verifica se há sintomas de emergência
if "dor intensa" in sintomas or "dificuldade respiratória" in sintomas or "perda de consciência" in sintomas:
    classificacao = "Emergência"
elif "fraturas" in sintomas or "sangramentos" in sintomas:
    classificacao = "Grave"
elif "febre" in sintomas or "dores leves" in sintomas:
    classificacao = "Preferencial"
 
# Adiciona prioridade para crianças e idosos
if (idade <= 12 or idade > 65) and (classificacao == "Emergência" or classificacao == "Grave"):
    classificacao += " (Prioridade)"
 
# Exibe o resumo da classificação
print(f"\nResumo da classificação para {nome}:")
print(f"Idade: {idade} anos")
print(f"Classificação: {classificacao}")