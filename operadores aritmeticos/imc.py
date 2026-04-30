#crie um progama de calculo de imc, recebendo do usuario os dados de peso e altura 
#lembrando que imc = 1 (peso / (alturaº))
#usaremos para (º potencia)**

nome = input("Digite o seu nome: ")
peso = float (input("digite o seu peso: "))
altura = float (input("Digite a sua altura: "))
imc = (peso /(altura ** 2))  #potencia 
print (f'Obrigada {nome}, o seu peso é {peso} e a sua altura {altura}, então o seu imc é: {imc: .2f}')