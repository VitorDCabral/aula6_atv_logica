numero = int(input("Digite um número para ver sua tabuada: "))
contador = 0

while contador <= 10:
    resultado = numero * contador
    print(f"{numero} * {contador} = {resultado}")
    contador += 1
