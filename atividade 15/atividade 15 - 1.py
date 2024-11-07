# '''
# Desenvolva um programa solicite uma temperatura e a escala. Depois 
# converta a temperatura de Celsius para Fahrenheit e vice-versa, 
# até que o usuário decida parar.
# '''
continuar = "s"
while continuar == 's':
    temperatura = float(input("digite a temperatura da sua cidade: "))
    graus = int(input("sua temperatura esta em °C (celsius) ou °F (Fahrenheit)?\n""1 - °C\n""2 - °F\n"))
    
    if graus == 1:
        Fahrenheit = temperatura * 1.8 + 32
        print(f"sua temperatura {temperatura} em °F (Fahrenheit) será: {Fahrenheit:.2f}°F",)

    elif graus == 2:
        celsius =  (temperatura - 32) / 1.8
        print(f"Sua temperatura {temperatura}°F em °C (Celsius) será: {celsius:.2}°C")
     
    
    else:
        print("Opção inválida. Por favor, digite 1 ou 2.")

    continuar = input("Deseja fazer outra conversão? (s/n): ").lower()
    # if continuar != 's':
    #      print("Programa encerrado.")
    

