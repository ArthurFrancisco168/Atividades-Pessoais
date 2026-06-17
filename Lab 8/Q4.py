class Pessoa:
    def __init__(self,nome,altura):
        self.nome = nome
        self.altura = altura

    def __str__(self):
        return f"Nome: {self.nome} Altura: {self.altura}"

    def __gt__(self,other):
        return self.altura > other.altura

    def __lt__(self,other):
        return self.altura < other.altura

quant = int(input("Qnt pessoa:"))

lst = []
for i in range(quant):
    lst.append(Pessoa(input("Nome: "),float(input("Altura: "))))

print(max(lst))
print(min(lst))

for pessoa in sorted(lst):
    print(pessoa)