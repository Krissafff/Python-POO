"""
*Criar variáveis para nome (str), idade (int),
*Altura (float) e peso (float) de uma pessoa,
*Obter o ano de nascimento da pessoa (baseado na idade e no ano atual)
*Obter o IMC da pessoa com 2 casas decimais (peso e na altura da pessoa)
* Exibir um texto com todos os valores na tela usando F-Strings (com as chaves)
"""

Nome = 'Henrique'
Idade = 22
Altura = 1.90
Peso = 98
Ano = 2022
Imc = 'temp'

Ano_Nascimento = Ano - Idade
Imc = Peso / (Altura ** 2)


print(F'Nasci no {Ano_Nascimento} ano e tenho o IMC de {Imc:.2f}')