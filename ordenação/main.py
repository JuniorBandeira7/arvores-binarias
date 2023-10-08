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

    def travesiaInorder(self, raiz):
        if raiz is not None:
            self.travesiaInorder(raiz.esquerda)

            print(raiz.value)

            self.travesiaInorder(raiz.direita)
        '''
        Quando a função recursiva é chamada, o estado atual da função (como variáveis locais e posição na árvore) é armazenado em 
        uma "pilha de chamadas" (ou stack call). Quando a função recursiva retorna, ela volta ao estado anterior (à chamada anterior) na pilha de chamadas e continua de onde 
        parou.
        Quando a função inorder_traversal encontra um nó que é None (geralmente em um nó folha), ela retorna para o chamador anterior (pai) e continua a
        partir desse ponto. Isso cria o efeito de percorrer a árvore em ordem crescente, visitando os nós em ordem e garantindo que todos os nós sejam processados 
        corretamente.
        Esse uso de pilha de chamadas é uma característica fundamental da recursão e é chamado de "desenrolamento de pilha" (ou "stack unwinding"). Permite que a função 
        retorne a estados anteriores e continue o processamento de forma controlada até que todo o percurso na árvore seja concluído. É uma técnica poderosa e eficiente 
        para percorrer estruturas de dados recursivas, como árvores.
        '''
arvoreDesordenada = [9, 10 , 2, 5 , 8 , 0, 96, 48, 32, 99, 1, 3]
bsTree = BSTree()
for numero in arvoreDesordenada:
    bsTree.inserir(numero)
bsTree.travesiaInorder(bsTree.raiz)

    
        

        
