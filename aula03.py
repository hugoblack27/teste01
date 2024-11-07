#condicionais if-elif-else

'''
no python, quando temos condiçõees para realizarmos ações, usamos o if-elif-else
SE | if |
-----------------
SENAO SE | elif |
-----------------
SENAO | else |
-----------------

sintaxe:
if : *condição* :
    *ação*
-----------------
elif : *condição*
    *ação*
-----------------
else :
    *ação*

****OBS: o python é uma linguagem de **IDENTAÇÃO OBRIGATÓRIA**, onde é possivel demarcar
    cada bloco com base no recuo da linha     
'''
print("1 - aluno")
print("2 - funcionario")
print("3 - visitante ")
tipoAcesso = input ("selecione uma opção: ")

if tipoAcesso == "1" or tipoAcesso == "2":
    print ("acesso liberado")
elif tipoAcesso == "3": 
    print("faça um cadastro pra entrar!")
else:
    print("acesso negado!")