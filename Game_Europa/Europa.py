# import (GAME-EUROPA.txt) - como importar txt???

import os
#limpeza do terminal

with open("Game_Europa\Arquivos_Imagem_ASCII\introducao_europa.txt", "r", encoding = "utf-8") as arquivo:
    introducaoEuropa = arquivo.read()
    
    print(f"\033[1;49;30m{introducaoEuropa}\033[m\n")

           #abrir arquivo de introdução "Europa", conta a história. 
           
def general_ougar():  
    with open("Game_Europa\Arquivos_Imagem_ASCII\ougar_imagem.txt", "r", encoding = "utf-8") as arquivo:
        ougar = arquivo.read()
    
        print(ougar)
        #mostra imagem alienígena(General Ougar) quando perde.
        
def msg_vitoria():  
    with open("Game_Europa\Arquivos_Imagem_ASCII\msg_vencedor.txt", "r", encoding = "utf-8") as arquivo:
        vencedor = arquivo.read()
        quebra_linha()
        print(vencedor)
        #mensagem de vitoria
        quebra_linha()
        
def opcao_invalida():
        quebra_linha()
        print(f"\033[1;49;31mFavor escolher opção válida.\033[m\n")
                              
def nova_tentativa():
    os.system("cls or clear") #limpeza do terminal    
    print(f"\033[1;49;31mVoltar ao jogo?\033[m\n")   
    nova_tentativa = int(input("[ 1 ] Sim [ 2 ] Não\n"))
    if  nova_tentativa == 1:
        
        selecao_jogador()
    else:
        print(f"\033[1;49;31mFica para uma próxima!!!\033[m")
        exit()


def quebra_linha():
    linha = ("-=" * 50)
    print(f"\033[33m{linha.center(100)}\033[m")
    
def titulo_jogo():
    titulo = (" MISSÃO ")
    print(f"\033[32m{titulo.center(100, '*')}\033[m")
    quebra_linha()
    with open("Game_Europa\Arquivos_Imagem_ASCII\europa_titulo.txt", "r", encoding = "utf-8") as arquivo:
        titulo = arquivo.read()
        print(f"\033[1;49;33m{titulo}\033[m")
        quebra_linha()
    print("Agora é com você...\n")
    print("O tempo não está ajudando...\n")
    print("Estamos em uma viagem pelo universo...\n")    
    print("Antes vc tem uma missão...\n")
   
quebra_linha()
titulo_jogo()
quebra_linha()
print(f"\033[1mEscolha um jogador.\033[m\n")

def selecao_jogador():
    jogador = int(input(f"\033[35m[ 1 ] MADRE  \033[m\n\033[32m[ 2 ] MARFÃO  \033[m\n\033[31m[ 3 ] SUCA \033[m\n"))
    quebra_linha()
    if jogador == 1:
        with open("Game_Europa\Arquivos_Imagem_ASCII\madre_imagem.txt", "r", encoding = "utf-8") as arquivo:
            madre_imagem = arquivo.read() #le arquivo txt com imagem ascii 
            print(madre_imagem) #mostra imagem
            quebra_linha()
            print(f"\033[1;49;30mMadre , 34 anos, natural de Uberlandia/MG, pscicóloga militar(NASA) com poderes de telecinese.\nReligiosa de extrema empatia, conhecida por agir com emoção em situações extremas.\033[m\n")
            quebra_linha()
            #definição jogador 01
       
    elif jogador == 2:
        with open("Game_Europa\Arquivos_Imagem_ASCII\marfao_imagem.txt", "r", encoding = "utf-8") as arquivo:
            marfao_imagem = arquivo.read()
            print(marfao_imagem)
            quebra_linha()
            print(f"\033[1;49;30mMarfão, alienígena(idade não definida), Zotax(refugiado), \nbiólogo/geneticista com poderes de teletransporte.\nChegou ao Planeta Terra fugindo da crueldade de seu líder(Hougar).\033[m\n")
            quebra_linha()
            #definição jogador 02
            
    elif jogador == 3:
        with open("Game_Europa\Arquivos_Imagem_ASCII\suca_imagem.txt", "r", encoding = "utf-8") as arquivo:
            suca_imagem = arquivo.read()
            print(suca_imagem)
            quebra_linha()
            print(f"\033[1;49;30mSuca, 45 anos, natural de Berlim/Alemanha, piloto/navegador experiência em combate, habilidade com armas.\nLegítimo soldado e nunca deixa ninguém para trás.\033[m\n")
            quebra_linha()
            #definição jogador 03
    else:
        quebra_linha()
        opcao_invalida()
        print(f"\033[1mEscolha entre 1 e 3\033[m\n")
        quebra_linha()
        selecao_jogador()
        #retornar ao inicio do jogo.
    
    print(f"\033[1mConfirma escolha ou troca?\033[m\n") 
    quebra_linha()
    confirma_escolha = int(input(f"\033[32m[ 1 ] Confirma \033\n\033[31m[ 2 ] Troca\033[m\n"))
    
    if  confirma_escolha == 1:
        quebra_linha()
        print(f"\033[1mÓtima escolha!!!\033[m\n")
        quebra_linha()
        
    else:
        quebra_linha()
        opcao_invalida()
        selecao_jogador()
        quebra_linha()
        #confirma a escolha do jogador
            
# def jogador_1
    while (jogador == 1):

        # if  jogador == 1:
        print(f"\033[1;49;30mEstamos a caminho de ""Europa"" e uma nave inimiga se aproxima!!!\033[m\n")
        quebra_linha()
        fase_01 = int(input("[ 1 ] Você ataca a nave enviando asteróides com seu poder de telecinese.\n[ 2 ] Você se esconde no banheiro e chora.\n[ 3 ] Você liga para sua mãe!!!\n"))
         
        if fase_01 == 1:
            quebra_linha()
            print(f"\033[1;49;32mVocê passou!!!\033[m\n")
            print(f"\033[1;49;30mChegamos sãos e salvos a europa graças ao ataque bem sucedido \nmas os alienigenas ja sabem de nossa presença.\033[m\n")   
            
        elif fase_01 == 2:
            quebra_linha()
            print(f"\033[1;49;31mFugir  ou se esconder nunca foi uma escolha!!!\033[m\n")
            print(f"\033[1;49;34mVamos tentar novamente?!\033[m\n")
            quebra_linha()
            nova_tentativa()
            
        elif fase_01 == 3:
            quebra_linha()
            print(f"\033[1;49;31mTá tão apavorado(a)!!! Resolve nada isso!!!\033[m\n")
            print(f"\033[1;49;34mVamos tentar novamente?!\033[m\n")
            quebra_linha()
            nova_tentativa()
            # inicio do jogo
        else:
            quebra_linha()
            opcao_invalida()
            nova_tentativa()           
            
        fase_02 = int(input("[ 1 ] Você destroi todos q se aproximam provocando uma tempestade de poeira espacial.\n[ 2 ] Você tenta conversar com os alienígenas, oferece sorvete e balas.\n"))

        if fase_02 == 1:
            quebra_linha()
            print(f"\033[1;49;32mVocê é incrível, mas ainda não acabou!\033[m\n")
            print(f"\033[1;49;30mTivemos algumas baixas, acontece!! \nMissao está difícil mas estamos de fora da base. \nPrecisamos entrar.\033[m\n")
            
        else:
            print(f"\033[1;49;31mTá de brincadeira, vidas em jogo e faz isso?!\033[m\n")
            general_ougar()
            nova_tentativa()

        fase_03 = int(input("[ 1 ] Você arranca a porta com toda fúria e resgata nossos amigos.\n[ 2 ] Você aperta a campainha e espera.\n"))

        if fase_03 == 1:
            quebra_linha()
            msg_vitoria()
            quebra_linha()
            print(f"\033[1;49;32mSUCESSO na missao, vamos voltar p casa!!!\nPizza pra todo mundo!!\n")
            quebra_linha()
            exit()
        else:
            quebra_linha()
            print(f"\033[1;49;31mComo é lesado(a)!!! Achou que daria certo?\033[m\n")
            general_ougar()
            quebra_linha()
            nova_tentativa()
            
  
            
# def jogador_2
    while (jogador == 2):
        print(f"\033[1;49;30mEstamos a caminho de ""Europa"" e uma nave inimiga se aproxima!!!\033[m\n")
            
        fase_01 = int(input("[ 1 ] Você se teletransporta para a nave inimiga com uma equipe e os surpreende.\n[ 2 ] Você vai sozinho. Sempre foi muito corajoso!\n"))
        
        if fase_01 == 1:
            quebra_linha()
            print(f"\033[1;49;32mDiscreto e inteligente, isso mesmo!!!\033[m\n")
            print(f"\033[1;49;30mChegamos sãos e salvos a europa graças a seu ataque furtivo \nmas os alienigenas ja sabem de nossa presença.\033[m\n")
            
        else:
            quebra_linha()
            print(f"\033[1;49;31mVocê é louco!! Deu ruim!!!\033[m\n")
            general_ougar()
            quebra_linha()
            nova_tentativa()
            
        fase_02 = int(input("[ 1 ] Você desiste da missão e se junta ao seus antigos companheiros alienígenas.\n[ 2 ] Você usa sua arma biologica para abrir caminho até a base.\n"))

        if fase_02 == 2:
            quebra_linha()
            print(f"\033[1;49;32mVocê é incrível, mas ainda não acabou!\033[m\n")
            print(f"\033[1;49;30mTivemos algumas baixas, acontece!! Missão está difícil mas estamos de fora da base. Precisamos entrar.\033[m\n")
            
        else:
            quebra_linha()
            print(f"\033[1;49;31mAí não!! Eles são impiedosos com traidores!!!\033[m\n")
            general_ougar()
            quebra_linha()
            nova_tentativa()
        
        fase_03 = int(input("[ 1 ] Você se teletransporta para dentro da base e resgata todos sobreviventes.\n[ 2 ] Você tenta encontrar uma entrada nos fundos.\n"))
        
        if fase_03 == 1:
            quebra_linha()
            msg_vitoria()
            quebra_linha()
            print(f"\033[1;49;32mSUCESSO na missao, vamos voltar p casa,\nHj tem lasanha e coca-cola pra todo mundo!!\033[m\n")
            exit()
        else:
            quebra_linha()
            print(f"\033[1;49;31mPéssima escolha!!! Perdeu tempo e foi encontrado!!!\nMissão foi um fracasso!!!\033[m\n")
            general_ougar()
            quebra_linha()
            nova_tentativa()
           

# def jogador_3
    while (jogador == 3):
        print(f"\033[1;49;30mEstamos a caminho da ""Europa"" e uma nave inimiga se aproxima!!!\033[m\n")
            
        fase_01 = int(input("[ 1 ] Você lança um ataque com misseis nucleares.\n[ 2 ] Você ativa campo de camuflagem e espera eles sairem do alcance.\n"))
        
        if fase_01 == 1:
            quebra_linha()
            print(f"\033[1;49;32mParabéns, começamos bem!!!\033[m\n")
            print(f"\033[1;49;30mChegamos sãos e salvos a europa graças ao ataque bem sucedido e sua perspicácia \nmas os alienigenas ja sabem de nossa presença.\033[m\n")
            
        else:
            quebra_linha()
            print(f"\033[1;49;31mIsso atrasou a missão, eles estão em patrulha e não vão se distanciar tão cedo!!!\033[m\n")
            general_ougar()
            quebra_linha()
            nova_tentativa() 
            
        fase_02 = int(input("[ 1 ]  Você sai da nave com a equipe e entra em combate direto para chegar a base!!!\n[ 2 ]  Você usa sua arma de choque da nave para atordoa-los.\n"))
  
        if fase_02 == 2:
            quebra_linha()
            print(f"\033[1;49;32mVocê é incrível, mas ainda não acabou!!!\033[m\n")
            print(f"\033[1;49;30mTivemos algumas baixas, acontece!!\nMissao está difícil mas estamos de fora da base. \nPrecisamos entrar.\033[m\n")
            
        else:
            quebra_linha()
            print(f"\033[1;49;31mPoxa, não mano!!! \nSão mais fortes soldado(a)!!!\033[m\n")
            general_ougar()
            nova_tentativa()
        
        fase_03 = int(input("[ 1 ] Você usa seu laser em potência reduzida e abre a porta lateral.\n[ 2 ] Você explode a entrada principal com uma granada de nitrogênio.\n"))
            
        if fase_03 == 1:
            quebra_linha()
            msg_vitoria()
            quebra_linha()
            print(f"\033[1;49;32mSUCESSO!!! Voltar para 'Esquadra Espacial',\nVamos em busca de um novo lar!!!\033[m\n")
            exit()   
            
        else:
            quebra_linha()
            print(f"\033[1;49;31mSó pode ter bebido!!! \nExplodiu foi tudo!!!\033[m\n")
            general_ougar()
            nova_tentativa()
            


selecao_jogador()
      
