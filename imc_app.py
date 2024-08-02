# Inicia o loop
while True:
    # usuário informa os dados
    nome = str(input("Informe o seu nome: "))
    idade = int(input("Informe a sua idade: "))
    peso = str(input("Informe o seu peso em Kg: ")).replace(",", ".")
    altura = str(input("Informe a sua altura: ")).replace(",", ".")

    # Converção da tipagem dos dados
    peso = float(peso)
    altura = float(altura)

    # Cálculo do IMC
    imc = peso/(altura**2)

    # Mostra o valor do IMC
    print(f"IMC de {nome}: {imc}.")

    # Análise das condições
    if imc >= 40:
        print("Obesidade grau III.")
    elif imc >= 35:
        print("Obesidade grau II.")
    elif imc >= 30:
        print("Obesidade grau I.")
    elif imc >= 25:
        print("Sobrepeso.")
    elif imc >= 18.5:
        print("Peso normal.")
    else:
        print("Baixo peso.")
    # Verificar se o usuário deseja continuar
    continuar = input("Deseja continuar? (s/n)").lower()
    
    #verifica a opção do usuário
    if continuar == "s":
        continue
    else:
        break
    

