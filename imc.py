# Dados do Usuário
nome = input("Digite seu nome: ")
altura = float(input("Digite sua altura: "))
peso = float(input("Digite seu peso: "))

# Calculo
imc = (peso/(altura * 2))


# Resultados
if imc <= 18.5:
    print(f'Olá {nome.capitalize()}! Seu IMC é de {imc:.2f} e está classificado como magreza')
elif imc < 24.9:
    print(f'Olá {nome.capitalize()}! Seu IMC é de {imc:.2f} e está classificado como normal')
elif imc < 29.9:
     print(f'Olá {nome.capitalize()}! Seu IMC é de {imc:.2f} e está classificado como sobrepeso')
else:
    print(f'Olá {nome.capitalize()} Seu IMC é de {imc:.2f} e está classificado como obeso')
#    print('Olá', nome, 'Seu IMC é de', imc, "e está classificado como obeso")

