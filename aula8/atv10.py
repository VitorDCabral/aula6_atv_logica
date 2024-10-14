nota = float(input("Digite a sua nota:"))

if nota < 20:
    print("Voce tirou F")
elif 20  <=  nota <= 40:
    print("Voce tirou D")
elif 40 <= nota <= 60:
    print("Voce tirou C")
elif 60 <= nota <= 80:
    print("Voce tirou B")
else:
    print("Voce tirou A")             