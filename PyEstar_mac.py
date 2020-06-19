import time

from datetime import datetime

versao = "v0.1.6"

#region Setups dos sistema de login
listaNomes = ["admin"] #Define a lista de nomes
listaLogins = ["rootADM"] #Define a lista de Logins
listaSenhas = ["admpyestar"] #Define a lista de Senhas
#endregion

executando = 1

while executando == 1:
    abertura = (input("Seja bem vindo ao sistema PyEstar.\nDigite '1' caso você já tenha um login, caso contrário, digite '2' para fazer um cadastro: ")) #Abertura inicial do programa
    while(abertura != "1" and abertura != "2"):
        abertura = (input("Valor inválido. Seja bem vindo ao sistema PyEstar.\nDigite '1' caso você já tenha um login, caso contrário, digite '2' para fazer um cadastro: "))

    #region Processo de abertura:
    if abertura == "2": #Faz o cadastro do usuário
        print("==================================================================================================================")
        novoNome = input("\nPrimeiramente, insira seu nome: ") #Nome do Usuário
        listaNomes.append(novoNome) #Adiciona o nome na Lista de nomes
        
        novoUsuario = input("Insira um nome para login: ") #Novo login a ser cadastrado
        while listaLogins.count(novoUsuario) > 0: #Verifica se o nome de login já esta sendo usado
            novoUsuario = input("Já existe um usuário com este login, por favor, insira outro nome: ") #Novo login a ser cadastrado     
        listaLogins.append(novoUsuario) #Adiciona o login na Lista de longins
        
        novaSenha = input("Agora, insira uma senha: ") #Define uma nova senha
        listaSenhas.append(novaSenha) #Adiciona a senha a lista de senhas
        
        print("Cadastro realizado com sucesso") #Cadastro Finalizado
        
    print ("\n==================================================================================================================")
    login = input("\nInsira o seu nome de login: ") #Inicia o processo de login

    while listaLogins.count(login) == 0: #Verifica se o login existe na lista
        login = input("Login inválido, por favor insira um login válido: ") #Insere o login
        
    localLoginTemp = listaLogins.index(login) #Armazena a posição do login na lista
    senhaDoLogin = listaSenhas[localLoginTemp] #Encontra a senha localizada na mesma posição do Login informado
        
    senha = input("Insira a sua senha: ") #Pede que o usuário informe a senha

    while senha != senhaDoLogin: #Verifica se a senha informada é a correta
        senha = input("Senha incorreta, informe a senha novamente: ") #Pede que o usuário informe a senha
    #endregion

    usuarioLogado = 1 #Variável que define se o usuário está logado

    #region Setup dos dados do usuário logado
    nome = listaNomes[localLoginTemp] #Define o nome do usuário logado
    MarcaVeiculosCadastrados = [login] #Lista de Marcas dos veículos cadastrados de cada usuário
    ModeloVeiculosCadastrados = [login] #Lista de Modelos dos veículos cadastrados de cada usuário
    PlacaVeiculosCadastrados = [login] #Lista de Placas dos veículos cadastrados de cada usuário
    HistoricoDeUso = [login] #Histórico de uso do usuário
    dinheiro = 0 #Saldo em reais do usuário logado
    CarteiraUsuario = [login,dinheiro] #Lista do saldo do usuário
    #endregion
    while usuarioLogado == 1: #Enquanto o usuário estiver logado no sistema
        
        print("\n==================================================================================================================")
        acaoParaRealizar = (input("\nOlá " + str(nome) +", seja bem vindo ao PyEstar, qual ação você deseja realizar?:\n 1 - Cadastrar um veículo \n 2 - Estacionar um veículo cadastrado \n 3 - Comprar créditos \n 4 - Ver saldo \n 5 - Histórico \n 6 - Sobre \n 7 - Logout \n 8 - Sair \n Digite o número correspondente à ação que você deseja realizar: "))#Menu
        print("\n==================================================================================================================")

        while acaoParaRealizar != "0": #Enquanto alguma ação estiver sendo executada, não mudar para o menu
            if acaoParaRealizar == "1": #Cadastrar um veículo
                marcaTemp = input("\nInforme a marca do veículo que você deseja cadastrar: ")#Marca do veículo a ser cadastrado
                MarcaVeiculosCadastrados.append(marcaTemp) #Adiciona a marca desejada na última posição da lista 
                modeloTemp = input("Agora, informe o modelo do veículo: ") #Modelo do veículo a ser cadastrado
                ModeloVeiculosCadastrados.append(modeloTemp) #Adiciona o modelo desejado na última posição da lista
                placaTemp = input("E, por fim, informe a placa do veículo: ") #Placa do veículo a ser cadastrada
                while PlacaVeiculosCadastrados.count(placaTemp) > 0: #Verifica se a placa já existe na lista de placas
                    placaTemp = input("Essa placa já está cadastrada em outro veículo, por favor, insira outra placa: ") #Se verdadeiro, pedir uma nova placa
                PlacaVeiculosCadastrados.append(placaTemp) #Adiciona a placa desejada na última posição da lista
                print("Pronto, o veículo " + str(MarcaVeiculosCadastrados[len(MarcaVeiculosCadastrados)-1]) + " " + str(ModeloVeiculosCadastrados[len(ModeloVeiculosCadastrados)-1]) + " de placa: " + str(PlacaVeiculosCadastrados[len(PlacaVeiculosCadastrados)-1]) + " foi cadastrado com sucesso!")
                acaoParaRealizar = "0"#Volta para o menu
            elif acaoParaRealizar == "2": #Estacionar um veículo já cadastrado

                if dinheiro == 2: #Verifica se o usuário tem crédito o suficiente para estacionar apenas por 1 hora
                    print("\nVocê possui um total de R$2,00, portanto, você só poderá ficar estacionado durante, no máximo, 1(uma) hora.")
                elif dinheiro < 2: #Verifica se o usuário tem crédito o suficiente para estacionar
                    print("\nVocê não possui saldo o suficiente para utilizar o serviço, por favor, adicione créditos em sua carteira caso queira utilizá-lo.")
                    input("\nPressione 'ENTER' para voltar ao menu.")#Retorna para o menu inicial (1)
                    acaoParaRealizar = "0" 
                    break

                if len(PlacaVeiculosCadastrados) > 1: #Verifica se o usuário tem pelo menos um veículo cadastrado
                    print("\nVocê possui " + str(len(PlacaVeiculosCadastrados)-1) + " veículo(s) cadastrado(s): ") #Avisa quantos veículos estão cadastrados
                    for carros in range(len(PlacaVeiculosCadastrados)-1): #Mostra a lista de veículos cadastrados
                        print(str(carros+1) + " - " + str(MarcaVeiculosCadastrados[carros+1])+ " " + str(ModeloVeiculosCadastrados[carros+1]) + ". Placa: " + str(PlacaVeiculosCadastrados[carros+1]))
                    carroEstacionado = int(input("Digite o número do carro que você deseja estacionar: ")) #Variável para definir o carro à ser cadastrado

                    while carroEstacionado > (len(PlacaVeiculosCadastrados)-1) or carroEstacionado == 0: #Verifica se o número selecionado corresponde à um item da lista
                        carroEstacionado = int(input("Carro não encontrado. Digite o número do carro que você deseja estacionar: ")) #Variável para definir o carro à ser cadastrado

                    tempoEstacionado = int(input("\nSelecione o tempo que você deseja ficar estacionado: \n1 - Até 1 (uma) hora \n2 - Até 2 (duas) horas \nDigite o número correspondente ao tempo desejado: "))

                    while tempoEstacionado != 1 and tempoEstacionado !=2 :
                        tempoEstacionado = int(input("\n----------------\n|Ação inválida.|\n----------------\nSelecione o tempo que você deseja ficar estacionado: \n1 - Até 1 (uma) hora \n2 - Até 2 (duas) horas \nDigite o número correspondente ao tempo desejado: ")) 

                    if dinheiro <= 2: #Verifica se o saldo corresponde ao tempo desejado
                        while tempoEstacionado >= 2 or tempoEstacionado <= 0:
                            tempoEstacionado = int(input("\nVocê só possui saldo suficiente para ficar estacionado por uma hora. \nSelecione o tempo que você deseja ficar estacionado: \n1 - Até 1 (uma) hora \n2 - Até 2 (duas) horas\nDigite o número correspondente ao tempo desejado: "))

                    if tempoEstacionado == 1: #Determina o valor a ser descontado de acordo com o tempo estacionado
                        descontarValor = 2
                    elif tempoEstacionado == 2:
                        descontarValor = 4

                    dataHoraInicio = datetime.now() #Puxa do sistema a data e a hora
                    print("\n")
                    print(dataHoraInicio.strftime("%d/%m/%Y %H:%M")) #Escreve na tela a data e a hora inicial

                    HistoricoDeUso.append(str(dataHoraInicio.strftime("%d/%m/%Y %H:%M")) + " durante " + str(tempoEstacionado) + " horas com o veículo " + str(MarcaVeiculosCadastrados[carroEstacionado])+ " " + str(ModeloVeiculosCadastrados[carroEstacionado]) + ". Placa: " + str(PlacaVeiculosCadastrados[carroEstacionado])) #Adiciona no histórico o uso

                    dinheiro -= descontarValor  #Desconta o valor da carteira do usuário
                    CarteiraUsuario = [login,dinheiro]  #Atualiza o valor na carteira
                    print("\nMuito obrigado por utilizar o sistema PyEstar, você ficou estacionado durante " + str(tempoEstacionado) + " hora(s).\n" + "Foi debitado um total de R$" + str(descontarValor) + ",00 da sua conta. Volte sempre!")
                    carroEstacionado = 0
                    acaoParaRealizar = "0" #(1)

                else: #Caso não possua um veículo cadastrado vai até a tela de cadastro de veículo
                    print("\nVocê não possui veículos cadastrados no momento.")
                    acaoParaRealizar = "1"
            elif acaoParaRealizar == "3": #Comprar créditos
                print("\nVocê tem um total de : R$" + str(CarteiraUsuario[1]) + ",00 em sua carteira") #Escreve o valor que o usuário tem na carteira
                adicionarNaCarteira = int(input("Qual o valor que você deseja creditar em sua carteira?: \n1 - R$2,00 \n2 - R$4,00 \n3 - R$10,00 \n4 - R$20,00 \n5 - R$50,00 \nDigite o número correspondente ao valor que você deseja creditar: "))
                if adicionarNaCarteira == 1: #Adicionar 2 reais na carteira
                    dinheiro += 2
                elif adicionarNaCarteira == 2: #Adicionar 4 reais na carteira
                    dinheiro += 4
                elif adicionarNaCarteira == 3: #Adicionar 10 reais na carteira
                    dinheiro += 10
                elif adicionarNaCarteira == 4: #Adicionar 20 reais na carteira
                    dinheiro += 20
                elif adicionarNaCarteira == 5: #Adicionar 50 reais na carteira
                    dinheiro += 50
                
                CarteiraUsuario = [login,dinheiro] #Atualiza a carteira do usuário
                print("Pronto, seu saldo agora é de: R$" + str(dinheiro) + ",00.") #Mostra o saldo total
                input("\nPressione 'ENTER' para voltar ao menu.") #(1)
                acaoParaRealizar = "0"        
            elif acaoParaRealizar == "4": #Ver saldo
                print("\nVocê tem um total de : R$" + str(CarteiraUsuario[1]) + ",00.") #Mostra o saldo do usuário
                input("\nPressione 'ENTER' para voltar ao menu.") #(1)
                acaoParaRealizar = "0"
            elif acaoParaRealizar == "5": #Histórico
                if len(HistoricoDeUso) > 1: #Verifica se o usuário já possui um histórico
                    for contador in range(len(HistoricoDeUso)-1,0,-1): #Cria uma lista referente ao histórico
                        print("\n" + str(contador) + " - " + HistoricoDeUso[contador])
                else:
                    print("\nVocê ainda não utilizou nosso serviço.")
                input("\nPressione 'ENTER' para voltar ao menu.") #(1)
                acaoParaRealizar = "0"
            elif acaoParaRealizar == "6": #Informações sobre o PyEstar
                print("\nO PyEstar é um programa de estacionamento em determinadas áreas públicas da cidade. \nO limite de tempo máximo estacionado em um local é de 2 (duas) horas, e cada hora custa um total R$2,00. \nO sistema não possui tolerância, ou seja, a partir do momento que se inicia a contagem do estacionamento, \nimediatamente a primeira hora passa a contar e um valor de 2 (dois) reais serão descontados de sua conta,\n e, depois de 1 hora estacionado, a segunda hora começa a contar, e passarão a ser decontados um total de 4 reais.\n\nO PyEstar está em sua versão beta " + str(versao) + "\nDesenvolvedores: Bryan Yassunori Tanaka e Leonardo Mafra Salin.")
                input("\nPressione 'ENTER' para voltar ao menu.") #(1)
                acaoParaRealizar = "0"
            elif acaoParaRealizar == "7": #Deslogar
                print("\n\n\nDeslogando...\n\n\n\n==================================================================================================================")
                acaoParaRealizar = 0
                usuarioLogado = 0
            elif acaoParaRealizar == "8": #Fechar o programa
                print("Finalizando...")
                executando = 0
                exit()
            else:
                acaoParaRealizar = "0"