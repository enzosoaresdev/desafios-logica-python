#O objetivo é imprimir os números de 1 a 100, substituindo múltiplos de 3 por "Fizz", 
#múltiplos de 5 por "Buzz", e múltiplos de ambos por "FizzBuzz"

num = 1

while (num<=100):
    if(num%3==0):
        print("Fizz")
    elif(num%5==0):
        print("Buzz")
    elif(num%15==0):
        print("FizzBuzz")
    else:
        print(num)
    num += 1