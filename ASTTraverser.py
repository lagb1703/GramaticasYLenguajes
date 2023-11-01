class ASTTraverser(object):

    ANDS = ['and', '*']

    ORS = ['or', '+']

    IMP = ['=>']

    DIMP = ['<=>']

    verdadero = ['true', '1']

    false = ['false', '0']

    def __init__(self):
        self.funciones = map()
        self.pila = []
        self.valores = []

    def visit(self, tree):
        method = getattr(self, tree.head, None)
        # print("Visit for {} will call {}".format(tree.head, method))
        if method:
            return method(tree)
        else:
            print("Method {} is not defined by the class".format(method))
    
    def expresion(self, tree):
        for i in tree.tail:
            self.visit(i)

    def start(self, tree):
        print("Start*- {}".format(tree))
        le = tree.tail[0]
        self.visit(le)
    
    def logicalexpression(self, tree):
        match len(tree.tail):
            case 3:
                if(tree.tail[0] == "("):
                    self.visit(tree.tail[1])
                else:
                    self.visit(tree.tail[0])
                    self.visit(tree.tail[2])
                    if tree.tail[1] in ASTTraverser.ANDS:
                        if self.valores[0]:
                            pass
                    elif tree.tail[1] in ASTTraverser.ORS:
                        pass
                    elif tree.tail[1] in ASTTraverser.IMP:
                        pass
                    elif tree.tail[1] in ASTTraverser.DIMP:
                        pass
    
    def parenle(self, tree):
        print("parenle {}".format(tree))
        print(len(tree.tail))

   