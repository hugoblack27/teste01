login_correto = "tds01"
senha_correto = "123"
login = ""
senha = ""
tentativas =  3

while (login != login_correto or senha != senha_correto) and tentativas > 0:

    login = input("digite seu login: ").lower()
    senha = input("digite sua senha: ").lower()
    
    if login == login_correto and senha == senha_correto:
        print("logado com sucesso")
        

    else:
        tentativas -= 1 
        print("refaça senha ou login errados. Tentativas restantes", tentativas)
    if tentativas == 0:
        print("usuario bloqueado")
