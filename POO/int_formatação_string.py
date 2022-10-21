nome = 'Henrique' #String
idade = 22 #Int
altura = 1.90 #Float
e_maior = idade > 18 #Bool
peso = 98
imc = 'temp'

imc = peso / (altura ** 2)
print('f {nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{n} tem {i} anos de idade e seu imc é {im}'.format(n=nome, i=idade, im=imc))