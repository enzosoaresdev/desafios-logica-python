#Exercicio3

print("Bem-Vindo ao aplicativo do banco!")

tentativas = 0
senhacorreta = False

while tentativas <3 and senhacorreta == False:
    senha = input("Digite sua senha: ")
    if (senha=="PythonMestre"):
        senhacorreta = True
    else:
        tentativas += 1
        print(f"Senha incorreta, tentativa {tentativas} de 3.")

if senhacorreta == True:
    print("Parabéns, acesso concedido!")
else:
    print("Acesso bloqueado!")