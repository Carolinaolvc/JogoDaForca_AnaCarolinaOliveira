import random
    
# Escolher palavra:
def escolher_palavra(tema):
    if tema == 'FRUTAS':
        palavras = ['BANANA', 'GOIABA', 'MORANGO', 'ABACAXI', 'MELANCIA', 'CEREJA', 'CUPUACU', 'TANGERINA', 'LARANJA', 'MARACUJA', 'PESSEGO', 'PITANGA', 'GRAVIOLA', 'ACEROLA']
    elif tema == 'ANIMAIS':
      palavras = ['GIRAFA', 'ELEFANTE', 'TUBARAO', 'TARTARUGA', 'JIBOIA', 'LONTRA', 'RINOCERONTE', 'BUFALO', 'AVESTRUZ', 'LEOPARDO', 'CAMALEAO', 'CENTOPEIA', 'CORDEIRO', 'OVELHA', 'ESQUILO']
    elif tema == 'CAPITAIS':
        palavras = ['PARIS','TOQUIO', 'BERLIM', 'LONDRES', 'MOSCOU', 'PEQUIM', 'CAIRO', 'VIENA', 'DUBLIN', 'LISBOA', 'ATENAS', 'BRASILIA', 'PRAGA', 'ESTOCOLMO']
    else:
        return None

    return random.choice(palavras)

# Sortear tema e palavra:
temas = ['FRUTAS', 'ANIMAIS', 'CAPITAIS']
tema = random.choice(temas)
palavra = escolher_palavra(tema)


# Informações gerais:
palavra_secreta = list("_" * len(palavra))
tentativas = 0
chances = 5
erros = 1
letras_escolhidas = []

# Boneco da forca    
def desenhar_boneco(erros):
    if erros == 1:
        print(" ---┐")
        print(" o  |")
        print("    |")
        print("    |")
        print("    |")
        print("   _|_")
    elif erros == 2:
        print(" ---┐")
        print(" o  |")
        print(" |  |")
        print("    |")
        print("    |")
        print("   _|_")
    elif erros == 3:
        print(" ---┐")
        print(" o  |")
        print("/|  |")
        print("    |")
        print("    |")
        print("   _|_")
    elif erros == 4:
        print(" ---┐")
        print(" o  |")
        print("/|\ |")
        print(" |  |")
        print("    |")
        print("   _|_")
    elif erros == 5:
        print(" ---┐")
        print(" o  |")
        print("/|\ |")
        print("/ \ |")
        print("    |")
        print("   _|_")
    elif erros == 6:
        print(" ---┐")
        print(" o  |")
        print(" |  |")
        print("/ \ |")
        print("    |")
        print("   _|_")

# Inicio:

titulo = r"""
 ____ ____ ____ ____ _________ ____ ____ _________ ____ ____ ____ ____ ____ 
||J |||O |||G |||O |||       |||D |||A |||       |||F |||O |||R |||C |||A ||
||__|||__|||__|||__|||_______|||__|||__|||_______|||__|||__|||__|||__|||__||
|/__\|/__\|/__\|/__\|/_______\|/__\|/__\|/_______\|/__\|/__\|/__\|/__\|/__\|
"""

print(titulo)
print(f'\nO tema é: {tema}')
print(f"\nVocê tem {chances} tentativas!")


# Tentativas 
while tentativas < chances and "".join(palavra_secreta) != palavra:
    letra = input("\nInsira uma letra: ").upper()

    if len(letra) != 1 or not letra.isalpha():
        print("Entrada inválida! Digite apenas uma letra.")
        continue

    while letra in letras_escolhidas:
        print("\nVocê já tentou essa letra, digite outra.")
        letra = input("\nInsira outra letra: ").upper()
    
    letras_escolhidas.append(letra)
    
    if letra in palavra: 
        print("\nParabéns! Você acertou uma letra!")
        for w in range(len(palavra)):
            if letra == palavra[w]:
                palavra_secreta[w] = letra

    else:
        print("\nQue pena! Você errou!")
        print(desenhar_boneco(erros))
        tentativas = tentativas + 1
        erros += 1

    # Quantidade de tentativas restantes
    print (f"\nVocê já cometeu {tentativas} erros, ainda restam {chances - tentativas} tentativas.")
    
    # Estado atual da forca
    print ("\nEsse é seu jogo atual:")
    print (palavra_secreta)

    # Quais letras já foram tentadas:
    print ("\nEssas foram as letras já tentadas: ")
    for item in letras_escolhidas:
	    print (item, end=" ")

# Final do game

if tentativas == chances:
    print ("\nAcabaram suas tentativas! Você perdeu!")
    print(f"\nA PALAVRA ERA: {palavra}.")
    print("\n    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")
    
elif '_' not in palavra_secreta:
    print (f"\nPARABÉNS! VOCÊ GANHOU! A PALAVRA ERA: {palavra}")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")
