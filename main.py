class Node():
    def __init__(self, node):
        self.value = node
        self.esquerda = None#menor
        self.direita = None#maior
    
class BSTree():
    def __init__(self):
        self.raiz = None

    def inserir(self, node):
        if self.raiz is None:
            self.raiz = Node(node)
        else:
            self.inserirRecursivo(self.raiz, node)

    def inserirRecursivo(self, raiz, node):
        if node < raiz.value:
            if raiz.esquerda is None:
                raiz.esquerda = Node(node)
            else:
                self.inserirRecursivo(raiz.esquerda, node)

        else:
            if raiz.direita is None:
                raiz.direita = Node(node)
            else:
                self.inserirRecursivo(raiz.direita, node)

    
        

        
