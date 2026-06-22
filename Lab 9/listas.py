# QUESTÃO 1
lista = [int(x) for x in input("Números Inteiro separados por espaço: ").split()]
print(lista)
print(lista[2:])
print(lista[-2:])
print(lista[::-1])
print(lista[::2])
print(lista[1::2])

# QUESTÃO 2
URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.reddit.com", "www.yahoo.com"]
print([dominio[4:-4] for dominio in URLs])

# QUESTÃO 3
import random
lista = [random.randint(-100,100) for x in range(10)]
print(sorted(lista))
print(lista)
print(lista.index(max(lista)))
print(lista.index(min(lista)))
soma = 0
for num in lista:
    soma += num
print(soma)
print(soma/10)

# QUESTÃO 4
lista_1 = [int(x) for x in input("Lista1 separada por espaço: ").split()]
lista_2 = [int(x) for x in input("Lista2 separada por espaço: ").split()]
lista_3 = []
for i in range(max(len(lista_1),len(lista_2))-1):
    try:
        lista_3.append(lista_1[i])
    except:
        pass
    try:
        lista_3.append(lista_2[i])
    except:
        pass
print(lista_3)

# QUESTÃO 5
import random
lista_1 = [random.randint(0,50) for x in range(10)]
lista_2 = [random.randint(0,50) for x in range(10)]
lista_intersecao = []
for elemento in lista_1:
    if elemento in lista_2 and elemento not in lista_intersecao:
        lista_intersecao.append(elemento)
print(lista_1)
print(lista_2)
print(lista_intersecao)

# QUESTÃO 6