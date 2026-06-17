class Onibus:
    def __init__(self,placa,nome_motorista,assentos):
        self.placa = placa
        self.nome_motorista = nome_motorista
        lst = []
        for i in range(assentos):
            lst.append(False)
        self.assentos = lst

    def __len__(self):
        return len(self.assentos)

    def __getitem__(self,indice):
        if -1 < indice < len(self.assentos):
            return self.assentos[indice]
        else:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")
    
    def __setitem__(self,indice,valor):
        if -1 < indice < len(self.assentos):
            if isinstance(valor,bool):
                self.assentos[indice] = valor
                return self.assentos[indice]
            else:
                raise TypeError(f"Valor deve ser booleano (True/False)")
        else:
            raise IndexError(f"Escolha um valor entre 0 e {len(self.assentos)}")

    def __str__(self):
        return f"Ôninus({self.placa}) - Motorista: {self.nome_motorista}\nAssentos totais: {len(self.assentos)}\nAssentos ocupados: {self.assentos.count(True)}\nAssentos livres: {self.assentos.count(False)}"

onibus = Onibus("ABC-1234", "João Silva", 10)
print(len(onibus))
onibus[0] = True
print(onibus)