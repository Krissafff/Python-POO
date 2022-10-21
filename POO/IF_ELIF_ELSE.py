#CONDIÇÕES IF, ELIF E ELSE

"""
if False:
    print("Verdadeiro.")
elif False:
    print("Agora é verdadeiro")
elif False:
    print('Mais uma verdadeira.')
else:
    print('A minha expressão não é verdadeira.')
"""   
     
#Operadores Relacionais
# == > >= < <= !=

"""   
num_1 = 2 #int
num_2 = 2 #int

print( num_1 == num_2)
print( num_1 > num_2)

nome = input('Qual é o seu nome? ')
idade = input('Qual é a sua idade? ')
idade = int(idade)

#Limite para pegar empréstimo
idade_menor = 20 #Muito jovem
idade_maior = 30 #Passou da idade

if idade >= idade_maior and idade <= idade_maior:
    print(F'{nome} pode pegar o empréstimo.')
else:
    print(F'{nome} Não pode pegar empréstimo.')
"""   

#Operadores Lógicos - and, or, not, in e not in

# (Verdadeiro ou falso) = falso
#comparacao1 and comparacao2

#Verdadeiro ou Verdadeiro
#comp1 or comp2

"""   
a = 2
b = 3
if b > a:
    print('B é maior do que A.')
else:
    print('A é maior do que B.')
    
nome = 'Henrique'

if 's' in nome:
    print("Existe a letra U no seu nome")
else:
    print('Não existe')
"""   
usuario = input('Nome do usuário: ')
senha = input("Senha do usuário: ")

usuario_bd = 'luiz'
senha_bd = '12345'

if usuario_bd == usuario and senha_bd == senha:
    print('Você está logado no sistema')
else:
    print('Usuário ou senha inválidos.')