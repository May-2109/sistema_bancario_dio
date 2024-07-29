class Bicicleta :
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        
        
    def Buzinar(self):
        print('Plim Plim')
    
    def Parar(self):
        print('Parando bicicleta...')
        print('Bicicleta parada!')
        
    def Correr(self):
        print('Vrummmmmm ...')
   
    def __str__(self):
        return f"{self.__class__.__name__}: {", ".join([f'{chave} = {valor}' for chave, valor in self.__dict__.items()])}"

        
b1 = Bicicleta("vermelha", "caloi", 2022, 600)
b1.Buzinar()
b1.Correr()
b1.Parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)

b2 = Bicicleta('verde','monark', 2000, 189)
Bicicleta.Buzinar(b2)
print(b2)