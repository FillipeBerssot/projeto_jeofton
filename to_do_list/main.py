from funcoes import *

def menu():
    while True:
        opcao = input('''
                      ===============================
                      .:PROJETO: LISTA DE AFAZERES:.
                      ===============================
                      MENU:
                      [1] - .:ADICIONAR TAREFAS:.
                      [2] - .:LISTAR TAREFAS:.
                      [3] - .:ATUALIZAR TAREFAS:.
                      [4] - .:DELETAR TAREFA:.
                      [5] - .:ENCERRAR PROGRAMA:.
                      
                      ESCOLHA SUA OPÇÃO: ''').strip()
        
        if opcao == '1':
            adicionarTarefas()
        elif opcao == '2':
            listarTarefas()
        elif opcao == '3':
            atualizarTarefas()
        elif opcao == '4':
            deletarTarefas()
        elif opcao == '5':
            encerrarPrograma()
        else:
            print('OPS! Opção inválida! Tente Novamente.')

if __name__ == '__main__':
    menu()