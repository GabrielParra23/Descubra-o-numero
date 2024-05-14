import random
from replit import clear
from logo import logo

hard = 5
easy = 10

def chances(modo):
    
    if modo == "hard":
        return hard
    elif modo == "easy":
        return easy
 
def tentativas(vida,tentativa,numero):
    global fim_jogo 
    
    if tentativa == numero:
        fim_jogo = False
        print("Voce acertou o numero")
    
    elif tentativa > numero:
        print("Muito alto")
        return vida - 1
        
    else:
        print("Muito baixo")
        return vida - 1 
        
def game():
    jogo = True
    while jogo == True:
        fim_jogo = True
        print(logo)
        numero = random.randint(1,101)
        ("Bem vindo ao jogo: Acerte o numero ")
        print("Voce deve acertar o numero de 1 a 100")
        dificuldade = input("Escolha a dificuldade \"easy\" ou \"hard\"").lower()   
        vidas = chances(dificuldade)
    
        tentativa = 0
        clear()
        while tentativa != numero and fim_jogo == True:
        
            tentativa = int(input("Escolha 1 numero entre 1 e 100: "))
    
            vidas = tentativas(vidas,tentativa,numero)
            
            print(f"Voce possui {vidas} vidas")
        
    
            if vidas == 0:
                print(f"Suas chances acabaram o numero era {numero}")
                fim_jogo = False
        fim = input("Se deseja jogar novamente digite \"S\", se deseja parar digite \"N\"").lower()
        clear()
        if fim == "s":
            jogo = True
        else:
            jogo = False
      
game()  
    
    