# Escreva um código que mostre na tela um "MENU" de opções de operações matematicas (Adição, Subtração, Divisão e Multiplicação)
# O usuário deve escolher uma das opções e depois inserir dois números para serem calculados de acordo com a operação escolhida.
# No fim mostre o resultado da operação

# OUTPUT ESPERADO:

#----------------------------------------- Exemplo 1 (Soma)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 1
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 20.0

# ----------------------------------------- Exemplo 2 (Multiplicação)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 3
# | Digite o primeiro número:10
# | Digite o segundo número:10
# | O resultado é: 100.0

# ----------------------------------------- Exemplo 3 (Opção inválida)

# |------------------------------|
# | Calculadora
# |------------------------------|
# | 1 - Soma
# | 2 - Subtração
# | 3 - Multiplicação
# | 4 - Divisão 
# |------------------------------|
# | Escolha uma das opções: 6
# | Digite o primeiro número:1
# | Digite o segundo número:2
# | ERRO. Escolha uma opção válida.



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------
print("|--------------------------------|")
print("|  CALCULADORA                   |")
print("|--------------------------------|")
print("| 1 soma                         |")
print("| 2 subtração                    |")
print("| 3 multiplicação                |")
print("| 4 divisão                      |")
print("|--------------------------------|")
opcao=int(input("Escolha uma das opção: "))
n1=float(input("Escolha o primeiro numero: "))
n2=float(input("Escolha o segundo numero: "))
if opcao == 1 :
    print("o resultado é" , n1+n2)
elif opcao == 2:
     print("o resultado é" , n1-n2)
elif opcao == 3:
      print("o resultado é" , n1*n2)
elif opcao== 4:
      print("o resultado é" , n1/n2)
else :
     print("Escolha uma opção do menu!")