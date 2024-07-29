class Estudante:
    escola = 'Dio' #variável de classe, altera a informação para todos os objetos instânciados
    
    def __init__(self, nome, matricula ):
        self.nome = nome #variável de instancia, se aterada só irá impactar a instância modificada
        self.matricula = matricula
    
    def __str__(self):
        return f'{self.nome} ({self.matricula}) - {self.escola}'
    
def mostrar_valores(*objs):
    for obj in objs:
        print(obj)
    
    
aluno_1 = Estudante('Guilherme', '001')
aluno_2 = Estudante('Eduardo', '002')
mostrar_valores(aluno_1, aluno_2)

Estudante.escola = 'Python'
aluno_3 = Estudante('Charpie', '0003')
aluno_2.nome = 'Giovanna'
aluno_3.escola = 'Python'
mostrar_valores(aluno_1, aluno_2, aluno_3)
