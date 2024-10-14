nota1 = float(input("Digite uma nota"))
nota2 = float(input("Digite uma nota"))
nota3 = float(input("Digite uma nota"))
nota4 = float(input("Digite uma nota"))

soma = nota1 + nota2 + nota3 + nota4

media = soma / 4

if media >= 6:
    print(f"Parabens pela {media} media")
else:
    print("Voce falhou")    
