import os
#limpeza do terminal

with open("introducaoEuropa.txt", "r", encoding = "utf-8") as arquivo:
    introducaoEuropa = arquivo.read()
    
    print(introducaoEuropa)

           #abrir arquivo de introdução "Europa", conta a história. 
           
def general_ougar():  
    with open("ougar.txt", "r", encoding = "utf-8") as arquivo:
        ougar = arquivo.read()
    
        print(ougar)
        #mostra imagem alienígena(General Ougar) quando perde.
        
def msg_vitoria():  
    with open("vencedor.txt", "r", encoding = "utf-8") as arquivo:
        vencedor = arquivo.read()
        quebra_linha()
        print(vencedor)
        #mensagem de vitoria
        quebra_linha()
                              
def quebra_linha():
    print('-=' * 42)

def nova_tentativa():
    os.system("cls or clear") #limpeza do terminal    
    print("Voltar ao jogo?")   
    nova_tentativa = int(input("[ 1 ] Sim [ 2 ] Não\n"))
    if  nova_tentativa == 1:
        
        selecao_jogador()
    else:
        print("Fica para uma próxima então!!!")
        exit()

def selecao_jogador():
    quebra_linha()
    print(("==-" * 12) + "MISSÃO" + ("-==" * 12))
    with open("titulo.txt", "r", encoding = "utf-8") as arquivo:
        titulo = arquivo.read()
        print(titulo)
    quebra_linha()
    print("Agora é com você...\n")
    print("O tempo não está ajudando...\n")
    print("Estamos em uma viagem pelo universo...\n")    
    print("Antes vc tem uma missão...\n")
    quebra_linha()
    print("Escolha um jogador:\n")
    quebra_linha()
    jogador = int(input("[ 1 ] MADRE  [ 2 ] MARFÃO  [ 3 ] SUCA \n"))
    quebra_linha()
    
    if jogador == 1:
        with open("madre.txt", "r", encoding = "utf-8") as arquivo:
            madre = arquivo.read() #le arquivo txt com imagem ascii 
            print(madre) #mostra imagem
            quebra_linha()
            print("Madre , 34 anos, natural de Uberlandia/MG, pscicóloga militar(NASA) com poderes\nde telecinese.\n")
            quebra_linha()
        #definição jogador 01
    elif jogador == 2:
        with open("marfao.txt", "r", encoding = "utf-8") as arquivo:
            marfao = arquivo.read()
            print(marfao)
        quebra_linha()
        print("Marfão, alienígena(idade não definida), Zotax(refugiado), biólogo/geneticista com\npoderes de teletransporte.\n")
        quebra_linha()
        #definição jogador 02
    elif jogador == 3:
        with open("suca.txt", "r", encoding = "utf-8") as arquivo:
            suca = arquivo.read()
            print(suca)
        quebra_linha()
        print("Suca, 45 anos, natural de Berlim/Alemanha, piloto/navegador experiência em combate,\nhabilidade com armas.\n")
        quebra_linha()
        #definição jogador 03
    else:
        print("*** Escolha inválida ***\nEscolha [ 1 ] [ 2 ] ou [ 3 ]")
        selecao_jogador()
        #retornar ao inicio do jogo.
    
    print("Confirma escolha ou trocar? ")  
    confirma_escolha = int(input("[ 1 ] Confirma [ 2 ] Troca\n"))
    if  confirma_escolha == 1:
        quebra_linha()
        
    elif confirma_escolha == 2:
        quebra_linha()
        nova_tentativa()
    else:
        print("valor innválido!")
        nova_tentativa()
        
    #confirma a escolha do jogador               
    
    while (jogador == 1):

        if  jogador == 1:
            print("Estamos a caminho da 'Europa' e uma nave de guerra inimiga se aproxima!!!\n")
            quebra_linha()
        
        
        fase_01 = int(input("[ 1 ] Você ataca a nave enviando asteroides com seu poder de telecinese.\n[ 2 ] Você se esconde no banheiro.\n"))
         

        if fase_01 == 1:
            quebra_linha()
            print("Você passou!!!\n")
            print("Chegamos sãos e salvos a europa graças ao ataque bem sucedido \nmas os alienigenas ja sabem de nossa presença.\n")
            quebra_linha()
            
            
        else:
            quebra_linha()
            print("Fugir  ou se esconder nunca foi uma escolha!!!")
            general_ougar()
            nova_tentativa()
            # volta ao inicio do jogo
        fase_02 = int(input("[ 1 ] Você destroi todos q se aproximam provocando uma tempestade de poeira espacial.\n[ 2 ] Você tenta conversar com os alienígenas, oferece sorvete e balas.\n"))
                    
        if fase_02 == 1:
            quebra_linha()
            print("Você é incrível, mas ainda não acabou!")
            print("Tivemos algumas baixas, acontece!! Missao está difícil mas estamos de fora da base.\n Precisamos entrar.\n")
            quebra_linha()
            
        
        else:
            quebra_linha()
            print("Tá de brincadeira, vidas em jogo e faz isso?!")
            general_ougar()
            quebra_linha()
            nova_tentativa()
            # volta ao inicio do jogo
        fase_03 = int(input("[ 1 ] Você arranca a porta com toda fúria e resgata nossos amigos.\n[ 2 ] Você aperta a campainha e espera.\n"))

        if fase_03 == 1:
            quebra_linha()
            msg_vitoria()
            quebra_linha()
            print("SUCESSO na missão, voltamos para 'Esquadra Estelar',\nPizza pra todo mundo!!\nA história não acaba aqui e nem agora...")
            quebra_linha()
            nova_tentativa()
            # volta ao inicio do jogo
        else:
            quebra_linha()
            print("Mas é vacilão mesmo!!!")
            general_ougar()
            quebra_linha()
            nova_tentativa()
            
            # volta ao inicio do jogo
            
    while (jogador == 2):

        if jogador == 2:            
            print("Estamos a caminho da ""Europa"" e uma nave inimiga se aproxima!!!\n")
            quebra_linha()
        fase_01 = int(input("[ 1 ] Você se teletransporta para a nave inimiga com uma equipe e os surpreende.\n[ 2 ] Você vai sozinho. Sempre foi muito corajoso!\n"))

        if fase_01 == 1:
            quebra_linha()
            print("Discreto e inteligente, isso mesmo!!!")
            print("Chegamos sãos e salvos a europa graças ao ataque bem sucedido \nmas os alienigenas ja sabem de nossa presença.\n")
            quebra_linha()
        else:
            quebra_linha()
            print("Aí não!! DEU RUIM!!!")
            general_ougar()
            nova_tentativa()
        fase_02 = int(input("[ 1 ] Você desiste da missão e se junta ao seus antigos companheiros alienígenas.\n[ 2 ] Você usa sua arma biologica para abrir caminho até a base.\n"))
            # voce reinicia o jogo
        if fase_02 == 2:
            quebra_linha()
            print("Você é incrível, mas ainda não acabou!")
            print("Tivemos algumas baixas, acontece!! Missão está difícil mas estamos de fora da base. Precisamos entrar.\n")
            quebra_linha()
        else:
            quebra_linha()
            print("Aí não!! Eles são impiedosos com traidores!!!")
            general_ougar()
            nova_tentativa()
            #voce reinicia ou para o jogo
        fase_03 = int(input("[ 1 ] Você se teletransporta para dentro da base e resgata todos sobreviventes.\n[ 2 ] Você tenta encontrar uma entrada nos fundos.\n"))
        if fase_03 == 1:
            quebra_linha()
            msg_vitoria()
            quebra_linha()            
            print("SUCESSO na missão, voltamos para 'Esquadra Estelar',\nPizza pra todo mundo!!\nA história não acaba aqui e nem agora...")
            nova_tentativa()
        else:
            quebra_linha()
            print("Péssima escolha!! Perdeu tempo e foi encontrado!!!\nMissão foi um fracasso!!!")
            general_ougar()
            nova_tentativa()
            #voce reinicia o jogo

    while (jogador == 3):

        if jogador == 3:
            print("Estamos a caminho da ""Europa"" e uma nave inimiga se aproxima!!!\n")
            fase_01 = int(input("[ 1 ] Você lança um ataque com misseis nucleares.\n[ 2 ] Você ativa campo de camuflagem e espera eles sairem do alcance.\n"))
        if fase_01 == 1:
            quebra_linha()
            print("Parabéns, começamos bem!!!")
            print("Chegamos sãos e salvos a europa graças ao ataque bem sucedido \nmas os alienigenas ja sabem de nossa presença.\n")
            
        else:
            quebra_linha()
            print("Isso atrasou a missão, eles estão em patrulha e não vão se distanciar tão cedo!!!")
            general_ougar()
            nova_tentativa()
            #reinicia o jogo
            
        fase_02 = int(input("[ 1 ] Você sai da nave com a equipe e entra em combate direto para chegar a base!!!\n[ 2 ] Você usa sua arma de choque da nave para atordoa-los.\n"))
        if fase_02 == 2:
            quebra_linha()
            print("Você é incrível, mas ainda não acabou!!!")
            print("Tivemos algumas baixas, acontece!!\nMissão está difícil mas estamos de fora da base. Precisamos entrar.\n")
            fase_03 = int(input("[ 1 ] Você usa seu laser em potência reduzida e abre a porta lateral.\n[ 2 ] Você explode a entrada principal com uma granada de nitrogênio.\n"))
        else:
            quebra_linha()
            print("Poxa, no mano a mano nãããããoooo!!! São mais fortes soldado(a)!!!")
            general_ougar()
            nova_tentativa()
            # volta inicio do jogo
        if fase_03 == 1:
            quebra_linha()
            msg_vitoria()
            quebra_linha()
            print("SUCESSO na missão, voltamos para 'Esquadra Estelar',\nPizza pra todo mundo!!\nA história não acaba aqui e nem agora...")
            nova_tentativa()
            #decide se joga novamente apos vencer.
        else:
            quebra_linha()
            print("Melhor sorte da próxima vez!!!")
            general_ougar()
            nova_tentativa()

            # Volta ao inicio do jogo

selecao_jogador()
#se não chama a função o jogo não roda.