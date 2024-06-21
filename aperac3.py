import re

def palindromo(frase):
   
    frase_mudada = re.sub(r'[^a-zA-Z]', '', frase.lower())
    return frase_mudada == frase_mudada[::-1]

while True:
    frase = input('Digite uma frase digite "fim" para terminar): ')
    
    if frase.lower() == 'fim':
        print('Encerrando o programa...')
        break
    if palindromo(frase):
        print(f'"{frase}" é palíndromo')
    else:
        print(f'"{frase}" não é palíndromo')
