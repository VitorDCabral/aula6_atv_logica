usuario = ""
senha = ""

max_tentativas_usuario = 3
max_tentativas_senha = 3
tentativas_usuario = 0
tentativas_senha = 0

while usuario != "vitor" and tentativas_usuario < max_tentativas_usuario:
    usuario = input("Digite o seu usuário: ")
    if usuario == "vitor":
        print("Usuário correto!")
    else:
        tentativas_usuario += 1
        print("Usuário incorreto, tente novamente.")
        if tentativas_usuario == max_tentativas_usuario:
            print("Número máximo de tentativas de usuário atingido. Acesso negado.")
            break

if usuario == "vitor":
    while senha != "12345" and tentativas_senha < max_tentativas_senha:
        senha = input("Digite a senha: ")
        if senha == "12345":
            print("Acesso concedido!")
        else:
            tentativas_senha += 1
            print("Senha incorreta, tente novamente.")
            if tentativas_senha == max_tentativas_senha:
                print("Número máximo de tentativas de senha atingido. Acesso negado.")
