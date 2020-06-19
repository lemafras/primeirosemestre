#region Setups Gerais
import random #Biblioteca de randomização
import time #Biblioteca de tempo

from datetime import date
from datetime import datetime

versao = "0.0.5" #Versão atual do app
abertura = "" #Variável da mensagem de abertura
usuarioLogado = 0 #Variável para verificar se o usuário esta logado
listaInformacoesVacina = [ #Lista de informações das vacinas cadastradas no app
    "\n 1 - BCG (Bacilo Calmette-Guerin) – (previne as formas graves de tuberculose, principalmente miliar e meníngea)",
    "\n 2 - Penta – (previne difteria, tétano, coqueluche, hepatite B e infecções causadas pelo Haemophilus influenzae B)",
    "\n 3 - Rotavírus humano – (previne diarreia por rotavírus)",
    "\n 4 - Meningocócica C (conjugada) – (previne Doença invasiva causada pela Neisseria meningitidis do sorogrupo C)",
    "\n 5 - Febre Amarela – (previne a febre amarela)",
    "\n 6 - Tríplice viral – (previne sarampo, caxumba e rubéola)",
    "\n 7 - DTP – (previne a difteria, tétano e coqueluche)",
    "\n 8 - Hepatite B – (previne a hepatite B)",
    "\n 9 - Pneumocócica 23 Valente – (previne pneumonia, otite, meningite e outras doenças causadas pelo Pneumococo)"]

listaLogin = ["00000000000"] #Lista de CPF's cadastrados no App
listaSenha = ["admpyvacina"] #Lista de senhas dos usuários

listaNome = ["admin"] #Lista de nomes dos usuários
listaNascimento = ["01092000"] #Lista de datas de nascimento dos usuários
listaFaixaEtaria = ["Adolescente"] #Lista de faixa etária dos usuários
listaLocalidade = ["Curitiba"] ##Lista de cidades dos usuários

#listaVacinas = ["BCG",""]
#Lista de vacinas de acordo com a faixa etária {
listaVacinasCrianca = ["BCG","Penta","Rotavírus Humano","Meningocócica C","Febre Amarela","Tríplice Viral","DTP","Hepatite B"] 
listaVacinasAdolescente = ["Meningocócica C","Febre Amarela","Tríplice Viral","Pneucócica 23","Hepatite B"]
listaVacinasAdulto = ["Febre Amarela","Tríplice Viral","Pneucócica 23","Hepatite B"]
listaVacinasIdoso = ["Febre Amarela","Tríplice Viral","Pneucócica 23","Hepatite B"]
#}


listaRepeticaoVacina = [] #Lista que determina as repetições de cada vacina do usuário
listaVacinasTomadas = [] #Lista que armazena as vacinas aplicadas no usuário
listaVacinasAgendadas = [] #Lista que armazena as vacinas agendadas do usuário
#endregion

def pularLinhas(): #Função estética
    print("\n............................................................................................................\n")
def cadastrarLogin(): #Função para cadastro de novo usuário

    pularLinhas()

    cpfTemp = input("Primeiramente insira o seu CPF como forma de login (somente caracteres numéricos ex: 00000000000): ") #CPF para cadastro

    while(len(cpfTemp) != 11): #CPF para cadastro caso inválido
       cpfTemp = input("CPF inválido. O CPF deve conter 11 caracteres numéricos. Insira novamente: ")

    while listaLogin.count(cpfTemp) > 0: #CPF para cadastro caso já cadastrado
        cpfTemp = input("Esse CPF já foi cadastrado, insira novamente: ")
        while(len(cpfTemp) != 11): #CPF para cadastro caso inválido
            cpfTemp = input("CPF inválido. O CPF deve conter 11 caracteres numéricos. Insira novamente: ")
    
    listaLogin.append(cpfTemp) #Adiciona o CPF na lista de logins
    print("\n\nCPF cadastrado com sucesso!\n\n") #Mensagem de confirmação
    
    senhaTemp = input("Agora insira uma senha: ") #Senha para cadastro
    listaSenha.append(senhaTemp) #Adiciona a senha na lista de senhas

    print("\nLogin e senha cadastrados com sucesso!") #Mensagem de confirmação
    pularLinhas()

    nomeTemp = input("Insira o seu nome: ") #Nome do usuário
    listaNome.append(nomeTemp) #Adiciona o nome na lista de nomes

    nascimentoTemp = input("Insira sua data de nascimento. (Somente números) Ex: 01092000 (1º de setembro de 2000): ") #Data de nascimento do usuário
    while len(nascimentoTemp) != 8: #Data de nascimento do usuário caso inválida
        nascimentoTemp = input("Data inválida. Insira novamente. (Somente números) Ex: 01092000 (1º de setembro de 2000): ")
    listaNascimento.append(nascimentoTemp) #Adiciona a data de nascimento na lista de nascimentos

    diaCadastro = datetime.now() #Verifica a data do sistema pela biblioteca date
    anoCadastro = int(diaCadastro.year) #Armazena o ano do cadastro do sistema pela biblioteca date
    anoTemp = int(nascimentoTemp[4:]) #Armazena apenas o ano de nascimento do usuário

    idadeTemp = anoCadastro-anoTemp #Determina a idade do usuário apenas pelo ano

    if idadeTemp < 10: #Se idade menor que 10 determina a faixa etária como criança
        listaFaixaEtaria.append("Criança")
    elif idadeTemp < 20: #Se idade menor que 20 e maior que 10 determina a faixa etária como adolescente
        listaFaixaEtaria.append("Adolescente")
    elif idadeTemp < 60:#Se idade menor que 60 e maior que 20 determina a faixa etária como adulto
        listaFaixaEtaria.append("Adulto")
    else: #Se idade maior que 60 determina a faixa etária como idoso
        listaFaixaEtaria.append("Idoso")

    listaLocalidade.append(input("Informe qual é a sua cidade: ")) #Determina a cidade do usuário

    print("Cadastro realizado com sucesso!") #Mensagem de confirmação

    pularLinhas()
def logar(): #Função para login do usuário
    login = input("Insira o seu CPF: ") #Pede o login (CPF) para o usuário
    while(listaLogin.count(login)) == 0: #Verifica se o login é existente na lista
        login = input("CPF inválido, insira um CPF cadastrado: ")

    localLoginTemp = listaLogin.index(login) #Determina o local onde o login se encontra na lista
    senhaDoLogin = listaSenha[localLoginTemp] #Determina a senha correspondente do login
    
    senha = input("Insira a sua senha: ") #Pede a senha do login
    while(senha != senhaDoLogin): #Verifica se a senha é correspondente ao login
        senha = input("Senha incorreta, insira novamente:") 

    nome = listaNome[localLoginTemp] #Armazena o nome do usuário logado
    print("Login realizado com sucesso!") #Mensagem de confirmação
    return localLoginTemp #Retorna o id (local na lista) do usuário logado
def setarVacina(faixaEtaria): #Retorna as repeticões (doses) das vacinas de acordo com cada faixa etária
    if faixaEtaria == "Criança":
        return [1,3,2,3,1,1,2,1]
    elif faixaEtaria == "Adolescente":
        return [1,1,2,1,3]
    elif faixaEtaria == "Adulto":
        return [1,1,1,3]
    elif faixaEtaria == "Idoso":
        return [1,1,1,3]
def acaoMenu(acaoParaRealizar):
    if acaoParaRealizar == "1": #Agendar Vacina
        listaUsada = listarVacina() #Função para listar as vacinas do usuário

        agendarTemp = int(input("\n Por favor, selecione o número correspondente à vacina que você deseja agendar: "))-1 #Determina a vacina que será agendada

        while listaRepeticaoVacina[agendarTemp] == 0: #Caso a repetição da vacina escolhida seja = 0
            agendarTemp = int(input("Você já tomou todas as doses desta vacina. Por favor, selecione o número correspondente à vacina que você deseja agendar: "))-1

        if listaRepeticaoVacina[agendarTemp] > 0: #Se ainda tiver aplicações da vacina pendentes
            disponibilidade = random.randrange(3, 25) #Determina aleatóriamente uma data disponível para aplicação dos postos de saúde (através da biblioteca random)
            agendarDia = int(input("\nOs postos de saúde terão disponibilidade para aplicação desta vacina em " + str(disponibilidade) + " dias. \nDaqui a quantos dias você deseja agendar a aplicação da mesma? (O número deve ser maior ou igual a data de disponibilidade e menor que 1 ano): ")) #Pede o dia desejado para aplicação
            
            while (agendarDia < disponibilidade or agendarDia > 365): #Verifica se a data está disponível e está dentro do limite de um ano
                agendarDia = int(input("\nA data precisa ser maior ou igual à disponibilidade e estar dentro do período de um ano. \nOs postos de saúde terão disponibilidade para aplicação desta vacina em " + str(disponibilidade) + " dias. \nDaqui a quantos dias você deseja agendar a aplicação da mesma? (O número deve ser maior ou igual a data de disponibilidade e menor que 1 ano): "))

            numeroDiaAtualtemp = diaAtual.toordinal() #Variável que armazena o dia atual em ordinal. (Através da biblioteca date)
            diaAgendado = agendarDia + numeroDiaAtualtemp #Calcula o dia para aplicação (ordinal)
            diaAgendado = date.fromordinal(diaAgendado) #Determina o dia de aplicação (não ordinal)
            
            diaAgendado.strftime("%d/%m/%Y") #Transforma em string a data de aplicação (No formato Dia/Mês/Ano)

            listaVacinasAgendadas.append("Vacina : " + str(listaUsada[agendarTemp]) + " Dia: " + str(diaAgendado)) #Adiciona a vacina e a data agendada na lista de agendamentos

            repeticaoTemp = listaRepeticaoVacina[agendarTemp]  #Armazena a(s) dose(s) da vacina escolhida
            repeticaoTemp -= 1 #Diminui uma dose da vacina escolhida
            listaRepeticaoVacina.pop(agendarTemp) #Retira a dose da lista (por posição) 
            listaRepeticaoVacina.insert(agendarTemp, repeticaoTemp) #Adiciona a dose ajustada na lista (na mesma posição)

            input("A vacina " + str(listaUsada[agendarTemp]) + " está agendada para o dia " + str(diaAgendado) + ". Pressione ENTER para retornar ao menu.") #Mensagem de confirmação e retorno ao menu
    elif acaoParaRealizar == "2": #Vacinas Agendadas
        for i in listaVacinasAgendadas: #Printa as vacinas agendadas de acordo com a lista
            print(i)

        input("Pressione ENTER para voltar ao menu: ") #Retornar ao menu
        acaoParaRealizar = "0"
    elif acaoParaRealizar == "3": #Histórico de vacinação
        for i in listaVacinasTomadas: #Printa as vacinas já aplicadas de acordo com a lista
            print (i)
        input("Pressione ENTER para retornar ao menu.") #Retornar ao menu
    elif acaoParaRealizar == "4": #Aplicação de vacina não agendada
        listaUsada = listarVacina() #Printa as vacinas do usuário
        vacinaAplicada = int(input("Informe o número correspondente a vacina aplicada: "))-1 #Pede o número correspondente a vacina aplicada

        while listaRepeticaoVacina[vacinaAplicada] <= 0: #Verifica se a vacina já não estava aplicada anteriormente ou se existe um agendamento prévio
            vacinaAplicada = int(input("Esta vacina já foi aplicada, ou existe um agendamento pendente. Informe o número correspondente a vacina aplicada: "))-1
        
        diaTomado = int(input("Há quantos dias a vacina foi aplicada? : ")) #Pede a data de aplicação da vacina

        while diaTomado < 0: #Verifica se a aplicação foi retroativa
            diaTomado = int(input("(Insira um número maior ou igual à zero.) Há quantos dias a vacina foi aplicada? : "))

        numeroDiaAtualtemp = diaAtual.toordinal() #Armazena a data atual do sistema 
        diaTomado = numeroDiaAtualtemp - diaTomado #Calcula o dia de aplicação
        diaTomado = date.fromordinal(diaTomado) #Transforma o dia de aplicação em não ordinal
        
        repeticaoTemp = listaRepeticaoVacina[vacinaAplicada] #Armazena a(s) dose(s) da vacina escolhida
        repeticaoTemp -= 1 #Diminui uma dose da vacina aplicada
        listaRepeticaoVacina.pop(vacinaAplicada) #Retira a dose da lista (por posição) 
        listaRepeticaoVacina.insert(vacinaAplicada, repeticaoTemp)#Adiciona a dose ajustada na lista (na mesma posição)

        diaTomado.strftime("%d/%m/%Y") #Transforma a data de aplicação em string

        listaVacinasTomadas.append("Vacina : " + str(listaUsada[vacinaAplicada]) + " Dia: " + str(diaTomado)) #Adiciona a data de aplicação na lista de vacinas tomadas
    elif acaoParaRealizar == "5": #Informações sobre as vacinas
        print("Informações sobre as vacinas fornecidas pelo Ministério da Saúde: ")
        for i in listaInformacoesVacina: #Printa as informações sobre as vacinas listadas
            print (i)

        input("\n Pressione ENTER para voltar ao menu.") #Retornar ao menu
    elif acaoParaRealizar == "6": #Perfil do usuário

        dataTemp = listaNascimento[identificadorDoUsuario] #Armazena a data de nascimento do usuário
        diaTemp = dataTemp[0:2] #Armazena o dia de nascimento
        mesTemp = dataTemp[2:4] #Armazena o mês de nascimento
        anoTemp = dataTemp[4:9] #Armazena o ano de nascimento
        dataEscrita = str(diaTemp) + "/" + str(mesTemp) + "/" + str(anoTemp) #Adiciona os caracteres especiais relacionados a data de nascimento

        print("\nNome do Usuário: ", nome, ".\nCPF: ", listaLogin[identificadorDoUsuario], "\nData de nascimento: ", dataEscrita,"\nCidade: ", listaLocalidade[identificadorDoUsuario]) #Lista os dados do usuário
        input("\nPressione 'ENTER' para voltar ao menu.") #Retornar ao menu
    elif acaoParaRealizar == "7": #Informações sobre o PyVacina
        print("\nO ditado popular “melhor prevenir do que remediar” se aplica perfeitamente à vacinação. Muitas doenças comuns \nno Brasil e no mundo deixaram de ser um problema de saúde pública por causa da vacinação massiva da população.\nPoliomielite, sarampo, rubéola, tétano e coqueluche são só alguns exemplos de doenças comuns no passado e que \nas novas gerações só ouvem falar em histórias. O resultado da vacinação não se resume a evitar doença. \nVacinas salvam vidas.")
        print("\nO PyVacina é um aplicativo que auxilia no monitoramento de suas vacinas. \nNele é possível ver as suas vacinas aplicadas e agendar novas aplicações. \nO PyVacina está em sua versão beta " + str(versao) + "\nDesenvolvedores: Bryan Yassunori Tanaka e Leonardo Mafra Salin.")
        input("\nPressione 'ENTER' para voltar ao menu.") #(1)
        acaoParaRealizar = "0"
    elif acaoParaRealizar == "8": #Deslogar
        print("\n\n\nDeslogando...\n\n\n\n==================================================================================================================")
        acaoParaRealizar = 0
        return 0
    elif acaoParaRealizar == "9": #Fechar o programa
        print("Finalizando...")
        acaoParaRealizar = 0
    else:
        acaoParaRealizar = "0"
def listarVacina(): #Função que printa na tela as vacinas respectivas de cada usuário.
    identificadorVacina = 1 #Varíavel para ordenar as vacinas
    if listaFaixaEtaria[identificadorDoUsuario] == "Criança": #Verifica se faixa etária == criança
        for i in listaVacinasCrianca:
            print ("\n",identificadorVacina, " - Vacina: ",i, "\n Doses restantes: ",listaRepeticaoVacina[(listaVacinasCrianca.index(i))]) #Printa o nome das vacinas e as doses restantes
            identificadorVacina += 1
            listaUsada = listaVacinasCrianca
    elif listaFaixaEtaria[identificadorDoUsuario] == "Adolescente": #Verifica se faixa etária == adolescente
        for i in listaVacinasAdolescente:
            print ("\n",identificadorVacina," - Vacina: ",i, "\n Doses restantes: ",listaRepeticaoVacina[(listaVacinasAdolescente.index(i))]) #Printa o nome das vacinas e as doses restantes
            identificadorVacina += 1
            listaUsada = listaVacinasAdolescente
    elif listaFaixaEtaria[identificadorDoUsuario] == "Adulto": #Verifica se faixa etária == adulto
        for i in listaVacinasAdulto:
            print ("\n",identificadorVacina," - Vacina: ",i, "\n Doses restantes: ",listaRepeticaoVacina[(listaVacinasAdulto.index(i))]) #Printa o nome das vacinas e as doses restantes
            identificadorVacina += 1
            listaUsada = listaVacinasAdulto
    elif listaFaixaEtaria[identificadorDoUsuario] == "Idoso": #Verifica se faixa etária == idoso
        for i in listaVacinasIdoso:
            print ("\n",identificadorVacina," - Vacina: ",i, "\n Doses restantes: ",listaRepeticaoVacina[(listaVacinasIdoso.index(i))]) #Printa o nome das vacinas e as doses restantes
            identificadorVacina += 1
            listaUsada = listaVacinasIdoso

    return listaUsada #Retorna a lista usada pela função

executando = 1 #Inicio do programa

while executando == 1: #Enquanto o programa estiver executando
    while usuarioLogado == 0: #Enquanto usuário não logado
        if abertura == "1": #Caso o usuário selecione a opção login
            identificadorDoUsuario = logar() #Chama a função de login e armazena a id do usuário
            abertura = 0 #Determina a opção de abertura como 0
            usuarioLogado = 1 #Determina o usuário como logado
            nome = listaNome[identificadorDoUsuario] #Determina o nome correspondente ao usuário
            listaRepeticaoVacina = [] #Limpa a lista de repetição das vacinas
            listaVacinasTomadas = [] #Limpa a lista de vacinas tomadas
            listaVacinasAgendadas = [] #Limpa a lista de vacinas agendadas
            listaRepeticaoVacina = setarVacina(listaFaixaEtaria[identificadorDoUsuario]) #Determina a repetição das vacinas do usuário
            diaAtual = date.today() #Armazena o dia atual do sistema através da biblioteca date
        elif abertura == "2": #Caso o usuário selecione a opção cadastro
            cadastrarLogin() #Função para cadastro
            abertura = 0 #Determina a opção de abertura como 0
        else:
            abertura = input("Seja bem vindo ao sistema PyVacina.\nDigite '1' caso você já tenha um login, caso contrário, digite '2' para fazer um cadastro: ") #Abertura inicial do programa
    
    pularLinhas() 
    if usuarioLogado != 0: #Se o usuário não deslogou
        opcaoEscolhida = (input("\nOlá " + str(nome) +", seja bem vindo ao PyVacina, qual ação você deseja realizar?:\n 1 - Agendar vacinas \n 2 - Vacinas Agendadas \n 3 - Histórico de Vacinação \n 4 - Informar aplicação de Vacina não agendada \n 5 - Informações sobre as vacinas \n 6 - Meu perfil \n 7 - Sobre \n 8 - Logout \n 9 - Fechar \n Digite o número correspondente à ação que você deseja realizar: "))#Menu 
        pularLinhas()
        if opcaoEscolhida == "9" : #Caso a opção seja == 9 (Fechar o programa)
            executando = 0 #Fim do programa
        usuarioLogado = acaoMenu(opcaoEscolhida) #Caso a opção seja == 9 (fechar o programa) ou 8 (deslogar) determina usuário logado = 0

exit() #Fechar o programa

