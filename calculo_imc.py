#Realiza o calculo de IMC de seu peso e altura.

peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))

def calcular_imc(peso, altura):
    imc = peso / (altura*altura)
    return imc
 
resultado = calcular_imc(peso, altura)
print(f"O seu IMC é: {resultado:.2f}")

def classificar_imc(imc):
    if imc < 18.5:
        return "Abaixo do peso."
    elif imc < 25:
        return "Peso Normal."
    elif imc < 30:
        return "Sobrepeso."
    else:
        return "Obesidade"
    
print(classificar_imc(resultado))