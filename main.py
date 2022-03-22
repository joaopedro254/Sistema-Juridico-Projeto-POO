from Processo import Processo
from Audiencias import Audiencia
from Pessoa import Pessoa
from Custo import Custo
from Advogado import Advogado

if __name__ == '__main__':

    #CRIAÇÃO DOS OBJETOS
    #Listas de audiências
    listaDeAudienciasJoao1 = []
    listaDeAudienciasJoao2 = []

    listaDeAudienciasPedro1 = []
    listaDeAudienciasPedro2 = []
    listaDeAudienciasPedro3 = []

    listaDeAudienciasCarlos = []

    # Listas de processos
    listaDeProcessosJoao = []
    listaDeProcessosPedro = []
    listaDeProcessosCarlos = []

    listaDeProcessosBrunoADV = []
    listaDeProcessosAntonioADV = []

    #Criação dos objetos Pessoa
    joao = Pessoa('123.456.789-10', 'João Silva', listaDeProcessosJoao)
    pedro = Pessoa('452.265.887-91', 'Pedro Oliveira', listaDeProcessosPedro)
    carlos = Pessoa('652.178.901-28', 'Carlos Henrique', listaDeProcessosCarlos)
    pessoas = [joao, pedro, carlos]

    #Criação dos objetos Advogado
    brunoADV = Advogado('8723872', 'Bruno Henrique Vasconcelos', listaDeProcessosBrunoADV)
    antonioADV = Advogado('9320123', 'Antônio Carlos Fernandes', listaDeProcessosAntonioADV)
    advogados = [brunoADV, antonioADV]

    #Criação dos objetos Processo
    processoJoao1 = Processo('#938492', Custo('15/03/2021', 'Referente ao processo #938492', 1250), True, 'Deferido', joao, brunoADV, listaDeAudienciasJoao1)
    listaDeAudienciasJoao1.append(Audiencia('28/04/2021', 'Recomendação 1', 45))
    listaDeAudienciasJoao1.append(Audiencia('30/05/2021', 'Recomendação 2', 120))
    processoJoao2 = Processo('#123542', Custo('16/02/2021', 'Referente ao processo #123542', 2502.24), False, 'Indeferido', joao, antonioADV, listaDeAudienciasJoao2)
    listaDeAudienciasJoao2.append(Audiencia('28/02/2021', 'Recomendação 3', 30))

    processoPedro1 = Processo('#869453', Custo('27/02/2020', 'Referente ao processo #869453', 3050), True, 'Deferido', pedro, brunoADV, listaDeAudienciasPedro1)
    listaDeAudienciasPedro1.append(Audiencia('15/02/2020', 'Recomendação 4', 90))
    listaDeAudienciasPedro1.append(Audiencia('23/02/2020', 'Recomendação 5', 200))
    processoPedro2 = Processo('#923783', Custo('31/05/2020', 'Referente ao processo #923783', 3050), True, 'Deferido', pedro, brunoADV, listaDeAudienciasPedro2)
    listaDeAudienciasPedro2.append(Audiencia('05/06/2020', 'Recomendação 6', 110))
    processoPedro3 = Processo('#735987', Custo('28/08/2020', 'Referente ao processo #735987', 2030), False, 'indeferido', pedro, antonioADV, listaDeAudienciasPedro3)
    listaDeAudienciasPedro3.append(Audiencia('30/08/2020', 'Recomendação 7', 65))
    listaDeAudienciasPedro3.append(Audiencia('05/09/2020', 'Recomendação 8', 90))

    processoCarlos = Processo('#849584', Custo('16/11/2019', 'Referente ao processo #849584', 1930.43), True, 'Deferido', carlos, brunoADV, listaDeAudienciasCarlos)
    listaDeAudienciasCarlos.append(Audiencia('10/12/2019', 'Recomendação 9', 240))

    #Atribuindo processos a Pessoas e Advogados
    listaDeProcessosJoao.append(processoJoao1)
    listaDeProcessosJoao.append(processoJoao2)

    listaDeProcessosPedro.append(processoPedro1)
    listaDeProcessosPedro.append(processoPedro2)
    listaDeProcessosPedro.append(processoPedro3)

    listaDeProcessosCarlos.append(processoCarlos)

    listaDeProcessosBrunoADV.append(processoJoao1)
    listaDeProcessosBrunoADV.append(processoPedro1)
    listaDeProcessosBrunoADV.append(processoPedro2)
    listaDeProcessosBrunoADV.append(processoCarlos)

    listaDeProcessosAntonioADV.append(processoJoao2)
    listaDeProcessosAntonioADV.append(processoPedro3)
    #FIM DA CRIAÇÃO DOS OBJETOS


    while True:
        print('------------- MENU -----------------')
        print('1 - Digite 1 para verificar todas as audiências de um processo com tempo maior ou igual ao informado.')
        print('2 - Digite 2 para verificar a quantidade de decisões deferidas e indeferidas dos processos de uma pessoa.')
        print('3 - Digite 3 para verificar os custos dos processos de uma pessoa.')
        print('4 - Digite 4 para verificar os custos dos processos de uma pessoa com um único advogado.')
        print('5 - Digite 5 para verificar todos os clientes de um advogado.')
        print('6 - Digite 6 para verificar quantos processos defendidos por um advogado foram deferidos ou indeferidas.')
        print('7 - Digite 7 para verificar os ganhos de um advogado em todos os seus processos')
        print('8 - Digite 8 para finalizar o programa.')
        print('------------------------------------')

        escolha = int(input('Digito: '))
        print('')

        if escolha == 1:
            print('Clientes:')
            for i in range(len(pessoas)):
                print(f'{i+1} - {pessoas[i].nome}')

            testePessoa = int(input('\nEscolha um cliente: '))

            print('\nProcessos:')
            for i in range((len(pessoas[testePessoa-1].processos))):
                print(f'{i+1} - {pessoas[testePessoa-1].processos[i].descricao}')

            testeProcesso = int(input('\nEscolha um processo: '))
            temp = int(input('\nDigite a duração das audiências que deseja buscar:\n'))

            print('\nAudiências:')
            pessoas[testePessoa-1].processos[testeProcesso-1].audiencias_temp(temp)

        elif escolha == 2:
            print('Clientes:')
            for i in range(len(pessoas)):
                print(f'{i+1} - {pessoas[i].nome}')

            testePessoa = int(input('\nEscolha um cliente: '))

            teste = int(input('\nVerificar quantidade de processos deferidos ou indeferidos[1-2]: '))
            if teste == 1:
                print(pessoas[testePessoa-1].num_decisoes(True))
            elif teste == 2:
                print(pessoas[testePessoa-1].num_decisoes(False))

        elif escolha == 3:
            print('Clientes:')
            for i in range(len(pessoas)):
                print(f'{i+1} - {pessoas[i].nome}')

            testePessoa = int(input('\nEscolha um cliente: '))

            print(f'\nCusto total dos processos de {pessoas[testePessoa-1].nome}: R$ {pessoas[testePessoa-1].custo_total():.2f}\n')

        elif escolha == 4:
            print('Clientes:')
            for i in range(len(pessoas)):
                print(f'{i+1} - {pessoas[i].nome}')

            testePessoa = int(input('\nEscolha um cliente: '))
            
            for i in range(len(advogados)):
                print(f'{i+1} - {advogados[i].cod_oab} - {advogados[i].nome}')
            codOAB = input('\nDigite o Código da OAB do advogado que quer buscar custos: ')
            print(f'\nCusto total dos processos de {pessoas[testePessoa-1].nome} realizados pelo advogado de Código {codOAB}: R$ {pessoas[testePessoa-1].custo_total_adv(codOAB):.2f}\n')
        elif escolha == 5:
            for i in range(len(advogados)):
                print(f'{i+1} - {advogados[i].cod_oab} - {advogados[i].nome}')


            testeAdvogado = int(input('\nEscolha um advogado[ID]: '))
            print(f'\nClientes de {advogados[testeAdvogado-1].nome}:')
            print(advogados[testeAdvogado-1].lista_clientes())

        
        elif escolha == 6:      
            print('Advogados:')
            for i in range(len(advogados)):
                print(f'{i+1} - {advogados[i].nome}')

            testeAdvogado = int(input('\nEscolha um Advogado pelo indice: '))

            teste = int(input(f'\nVerificar quantidade de processos deferidos ou indeferidos defendidos por {advogados[testeAdvogado-1].nome}[1-2]: '))
            if teste == 1:
                print(advogados[testeAdvogado-1].processos_deferidos(True))
            elif teste == 2:
                print(advogados[testeAdvogado-1].processos_deferidos(False))
        
        elif escolha == 7:
            print('Advogados:')
            for i in range(len(advogados)):
                print(f'{i+1} - {advogados[i].nome}')

            testeAdvogado = int(input('\nEscolha um Advogado pelo indice: '))
            print(f'\nR$ {advogados[testeAdvogado-1].valor_ganho_ADV():.2f} ganho em todos os seus processos defendidos.\n')

        elif escolha == 8:
            print('Programa Finalizado!\n')
            break
        else:
            print('Valor inexistente.\n')
