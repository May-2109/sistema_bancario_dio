class Cliente:
    def __init__(self, nome, endereco, contas=[]):
        self.nome = nome
        self.endereco = endereco
        self.contas = contas
        
    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {", ".join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}" 
    
class Conta(Cliente):
    def __init__(self, saldo, numero, agencia, endereco, contas=[]):
        super().__init__(endereco, contas)
        self.saldo = saldo
        self.numero = numero
        self.agencia = agencia
        
p1 = Conta('Mayara Oliveira', 'Rua Paissandu, 126', '0001')
print(p1)