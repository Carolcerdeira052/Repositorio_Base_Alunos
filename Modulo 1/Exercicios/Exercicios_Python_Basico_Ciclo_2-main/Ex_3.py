# Utilize um loop while e um loop for para adicionar itens na lista.
# Peça para que o usuário digite quantos filmes deseja adicionar, e também os nomes dos filmes



# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

filmes = [] # Não apague esta lista
qt_filmes = int(input('Quantos filmes deseja colocar na lista? '))
# LOOP WHILE

# cont = 1
# while cont <= qt_filmes:
#     nome=input(f"Digite o nome do {cont} filme: ")
#     filmes.append(nome)
#     cont = cont + 1


#print(filmes)


# LOOP FOR
for n in range(1,qt_filmes+1):
    nome=input(f"Digite o nome do filme {n}: " )
    filmes.append(nome )
print(filmes )