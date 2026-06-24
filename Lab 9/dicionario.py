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


# QUESTÃO 3
def mesclar_dicionarios(d1:dict,d2:dict):
    d3 = d1
    for elemento in d2:
        if elemento in d3:
            if d2[elemento] > d3[elemento]:
                d3[elemento] = d2[elemento]
        else:
            d3[elemento] = d2[elemento]
    return d3

dicionario1 = {'a': 1, 'b': 2, 'c': 3}
dicionario2 = {'b': 4, 'd': 5}
resultado = mesclar_dicionarios(dicionario1, dicionario2)
print(resultado)

# QUESTÃO 4
def filtrar_dicionario(dados:dict,chaves_filtradas:list):
    d = {}
    for elemento in chaves_filtradas:
        d[elemento] = dados[elemento]
    return d

dados = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
chaves_filtradas = ['a', 'c', 'e']
resultado = filtrar_dicionario(dados, chaves_filtradas)
print(resultado)

# QUESTÃO 5
def resultado_votacao(votos:list):
    resultado = {}
    total = 0
    for dicionario in votos:
        for candidato in dicionario:
            if candidato in resultado:
                resultado[candidato] += dicionario[candidato]
                total += dicionario[candidato]
            else:
                resultado[candidato] = dicionario[candidato]
                total += dicionario[candidato]

    for candidato in resultado:
        resultado[candidato] = (candidato,resultado[candidato]/total*100)

    return resultado
votos = [
    {'candidato_A': 120, 'candidato_B': 85, 'candidato_C': 90},
    {'candidato_A': 110, 'candidato_B': 95, 'candidato_C': 80},
    {'candidato_A': 130, 'candidato_B': 78, 'candidato_C': 105},
]
resultado = resultado_votacao(votos)
print(resultado)