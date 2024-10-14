capital = float(input("Digite o seu capital:"))
investimento = float(input("Digite a sua taxa de juros:"))
tempo = float(input("Digite o tempo do investimento:"))

I = investimento / 100 

Juros = capital * I * tempo

print(Juros)