print("Digite três notas para calcular a média do aluno.")
num1 = int(input("Digite a primeira nota: "))
num2 = int(input("Digite a segunda nota: "))
num3 = int(input("Digite a terceira nota: "))

media = (num1+num2+num3)/3
media = int(media*10)/10

print(f"A média das notas do aluno é: {media}")