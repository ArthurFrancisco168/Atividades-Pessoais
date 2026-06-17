class Carteira:
    def __init__(self,moeda,saldo):
        self.moeda = moeda
        self.saldo = saldo
        self.conversao = {
            "BRL": 0.75,
            "USD": 0.15,
            "CNY": 1
        }
    
    def __add__(self, valor_yuan):
        self.saldo += valor_yuan * self.conversao[self.moeda]
        return self.saldo

    def __sub__(self, valor_yuan):
        self.saldo -= valor_yuan * self.conversao[self.moeda]
        return self.saldo
        
carteira = Carteira("USD",10)
print(carteira + 10)
print(carteira - 10)