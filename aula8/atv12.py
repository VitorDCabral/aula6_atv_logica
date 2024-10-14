senha = ""
usuario = ""

while usuario != "vitor":
    usuario = input("Digite o seu usuário:")
    if usuario == "vitor":
      print("Acesso concedido!")
    else:
        print("Usuário incorreto, tente novamente.")


while senha != "12345":
    senha = input("Digite a senha: ")
    if senha == "12345":
        print("Acesso concedido!")
    else:
        print("Senha incorreta, tente novamente.")