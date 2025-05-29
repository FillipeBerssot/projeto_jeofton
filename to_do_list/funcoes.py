import json

CAMINHO_ARQUIVO = 'tarefas.txt'

#Função de adicionar tarefas:
def adicionarTarefas():
    while True:
        tarefa = input('Digite a tarefa que deseja adicionar: ').strip().capitalize()

        try:
            with open(CAMINHO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
                arquivo.write(json.dumps(tarefa, ensure_ascii=False) + '\n')

            print(f'\nTarefa adicionada com sucesso!\n')

        except Exception as erro:
            print(f'\nErro ao adicionar tarefa: {erro}\n')

        resposta = validarSaida()
        if resposta == 'N':
            print('\nAdicionar tarefas foi encerrado. Obrigado!')
            print('======================================================================================')
            break

#Função de listar tarefas:
def listarTarefas():
    while True:
        try:
            with open(CAMINHO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
                tarefas = arquivo.readlines()
                if tarefas:
                    print('\nTarefas Cadastradas:\n')
                    tarefas_decodificadas = [json.loads(linha.strip()) for linha in tarefas]
                    for i, tarefa in enumerate(tarefas_decodificadas, start=1):
                        print(f'{i} - {tarefa}')
                else:
                    print('\nNenhuma tarefa foi cadastrada ainda.')
                    break

        except FileNotFoundError:
            print('Nenhum arquivo de tarefas encontrado.')
            return
        
        except Exception as erro:
            print(f'ERRO ao listar tarefas: {erro}')

        resposta = validarSaida()
        if resposta == 'N':
            print('\nListar tarefas foi encerrado. Obrigado!')
            print('======================================================================================')
            break
        
#Função de validar a saída:
def validarSaida():
    while True:
        resposta = input ('Deseja continuar? [S/N]: ').strip().upper()

        if resposta in 'SN':
            return resposta
        
        else:
            print('OPS! Opção inválida! Por favor, digite [S] para continuar ou [N] para sair.')

#Função de encerrar o programa:
def encerrarPrograma():
    print('\nEncerrando o programa. Obrigado por usar o nosso sistema de Lista de Afazeres!')
    print('======================================================================================')
    exit()