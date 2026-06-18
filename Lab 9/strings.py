# QUESTÃO 1
print(f"Bem-Vindo, {input("Primeiro Nome: ")} {input("Segundo Nome: ")}!")

# QUESTÃO 2
print(f"Espaços em Branco: {input("Frase: ").count(" ")}")

# QUESTÃO 3
for i in range(len(nome := input("Nome: "))):
    print(nome[:i+1])

# QUESTÃO 4
numero = input("Número: ")
if len(numero) == 9:
    if numero[0] == "9":  
        print(f"Número Completo: {numero[:5]}-{numero[5:]}")
    else:
        print("Número Inválido!")
elif len(numero) == 8:
    print(f"Número Completo: 9{numero[:4]}-{numero[4:]}")
else:
    print("Número Inválido!")

# QUESTÃO 5
frase = input("Frase: ")
indices = []
for i, letra in enumerate(frase):
    if letra in "AEIOUaeiou":
        indices.append(i)
print(f"Índices: {", ".join(indices)}")