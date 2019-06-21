def jogar():
    print("************")
    print("****JOGO****")
    print("************")

    palavra_secreta = "macaco".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0
    
    print(letras_acertadas)
    
    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper() #retira espacos em banco

        index = 0 
        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):                             
                    letras_acertadas[index] = letra
                index +=1
        else:
            erros += 1

        if (erros == len(palavra_secreta)):
            break
        if ("_" not in letras_acertadas):
            break
        print(letras_acertadas)
        
    if ("_" not in letras_acertadas): 
        print("Voce ganhou!!")
    else:
        print("Voce Perdeu!!")      
    print("fim do jogo") 

if(__name__== "__main__"):
    jogar()
