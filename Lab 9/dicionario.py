# QUESTÃO 1
def contagem_caracteres(texto):
    dict = {}
    for letra in texto:
        if letra in dict:
            dict[letra] += 1
        else:
            dict[letra] = 1
    return dict

frase = "python programming"
resultado = contagem_caracteres(frase)
print(resultado)

# QUESTÃO 2
