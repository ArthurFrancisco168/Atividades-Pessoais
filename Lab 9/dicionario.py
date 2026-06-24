# # QUESTÃO 1
# def contagem_caracteres(texto):
#     dict = {}
#     for letra in texto:
#         if letra in dict:
#             dict[letra] += 1
#         else:
#             dict[letra] = 1
#     return dict

# frase = "python programming"
# resultado = contagem_caracteres(frase)
# print(resultado)

# # QUESTÃO 2


# QUESTÃO 3
def mesclar_dicionarios(d1:dict,d2:dict):
    d3 = d1
    for elemento in d2:
        if elemento in d3:
            if d2[elemento] > d3[elemento]:
                d3[elementno] = d2[elemento]
        else:
            d3[elemento] = d2[elemento]
    return d3

dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)