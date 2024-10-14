idade = float(input("Digite a sua idade:"))

if idade < 12:
    print("Voce é criança")
elif 12 <= idade < 18:
       print("Voce é adolescente")
elif 18 <= idade < 65:
      print("Voce é adulto")
else:
      print("Voce é vovo")              
      