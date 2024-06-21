import re

def validador_senha(senha):

    mini_tamanho = len(senha) >= 8
    tem_maiuscula = re.search(r'A-Z]', senha) is not None
    tem_minuscula = re.search(r'[a-z]', senha) is not None
    tem_numero = re.search(r'/d', senha) is not None
    tem_carac_especial = re.search(r'[@#$%^&+=]', senha) is not None
    
    return mini_tamanho and tem_maiuscula and tem_minuscula and tem_numero and tem_carac_especial
 
senha1 = "Senha123@"
senha2 = "senhafraca"
senha3 = "Senha_fraca"
print(validador_senha(senha1)) 
print(validador_senha(senha2))  
print(validador_senha(senha3))  