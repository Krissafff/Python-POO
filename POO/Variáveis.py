"""
Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = 'Henrique' #String
idade = 22 #Int
altura = 1.90 #Float
e_maior = idade > 18 #Bool
data_1 = True #Bool
data_atual = 2022 #Int
peso = 98
imc = 'temp'

print('Nome:',nome)
print('Idade:', idade)
print('Altura:', altura)
print('É maior:', e_maior)
print(idade * altura)

imc = peso / (altura ** 2)
print(nome, 'tem', idade, 'de idade e seu imc é', imc)