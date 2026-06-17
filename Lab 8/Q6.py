import random

class Personagem:
    def __init__(self,nome,vida):
        self.nome = nome
        self.vida = vida
    
    def tomar_dano(self,valor):
        self.vida -= valor

class Mago(Personagem):
    def __init__(self,nome,vida,mana):
        super().__init__(nome,vida)

        self.mana = mana
    
    def __str__(self):
        return f"Nome: {self.nome} Vida: {self.vida} Mana: {self.mana}"

    def __add__(self,valor:float):
        self.mana += valor
        return self.mana

    def __sub__(self,valor:float):
        self.mana -= valor
        if self.mana < 0:
            self.mana = 0
        return self.mana

    def __mul__(self,valor:float):
        self.mana *= valor
        return self.mana
    
    def __truediv__(self,valor:float):
        self.mana /= valor
        return self.mana

class Barbaro(Personagem):
    def __init__(self,nome,vida,stamina):
        super().__init__(nome,vida)

        self.stamina = stamina
        self.furia = False

    def __str__(self):
        return f"Nome: {self.nome} Vida: {self.vida} Stamina: {self.stamina} Furia: {self.furia}"

    def __add__(self,valor:float):
        if self.furia:
            self.stamina += valor *1.5
        else:
            self.stamina += valor
        return self.stamina

    def __sub__(self,valor:float):
        self.stamina -= valor
        if self.stamina < 1 and not self.furia:
            self.furia = True
            self.stamina = 5
        return self.stamina

    def __mul__(self,valor:float):
        self.stamina *= valor
        if self.furia:
            self.vida += 5
        return self.stamina
    
    def __truediv__(self,valor:float):
        self.stamina /= valor
        return self.stamina

match input("Qual tipo deseja (Mago/Barbaro):"):
    case "Mago":
        personagem = Mago(
            input("Nome: "),
            float(input("Vida: ")),
            float(input("Mana: "))
            )

    case "Barbaro":
        personagem = Barbaro(
            input("Nome: "),
            float(input("Vida: ")),
            float(input("Stamina: "))
            )

while True:
    print("="*50)
    print(personagem)
    print("="*50)
    print("1. Tomar poção simples")
    print("2. Tomar poção especial")
    print("3. Ataque básico")
    print("4. Ataque especial")
    print("5. Sair")
    print()
    print("Oq deseja realizar?")
    print("="*50)

    match int(input()):
        case 5:
            print(personagem)
            break

        case 1:
            personagem + 5
            personagem.tomar_dano(random.randint(1,10))

        case 2:
            personagem * 1.5
            personagem.tomar_dano(random.randint(1,10))

        case 3:
            personagem - 2
            personagem.tomar_dano(random.randint(1,10))

        case 4:
            personagem / 2
            personagem.tomar_dano(random.randint(1,10))

        case _:
            print("Opção Inválida!")