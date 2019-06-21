import random 
def jogar():
    print("************")
    print("****JOGO****")
    print("************")

    arquivo = open("EX12_Palavras.txt","r")
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    
    arquivo.close()

    numero = random.randrange(0,len(palavras))
    palavra_secreta = palavras[numero].upper()

    
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




####################
logo = open('python-logo.png', 'rb')
data = logo.read()
logo.close()

logo2 = open('python-logo2.png', 'wb')
logo2.write(data)
logo2.close()

