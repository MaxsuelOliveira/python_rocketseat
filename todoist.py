import msvcrt
from datetime import datetime
tarefas = []

def criar_tarefa(status = False, titulo = "", data_created = datetime):

    if not titulo : 
        print("Título é obrigatorio.")

    if not data_created:
        print("Data da criacao é obrigatoria.")

    tarefa = {
        "status" : status,
        "titulo": titulo,
        "data_created" : data_created 
    }

    tarefas.append(tarefa)

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for i, tarefa in enumerate(tarefas, 1):
        completa = ""
        if tarefa["status"] == True : 
            completa = "X"
        
        print(f"{i}) - [{completa}] - {tarefa["titulo"]} - {tarefa["data_created"]}")
        # print(f'[{tarefa["ckeck"]}] - {tarefa["titulo"]}')

def atualizar_tarefa_status(index):
    if not index:
        print("Index é obrigatorio.")

    tarefas[index]["status"] = True

    print("Tarefa atualizada com sucesso !")

def apagar_tarefa(index):
    if not index : 
        print("O index é obrigatorio.")
        return
    tarefas.remove(index)
    
    return "Tarefa excluida com sucesso."

def remover_tarefas_finalizadas():
    total_tarefas_removidas = 0

    for i, tarefa in enumerate(tarefas, 1):
        if tarefa["status"] == True :
            tarefas.remove(tarefa)
            total_tarefas_removidas=+1

    return total_tarefas_removidas

def main():

    while True:
        print("\nTodoist V1.0\n")
        print("1 -> Criar tarefa")
        print("2 -> Listar tarefas")
        print("3 -> Conclir tarefa")
        print("4 -> Deletar tarefa")
        print("5 -> Remover tarefas finalizadas.")
        print("6 -> Sair")
        print("-"*50)
        opcao = int(input("\n> Escolha uma opção: "))
       
        if opcao == 1 :
            titulo = input("\n)Digite o título da sua tarefa : ")
            data_created = datetime.now()
            criar_tarefa(False, titulo , data_created)

        elif opcao == 2 :
            listar_tarefas()

            print("Pressione qualquer tecla para continuar...")
            msvcrt.getch()

        elif opcao == 3 :
            index = int(input("\n) Qual o id da tarefa ? "))

            if index < len(tarefas) : 
                print("O id nao é valido.")

            atualizar_tarefa_status(index)

        elif opcao == 4:
            index = int(input("\n) Qual o id da tarefa ? "))

            if index < len(tarefas) : 
                print("O id nao é valido.")

            result = apagar_tarefa(index)
            print(result)
        
        elif opcao == 5 : 
            result = remover_tarefas_finalizadas()
            print("Total de tarefas removidas foi {} !".format(result))

        elif opcao == 6 :
            break  

if __name__ == "__main__":
    main()
