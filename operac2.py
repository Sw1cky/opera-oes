def muda_vogal(frase):
    vogal = "AEIOUaeiou"
    muda_frase= '' 

    for letra in frase:
        if letra in vogal:
            muda_frase += '*'
        else:
            muda_frase += letra

    return muda_frase

original_frase = input("digite sua frase: ")

muda_frase = muda_vogal(original_frase)
print("Frase alterada:", muda_frase)