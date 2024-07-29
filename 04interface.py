from abc import ABC, abstractmethod

class ControleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass
    
    @abstractmethod
    def desligar(self):
        pass

 


class ControleTV(ControleRemoto):
    def ligar(self):
        print('Ligando a TV...')
        print('Ligado!')
        

    def desligar(self):
        print('Desligando a TV...')
        print('Desligado!')
        
class ControleArCondicionado(ControleRemoto):
    def ligar(self):
        print('Ligando a Ar Condicionado...')
        print('Ligado!')
    
    def desligar(self):
        print('Desligando a Ar Condicionado...')
        print('Desligado!')
      
    
    

controle = ControleTV()
controle.ligar()
controle.desligar()

controle = ControleArCondicionado()
controle.ligar()
controle.desligar()