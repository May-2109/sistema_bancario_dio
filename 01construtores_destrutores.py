class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando classe ...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado
        
    def __del__(self):
        print('Removendo a instância da classe')
        
    def Falar(self):
        print('auauauauauau')
        

def criar_cachorro():
    c = Cachorro('Zeus', "Branco e preto", False)
    print(c.nome)
        
criar_cachorro()