print("|-------------------------------|")
print("|    SISTEMA DE PROVAS    ")
print("|-------------------------------|")
limite=int(input("Digite quantas provas o aluno fez:"))
cont = 1
soma=0
while cont <= limite:
    nota=float(input(f"Digite a nota da prova {cont}: "))
    soma = soma + nota 
    cont = cont +1
    media=soma / nota 
print(f'A media do aluno é {media}')
