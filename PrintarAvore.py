from main import Node
from main import BSTree

class PrintarArvore(BSTree):
    def __init__(self, raiz, nivel, nivelEsp, anterior, anteAnterior):
        super().__init__()
        self.nivel = 0
        self.nivelEsp = 0
        self.anterior = None
        self.anteAnterior = None
    def CalcularNivel(self, raiz):
        if raiz is not None:
            #Calcular nivel(tamanho) da arvore
            #testar com arvores de niveis conhecidos

    def PrintarArvore(self, raiz):#o numero de niveis vai ser o numero de espaço do nó raiz ao passo que vai para a direita vai ganhando mais espaço e para direita perdendo espaço
        if raiz is not None:
            #anterior e anteAnterior sao usados para saber qual é o tamanho do pai do no 
            if self.anterior is None:
                self.anterior = raiz
            self.anteAnterior = anterior#ao ter 2 anteriores eu garanto que ao chegar em um no sem filhos o no anterior não vai ser o proprio no, pois ele vai ser o anteAnterior
            self.anterior = raiz
            self.travesiaInorder(raiz.esquerda)

            if raiz.value < self.anteAnterior:#o print vai dentro desse if
                #perde espaço
            else:
                #ganha espaço

            self.travesiaInorder(raiz.direita)
        else:
            self.nivel = self.nivel - 1
                                            
                                            
                                            
                                            ''' 1 a raiz nao pode nao ter espaço. ela tem a quantidade de espaço igual a quantidade de niveis
                                               2 1
                                              2   1 a base a direita tem o dobro da quantidade de niveis de quantidade de espaço
         a base a esquerda nao tem espaços'''                    