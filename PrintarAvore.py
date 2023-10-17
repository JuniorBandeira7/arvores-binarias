from main import Node
from CalcularNivel import CalcularNivel

class PrintarArvore(CalcularNivel):
    def __init__(self):
        super().__init__()
        self.anterior = None
        self.anteAnterior = None

    def PrintarArvore(self, raiz):#o numero de niveis vai ser o numero de espaço do nó raiz ao passo que vai para a direita vai ganhando mais espaço e para direita perdendo espaço
        if raiz is not None:
            #anterior e anteAnterior sao usados para saber qual é o tamanho do pai do no 
            if self.anterior is None:
                self.anterior = raiz
            self.nivel = self.nivel + 1
            self.anteAnterior = anterior#ao ter 2 anteriores eu garanto que ao chegar em um no sem filhos o no anterior não vai ser o proprio no, pois ele vai ser o anteAnterior
            self.anterior = raiz
            self.travesiaInorder(raiz.esquerda)
            self.travesiaInorder(raiz.direita)


        else:
            self.nivel = self.nivel - 1
                                            
                                            
                                            
                                           # 1 a raiz nao pode nao ter espaço. ela tem a quantidade de espaço igual a quantidade de niveis
                                          # 2 1
                                         # 2   1 a base a direita tem o dobro da quantidade de niveis de quantidade de espaço
        # a base a esquerda nao tem espaços  
        #  lista de abertos
        #lista de fechado
        #lista pintar

        #adiciona o pai na lista de fechados
        #adiciona o filho na lista de abertos...(continua o raciocinio)
