nome = input("Digite seu login: ")
senha = int(input("Digite sua senha: "))

if(nome == "willycorreia"):
    if(senha == 1234):
        print("login e senha corretos")
    else:
        print("senha inválida")
else:
    print("login inválido")
    