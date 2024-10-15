for numero in range(1, 11):
    if numero % 2 == 0:
        print(f"Número par encontrado: {numero}, interrompendo o laço.")
        break
    else:
        print(f"{numero} é impar, continuando.") 
else:
    print("Todos os números foram ímpares")        