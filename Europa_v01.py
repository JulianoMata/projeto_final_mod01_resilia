with open("introducaoEuropa.txt", "r", encoding = "utf-8") as arquivo:
    introducaoEuropa = arquivo.read()
    
    print("{:>60}".format(introducaoEuropa))

           #abrir arquivo de introdução "Europa", conta a história.   
                              
def quebra_linha():
    print('-=' * 42)

def nova_tentativa():    
    print("Voltar ao jogo?")   
    nova_tentativa = int(input("[ 1 ] Sim [ 2 ] Não\n"))
    if  nova_tentativa == 1:
        selecao_personagem()
    else:
        print("Fica para uma próxima então!!!")
        exit()

def selecao_personagem():
    quebra_linha()
    print(("==-" * 12) + "MISSÃO EUROPA" + ("-==" * 12))
    
    quebra_linha()
    print("Agora é com você...\n")
    print("O tempo não está ajudando...\n")
    print("Estamos em uma viagem pelo universo...\n")
    print("Antes vc tem uma missão...\n")
    print("Escolha um jogador:\n")
    quebra_linha()
    jogador = int(input("[ 1 ] MADRE  [ 2 ] MARFÃO  [ 3 ] SUCA \n"))
    
    
    
    if jogador == 1:
        print("Madre , 34 anos, natural de Uberlandia/MG, pscicóloga militar(NASA) com poderes de telecinese.\n")
        quebra_linha()
        #escolha_sim_ou_nao()
    elif jogador == 2:
        print(
            "Marfão, alienígena(idade não definida), Zotax(refugiado), biólogo/geneticista com poderes de teletransporte.\n")
        quebra_linha()
        #escolha_sim_ou_nao()
    elif jogador == 3:
        print("Suca, 45 anos, natural de Berlim/Alemanha, piloto/navegador experiência em combate, habilidade com armas.\n")
        quebra_linha()
        #escolha_sim_ou_nao()
    else:
        print("*** Escolha inválida ***\nEscolha [ 1 ] [ 2 ] ou [ 3 ]")
        selecao_personagem()
        #retornar ao inicio do jogo.
    
    print("Confirma escolha ou trocar? ")
    quebra_linha()   
    confirma_escolha = int(input("[ 1 ] Confirma [ 2 ] Troca\n"))
    if  confirma_escolha == 1:
        quebra_linha()
        
    elif confirma_escolha == 2:
        quebra_linha()
        nova_tentativa()
    else:
        print("valor innválido!")
        nova_tentativa()
        
                   
    

    while (jogador == 1):

        if  jogador == 1:
            print("Estamos a caminho da 'Europa' e uma nave de guerra inimiga se aproxima!!!\n")
            quebra_linha()
        
        
            fase_01 = int(input("[ 1 ] Você ataca a nave enviando asteroides com seu poder de telecinese.\n[ 2 ] Você se esconde no banheiro.\n"))

        else:
            print("Você perdeu!")
            quebra_linha()
            nova_tentativa()
            # inicio do jogo

        if fase_01 == 1:
            print("Você passou!!!\n")
            print("Chegamos sãos e salvos a europa graças ao ataque bem sucedido \nmas os alienigenas ja sabem de nossa presença.\n")
            quebra_linha()
            fase_02 = int(input("[ 1 ] Você destroi todos q se aproximam provocando uma tempestade de poeira espacial.\n[ 2 ] Você tenta conversar com os alienígenas, oferece sorvete e balas.\n"))
            
        else:
            print("Fugir  ou se esconder nunca foi uma escolha!!!")
            nova_tentativa()
            # volta ao inicio do jogo

        if fase_02 == 1:
            print("Você é incrível, mas ainda não acabou!")
            print("Tivemos algumas baixas, acontece!! Missao está difícil mas estamos de fora da base. Precisamos entrar.\n")
            quebra_linha()
            fase_03 = int(input("[ 1 ] Você arranca a porta com toda fúria e resgata nossos amigos.\n[ 2 ] Você aperta a campainha e espera.\n"))
        
        else:
            print("Tá de brincadeira, vidas em jogo e faz isso?!")
            quebra_linha()
            nova_tentativa()
            # volta ao inicio do jogo

        if fase_03 == 1:
            quebra_linha()
            print("SUCESSO na missão, voltamos para 'Esquadra Estelar',\nPizza pra todo mundo!!\nA história não acaba aqui e nem agora...")
            quebra_linha()
            nova_tentativa()
           
            # volta ao inicio do jogo
        else:
            quebra_linha()
            print("vc perdeu!!!")
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
            fase_02 = int(input("[ 1 ] Você desiste da missão e se junta ao seus antigos companheiros alienígenas.\n[ 2 ] Você usa sua arma biologica para abrir caminho até a base.\n"))
        else:
            quebra_linha()
            print("Aí não!! DEU RUIM!!!")
            nova_tentativa()

            # voce reinicia o jogo
        if fase_02 == 2:
            quebra_linha()
            print("Você é incrível, mas ainda não acabou!")
            print("Tivemos algumas baixas, acontece!! Missão está difícil mas estamos de fora da base. Precisamos entrar.\n")
            fase_03 = int(input("[ 1 ] Você se teletransporta para dentro da base e resgata todos sobreviventes.\n[ 2 ] Você tenta encontrar uma entrada nos fundos.\n"))
        else:
            quebra_linha()
            print("Aí não!! Eles são impiedosos com traidores!!!")
            nova_tentativa()
            #voce reinicia ou para o jogo
        if fase_03 == 1:
            quebra_linha()
            print("SUCESSO na missão, voltamos para 'Esquadra Estelar',\nPizza pra todo mundo!!\nA história não acaba aqui e nem agora...")
            nova_tentativa()
        else:
            quebra_linha()
            print("Péssima escolha!! Perdeu tempo e foi encontrado!!!\nMissão foi um fracasso3")
            nova_tentativa()

             #voce reinicia ou para o jogo

    while (jogador == 3):

        if jogador == 3:
            print("Estamos a caminho da ""Europa"" e uma nave inimiga se aproxima!!!\n")
            fase_01 = int(input("[ 1 ] Você lança um ataque com misseis nucleares.\n[ 2 ] Você ativa campo de camuflagem e espera eles sairem do alcance.\n"))
        if fase_01 == 1:
            quebra_linha()
            print("Parabéns, começamos bem!!!")
            print("Chegamos sãos e salvos a europa graças ao ataque bem sucedido \nmas os alienigenas ja sabem de nossa presença.\n")
            fase_02 = int(input("[ 1 ] Você sai da nave com a equipe e entra em combate direto para chegar a base!!!\n[ 2 ] Você usa sua arma de choque da nave para atordoa-los.\n"))
        else:
            print("Isso atrasou a missão, eles estão em patrulha e não vão se distanciar tão cedo!!!")
            nova_tentativa()
        if fase_02 == 2:
            quebra_linha()
            print("Você é incrível, mas ainda não acabou!!!")
            print("Tivemos algumas baixas, acontece!!\nMissão está difícil mas estamos de fora da base. Precisamos entrar.\n")
            fase_03 = int(input("[ 1 ] Você usa seu laser em potência reduzida e abre a porta lateral.\n[ 2 ] Você explode a entrada principal com uma granada de nitrogênio.\n"))
        else:
            print("Poxa, no mano a mano nãããããoooo!!! São mais fortes soldado(a)!!!")
            nova_tentativa()
            # volta inicio do jogo
        if fase_03 == 1:
            quebra_linha()
            print("SUCESSO na missão, voltamos para 'Esquadra Estelar',\nPizza pra todo mundo!!\nA história não acaba aqui e nem agora...")
            nova_tentativa()
            #decide se joga novamente apos vencer.
        else:
            print("Melhor sorte da próxima vez!!!")
            nova_tentativa()

            # Volta ao inicio do jogo

selecao_personagem()
      
