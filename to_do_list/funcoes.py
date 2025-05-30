import json

CAMINHO_ARQUIVO = 'tarefas.txt'

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

def atualizarTarefas():
    while True:
        caminho_arquivo = CAMINHO_ARQUIVO

        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                tarefas_json = arquivo.readlines()
            if not tarefas_json:
                print('\nNenhuma tarefa encontrada para atualizar.')
                break
            
        except FileNotFoundError:
            print('\nNenhum arquivo de tarefas encontrado.')
            return

        tarefas_decodificadas = [json.loads(linha.strip()) for linha in tarefas_json]

        print('\nQual tarefa você deseja atualizar?')
        
        for i, tarefa in enumerate(tarefas_decodificadas):
            print(f'{i + 1} - {tarefa}')

        while True:
            try:
                indice = int(input('Digite o número da tarefa que deseja atualizar: '))
                if 1 <= indice <= len(tarefas_decodificadas):
                    break
                else:
                    print('OPS! Número inválido. Tente novamente.')

            except ValueError:
                print('OPS! Entrada inválida. Por favor, digite apenas o número.')

        indice_tarefa = indice - 1
        nova_tarefa = input('Digite a nova tarefa: ').strip().capitalize()

        if not nova_tarefa:
            print('\nOPS! A nova tarefa não pode ser vazia.')
            continue
        
        tarefas_json[indice_tarefa] = json.dumps(nova_tarefa, ensure_ascii=False) + '\n'

        try:
            with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                arquivo.writelines(tarefas_json)
            print('\nTarefa atualizada com sucesso!')

        except Exception as erro:
            print(f'ERRO ao atualizar a tarefa: {erro}')

        resposta = validarSaida()
        if resposta == 'N':
            print('\nAtualizar tarefas foi encerrado. Obrigado!')
            print('======================================================================================')
            break
        
def deletarTarefas():
    while True:
        caminho_arquivo = CAMINHO_ARQUIVO

        try:
            with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
                tarefas_json = arquivo.readlines()
                if not tarefas_json:
                    print('\nNenhuma tarefa foi encontrada para deletar.')
                    break
                
        except FileNotFoundError:
            print('\nNenhum arquivo de tarefas encontrado.')
            return
        
        tarefas_decodificadas = [json.loads(linha.strip()) for linha in tarefas_json]
        print('\nQual tarefa você deseja deletar?')
        for i, tarefa in enumerate(tarefas_decodificadas):
            print(f'{i + 1} - {tarefa}')

        while True:
            try:
                escolha_tarefa = int(input('Digite o número da tarefa que deseja deletar: '))
                if 1 <= escolha_tarefa <= len(tarefas_decodificadas):
                    break
                else:
                    print('OPS! Número inválido. Tente novamente.')

            except ValueError:
                print('OPS! Entrada inválida. Por favor, digite apenas o número.')

        indice_para_deletar = escolha_tarefa - 1
        tarefa_selecionada = tarefas_decodificadas[indice_para_deletar]

        confirmacao = input(f'Você tem certeza que deseja deletar a tarefa "{tarefa_selecionada}"? [S/N]: ').strip().upper()

        if confirmacao != 'S':
            print('\nOperação de deletar tarefa foi cancelada.')
            pass

        else:
            tarefas_json.pop(indice_para_deletar)

            try:
                with open(caminho_arquivo, 'w', encoding='utf-8') as arquivo:
                    arquivo.writelines(tarefas_json)
                print('\nTarefa deletada com sucesso!')

            except Exception as erro:
                print(f'ERRO ao deletar a tarefa: {erro}')

        resposta = validarSaida()
        if resposta == 'N':
            print('\nDeletar tarefas foi encerrado. Obrigado!')
            print('======================================================================================')
            break

def validarSaida():
    while True:
        resposta = input ('Deseja continuar? [S/N]: ').strip().upper()

        if resposta in 'SN':
            return resposta
        
        else:
            print('OPS! Opção inválida! Por favor, digite [S] para continuar ou [N] para sair.')


def encerrarPrograma():
    print('\nEncerrando o programa. Obrigado por usar o nosso sistema de Lista de Afazeres!')
    print('======================================================================================')
    exit()