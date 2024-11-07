def calcular_prestacao(valor_total, numero_prestacoes):
   
    if numero_prestacoes < 12:
        return "O número de prestações deve ser no mínimo 12."

    
    if numero_prestacoes >= 36:
        valor_total *= 1.15 
    elif numero_prestacoes >= 24:
        valor_total *= 1.10 

    
    valor_prestacao = valor_total / numero_prestacoes
    return f"O valor de cada prestação é: R$ {valor_prestacao:.2f}"


valor_total = float(input("Digite o valor total em reais: "))
numero_prestacoes = int(input("Digite o número de prestações desejadas (mínimo 12): "))

resultado = calcular_prestacao(valor_total, numero_prestacoes)
print(resultado)


