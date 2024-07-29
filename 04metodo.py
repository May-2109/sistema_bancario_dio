class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome 
        self.idade = idade
        
    @classmethod 
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    

    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
# p1 = Pessoa('Mayara', 31)
# print(p1.nome, p1)

p = Pessoa.criar_de_data_nascimento(1992, 9 ,21, 'Mayara')
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))
