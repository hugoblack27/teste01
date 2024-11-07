login_correto = "tds01"
login = ""
senha = ""
senha_correto = "123"


while (login!=login_correto or senha!=senha_correto):
    login = input("digite seu login: ")
    senha = input("digite sua senha: ")
    
    if login == login_correto and senha == senha_correto:
        print("logado com sucesso")
       
    else:
        print("refaça senha ou login errado")