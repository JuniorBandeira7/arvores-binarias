from main import Node
from main import BSTree

class CalcularNivel(BSTree):
    def __init__(self):
        super().__init__()
        self.nivel = 0
        self.nivelEsp = 0
    
    def CalcularNivel(self, raiz):
        if raiz is not None:
            self.nivel = self.nivel + 1 
            self.CalcularNivel(raiz.esquerda)

            self.nivel = self.nivel + 1
            self.CalcularNivel(raiz.direita)

            self.nivel = self.nivel - 1
        else:
            self.nivel = self.nivel - 1
            if self.nivelEsp < self.nivel:
                self.nivelEsp = self.nivel
        return self.nivelEsp