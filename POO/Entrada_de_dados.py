"""
Entrada de dados
"""

nome = input('Qual o seu nome? ')
idade = input('Qual a sua idade? ')
ano_nascimento = 2022 - int(idade)
print(F'{nome} tem {idade} de idade e nasceu no ano {ano_nascimento}' F'{type(nome), type(idade)}')

numero_1 = int(input('Digite um número: '))
numero_2 = input('Digite outro número: ')
numero_2 = int(numero_2)
print( numero_1 ** numero_2 )