#solicite ao usuario o numero para ser divido e o divisor 

num3 = float(input('Digite o numero q quer dividir : '))
divisor = float (input("digite o divisor q deseja : "))
resultado = num3 % divisor  #apenas 1 / o resultado sera real 
print(f'o resultado da divisao de {num3} dividido por {divisor} é : {resultado}')