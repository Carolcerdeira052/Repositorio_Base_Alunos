# Escreva um programa que pede ao usuário o nome, idade, e-mail e senha para um cadastro e depois exiba as informações na tela:

# OUTPUT ESPERADO:

# | ------------------------------ |
# | ---------- CADASTRO ---------- |
# | ------------------------------ |
# | Nome: Maria
# | Idade: 17
# | Email: maria@email.com
# | Senha: 123123

# | ------------------------------ |
# | ----- USUÁRIO CADASTRADO ----- |
# | Seja bem vindo(a) Maria!
# | Email: maria@email.com
# | ------------------------------ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------


print("|-------------------------------------|")
print("|-----------CADASTRO------------------|")
print("|-------------------------------------|")
nome=input("Digite seu nome:  ")
idade=input("Digite sua idade: ")
email=input("digite seu e-mail: ")
senha=input("digite sua senha: ")

print("|-------------------------------------|")
print("|--------USUARIO CADASTRO-------------|")
print("|Seja bem vindo(A)"(nome))
print("| E-mail:"(email))
print("|--------------------------------------|")
