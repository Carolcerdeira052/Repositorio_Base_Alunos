
print("IMC(Indice de massa corporasl=Será que seu peso )")
nome=input("Nome de Usuario: ")
peso=float(input("Qual seu peso?: "))
altura=float(input("Qual sua altura?: "))
imc= peso / (altura ** 2)
if imc <=18.5 :
    print("Abaixo do Peso!!")
elif imc <=24.9:
    print("Peso normal")
elif imc >=29.9:
    print("Sobrepeso")
elif imc >=34.9:
    print("Obesidade Grau I")
elif imc >= 39.9 :
    print("Obesidade Grau II")
elif imc >=40.0 :
    print("Obesidade Grau III (mórbida)")



































