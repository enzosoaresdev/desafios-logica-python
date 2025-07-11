#Programa para veficar se um aluno foi aprovado ou não de acordo com suas notas
print("Digite as notas sequencialmente: ")
nota1 = int(input("Primeira nota: "))
nota2 = int(input("Segunda nota: "))
nota3 = int(input("Terceira nota: "))

media = (nota1+nota2+nota3)/3
media = int(media*10)/10

if(media>=6):
    print("Aluno aprovado!")
else:
    (media<6)
    print("Aluno reprovado!")
print(f"Média do aluno: {media}")