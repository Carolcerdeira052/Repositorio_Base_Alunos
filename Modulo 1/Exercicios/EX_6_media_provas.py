# Escreva um programa que pede ao usuário o nome de um aluno e as notas de 3 provas que este aluno realizou.
# No fim o programa deve mostrar na tela a média das 3 provas
# Dica:
# Para calcular a média das provas você deve dividir a soma das notas das provas pela quantidade de provas realizadas
# media = soma / 3

# OUTPUT ESPERADO:

# | ______________________________ |
# | SISTEMA DE PROVAS
# | ______________________________ |
# | Nome do aluno: Fulano
# | Nota da primeira prova: 9.8
# | Nota da segunda prova: 7
# | Nota da terceira prova: 8.5
# | ______________________________ |
# | Aluno: Fulano 
# | Média: 8.43
# | Aluno aprovado
# | ______________________________ |

# ------------------------------------------ ESCREVA SEU CÓDIGO ABAIXO -----------------------------------------------------------

print("|---------------------------|")
print("SISTEMA DE PROVAS ")
print("|---------------------------|")
nome=input("| Nome do aluno:  ")
a=float(input("| Nota da primeira prova: "))
b=float(input("| Nota da segunda prova:  "))
c=float(input("| Nota da terceira prova:  "))
print("|---------------------------|")
media=(a+b+c)/3
print(f"Aluno:{nome}  | Aprovado {media >=5} ")
if  media>=5:
    print("Aluno aprovado")
else:
        print ("Aluno reprovado!")