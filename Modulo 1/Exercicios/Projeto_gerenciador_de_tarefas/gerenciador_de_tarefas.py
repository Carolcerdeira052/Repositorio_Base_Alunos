import os 

tarefas = {
    "tarefas": [ "Arrumas o quarto" , "lavar a louça"] ,
    "datas" : ["17/10" , "17/10"]
}


def mostrar_tarefas():
    barra = f'|{60*'-'}|'
    print (barra)
    for i in range(len(tarefas["tarefas"])):
       print(f"| {i+1} tarefa : {tarefas["tarefas"]}| Data: {tarefas["datas"][i]}")
    input("| aperte 'ENTER' para continuar...")

def adicionar_tarefa():
    barra = f'|{60*'-'}|'
    print (barra)
    tarefa = input("| Nome da tarefa:  ")
    data = input("| Data: ")
    tarefas["tarefas"].append(tarefa)
    tarefas["datas"].append(tarefa)
    print("|Tarefa adicionada com sucesso! ")

    input("| aperte 'ENTER' para continuar...")
    
def remover_tarefa():
    barra = f'|{60*'-'}|'
    print (barra)
    for i in range(len(tarefas["tarefas"])):
       print(f"| {i+1} - tarefa: {tarefas['tarefas'][i]} | Data:{tarefas["datas"][i]}")
    id_tarefa = int(input("| Digite o numero da tarefa que deseja remover:  "))
    tarefa = tarefas ["tarefas"].pop(id_tarefa-1)
    tarefas["datas"].pop(id_tarefa-1)
    print(f"| Tarefa '{tarefa}' removida com sucesso!" )
    input("| aperte 'ENTER' para continuar...")

    if id_tarefa > 0:
        tarefa = tarefas['tarefas'].pop(id_tarefa-1)
        tarefas["datas"].pop(id_tarefa-1)
    else:
        print("| ID invalido.")
        input("| Aperte 'ENTER' para continuar...")

def menu():
    while True:
        try:
            os.system("cls")
            barra = f'|{30*'-'}|'
            print(barra)
            print("|GERENCIADOR DE TAREFAS")
            print(barra)       
            print(" | 1- Mostrar tarefas")
            print(" | 2- Adicionar tarefa ")
            print(" | 3- Remover tarefa")
            print(" | 4- Sair")
            print (barra)
            opc = int(input("| Escolha um numeroda opção: "))
            if opc == 1:
                os.system("cls")
                mostrar_tarefas()
            elif opc == 2:
                os.system("cls")
                adicionar_tarefa()
            elif opc == 3:
                os.system("cls")
                remover_tarefa()
            elif opc == 4:
                os.system("cls")
                print("| Saindo do programa...")
                break
            else:
                os.system("cls")
                print("| Opção invalida...")
                input("| Aperte 'ENTER' para continuar...")
        except: 
            print("| ERRO! Escolha uma opção válida")
            input("| Aperte 'ENTER' para continuar...")