import random

def embaralhar_palavras(frase):
    palavras = frase.split()
    embaralha_frase = []

    for palavra in palavras:
        if len(palavra) <= 3:  
            embaralha_frase.append(palavra)
        else:
            letras_internas = list(palavra[1:-1])  
            random.shuffle(letras_internas)  
            palavra_embaralhada = palavra[0] + ''.join(letras_internas) + palavra[-1]  
            embaralha_frase.append(palavra_embaralhada)

    return ' '.join(embaralha_frase)

frase = "De acordo com uma pesquisa do linguista Matt Davis, o cérebro humano consegue ler palavras com as letras embaralhadas, contanto que a primeira e a última letra estejam no lugar correto."
print(embaralhar_palavras(frase))