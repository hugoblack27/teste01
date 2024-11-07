votos = 0 
votosTotais = 0
jair = 0
carlos = 0
neves = 0
nulo = 0 
branco = 0


while True:
    votos = input("olá, seja bem vindo a urna, escolha seu candidato: \n"
    "1. Candidato Jair Rodrigues  \n"
    "2. Candidato Carlos Luz \n"
    "3. Candidato Neves Rocha  \n"
    "4. Nulo\n"
    "5. Branco\n"
    "6. Finalizar votação\n")
    

    if votos == "1" :
     jair += 1
     votosTotais += 1

    elif votos == "2":
        carlos += 1
        votosTotais += 1

    elif votos == "3":
        neves += 1
        votosTotais += 1

    elif votos == "4":
        nulo += 1
        votosTotais += 1

    elif votos == "5":
        branco += 1
        votosTotais += 1

    elif votos == "6":
        print("\nResultados da votação:")
        print(f"Candidato Jair Rodrigues: {jair}  votos")
        print(f"Candidato Carlos Luz: {carlos} votos")
        print(f"Candidato Neves Rocha: {neves} votos")
        print(f"Nulos: {nulo} votos")
        print(f"Brancos: {branco} votos\n")

    elif votos != "6":
        print("voto inválido\n")

        if votosTotais > 0:
            porcentagemnulo = (nulo/votosTotais) * 100
            porcentagembranco = (branco/votosTotais) * 100
            print(f"porcentagem de votos nulos: {porcentagemnulo:.2f}%", )
            print(f"porcentagem de votos brancos: {porcentagembranco:.2f}% \n", )

            vencedor = jair + carlos + neves

            if jair > carlos and jair > neves :
                print ("jair foi o vencedor")
            
            elif carlos > jair and carlos > neves:
                print("carlos foi o vencedor")

            elif neves > jair and neves > carlos:
                print("neves foi o vencedor")
        
            

        
        
        




    

    
      
      
      

 


