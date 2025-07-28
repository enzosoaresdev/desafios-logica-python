#Programa que realiza o calculo de IMC (índice de Massa Corporal).

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

def calcular_imc(peso, altura):
    imc = peso / (altura*altura)
    return imc

resultado = calcular_imc(peso, altura)

def classificacao_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso."
    elif imc < 25:
        return "Peso normal"
    elif imc < 30:
        return "Sobrepeso"
    else:
        return "Obesidade"

print(classificacao_imc(resultado))