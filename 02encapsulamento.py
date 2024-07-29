class Conta:
    def __init__(self, nro_agencia, nro_conta, saldo=0):
        self.nro_agencia = nro_agencia
        self.nro_conta = nro_conta
        self.saldo = saldo
        
    def depositar(self, valor):
        # ...
        self.saldo += valor
    
    def sacar(self, valor):
        # ...
        self.saldo -= valor
    
    def mostra_saldo(self):
         # ...
        return self.saldo
        
    

conta = Conta('0001', 100)
conta.depositar(100)
print(f'{conta.__class__.__name__} = {conta.nro_agencia}\nAgência = {conta.mostra_saldo()}')
