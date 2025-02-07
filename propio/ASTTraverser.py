import copy

class ASTTraverser(object):

    ANDS = ['and', '*']

    ORS = ['or', '+']

    IMP = ['=>']

    DIMP = ['<=>']

    VERDADERO = ['true', '1']

    FALSO = ['false', '0']

    def __init__(self):
        self.funciones = {}
        self.macths = {}
        self.pila = []
        self.valores = []

    def visit(self, tree):
        # try:
        #     method = getattr(self, tree.head, None)
        #     if method:
        #         return method(tree)
        #     else:
        #         print("Method {} is not defined by the class".format(method))
        # except:
        #     print("fin")
        method = getattr(self, tree.head, None)
        if method:
            return method(tree)
        else:
            print("Method {} is not defined by the class".format(method))
    
    def expresion(self, tree):
        for i in tree.tail:
            if i != ';':
                self.valores = []
                self.pila = []
                self.visit(i)
                #print(self.macths)

    def start(self, tree):
        self.visit(tree.tail[0])
    
    def logicalexpression(self, tree):
        self.visit(tree.tail[0])

    def logicaloperation(self, tree):
        self.visit(tree.tail[0])
        first = self.valores.pop()
        if first in self.VERDADERO or first in self.FALSO or (first[0] == '(' and first[-1] == ')'):
            self.valores.append(first)
        else:
            self.valores.append(f'({first})')

    def ands(self, tree):
        self.visit(tree.tail[0])
        self.visit(tree.tail[2])
        first = self.valores.pop()
        second = self.valores.pop()
        if first in ASTTraverser.FALSO or second in ASTTraverser.FALSO:
            self.valores.append(ASTTraverser.FALSO[0])
        elif first in ASTTraverser.VERDADERO:
            self.valores.append(second)
        elif second in ASTTraverser.VERDADERO:
            self.valores.append(first)
        elif f'!({first})' == second or f'!({second})' == first:
            self.valores.append(ASTTraverser.FALSO[0])
        else:
            self.valores.append(f'{first}*{second}')

    def ors(self, tree):
        self.visit(tree.tail[0])
        self.visit(tree.tail[2])
        first = self.valores.pop()
        second = self.valores.pop()
        if first in ASTTraverser.VERDADERO or second in ASTTraverser.VERDADERO:
            self.valores.append(ASTTraverser.VERDADERO[0])
        elif first in ASTTraverser.FALSO:
            self.valores.append(second)
        elif second in ASTTraverser.FALSO:
            self.valores.append(first)
        elif f'!({first})' == second or f'!({second})' == first:
            self.valores.append(ASTTraverser.VERDADERO[0])
        else:
            self.valores.append(f'{first}+{second}')

    def imps(self, tree):
        self.visit(tree.tail[0])
        self.visit(tree.tail[2])
        first = self.valores.pop()
        second = self.valores.pop()
        if first in ASTTraverser.VERDADERO and second in ASTTraverser.FALSO:
            self.valores.append(ASTTraverser.FALSO[0])
        elif (first in self.VERDADERO) or (first in self.FALSO) or (second in self.VERDADERO):
            self.valores.append(ASTTraverser.VERDADERO[0])
        else:
            self.valores.append(f'({first}+!({second}))')

    def doubleimps(self, tree):
        self.visit(tree.tail[0])
        self.visit(tree.tail[2])
        first = self.valores.pop()
        second = self.valores.pop()
        if first == second:
            self.valores.append(ASTTraverser.VERDADERO[0])
        else:
            self.valores.append(f'(({first}+!({second}))*({second}+!({first})))')
    
    def negation(self, tree):
        self.visit(tree.tail[2])
        first = self.valores.pop()
        if first in ASTTraverser.VERDADERO:
            self.valores.append(ASTTraverser.FALSO[0])
        elif first in ASTTraverser.FALSO:
            self.valores.append(ASTTraverser.FALSO[0])
        else:
            self.valores.append(f'!({first})')
            
    
    def parenle(self, tree):
        self.visit(tree.tail[1])
        first = self.valores.pop()
        if first in self.VERDADERO or first in self.FALSO or (first[0] and first[-1]):
            self.valores.append(first)
        else:
            self.valores.append(f'({first})')

    def logicalterminal(self, tree):
        if tree.tail[0] in ASTTraverser.VERDADERO or tree.tail[0] in ASTTraverser.FALSO:
            self.valores.append(tree.tail[0])
        else:
            indexi = 1
            indexj = 0
            for i in range(1, len(self.pila) + 1):
                indexj = 0
                solucion = False
                print(self.funciones[self.pila[-i][0]][0])
                for j in self.funciones[self.pila[-i][0]][0]:
                    print(" ", j, tree.tail[0])
                    if j == tree.tail[0]:
                        solucion = True
                        break
                    indexj += 1
                if solucion:
                    break
                indexi += 1
            print(indexi, indexj, self.pila)
            if len(self.pila) < indexi or len(self.pila[-1]) == 1:
                self.valores.append(tree.tail[0])
                return
            self.valores.append(self.pila[-indexi][indexj + 1])
            #self.valores.append(ASTTraverser.VERDADERO[0])
    
    def display(self, tree):
        self.visit(tree.tail[2])
        print(self.valores.pop())

    def funtioncreatearguments(self, tree):
        for i in tree.tail:
            if i != ',':
                if not(isinstance(i, str)):
                    self.visit(i)
                else:
                    self.valores.append(i)

    def funtioncreate(self, tree):
        if self.funciones.get(tree.tail[0]):
            raise Exception(f'{tree.tail[0]} YA HA SIDO CREADO')
        if len(tree.tail) != 5:
            self.visit(tree.tail[2])
        funcion = [self.valores, copy.deepcopy(tree.tail[-1])]
        self.funciones[tree.tail[0]] = funcion

    def funtioncallarguments(self, tree):
        for i in tree.tail:
            if i != ',':
                self.visit(i)
                if i.head == "logicalexpression" and len(self.valores) > 0:
                    self.pila[-1].append(self.valores.pop())
    
    def funcioncall(self, tree):
        if not(self.funciones.get(tree.tail[0])):
            raise Exception(f'{tree.tail[0]} NO HA SIDO CREADO')
        funcion = self.funciones.get(tree.tail[0])
        self.pila.append([tree.tail[0]])
        if len(tree.tail) == 4:
            self.visit(tree.tail[2])
            if len(self.pila[-1])-1 != len(funcion[0]):
                raise Exception(f'{tree.tail[0]} LE HA SIDO PROPOSIONADO {len(self.pila[-1]) - 1} SIENDO QUE NECESITA {len(funcion[0])}')
        self.visit(funcion[1])
        self.pila.pop()

    def conditionals(self, tree):
        self.visit(tree.tail[0])

    def ifs(self, tree):
        self.visit(tree.tail[1])
        first = self.valores.pop()
        if first in ASTTraverser.VERDADERO:
            self.visit(tree.tail[4])
        else:
            self.visit(tree.tail[-1])

    def macthcreation(self, tree):
        if self.macths.get(tree.tail[0]):
            raise Exception(f"{tree.tail[0]} YA HA SIDO CREADO")
        ma = {}
        if len(tree.tail) == 9:
            self.visit(tree.tail[3])
            self.visit(tree.tail[5])
            self.visit(tree.tail[7])
            ma['_'] = self.valores.pop()
            ma["logicalexpression(logicalterminal('false'))"] = self.valores.pop()
            ma["logicalexpression(logicalterminal('true'))"] = self.valores.pop()
        else:
            self.visit(tree.tail[-2])
            ma['_'] = self.valores.pop()
            self.visit(tree.tail[3])
            for i in self.pila:
                ma[i[0]] = i[1]
        self.macths[tree.tail[0]] = ma


    def localmactharguments(self, tree):
        if tree.tail[0] == '(':
            self.visit(tree.tail[-1])
            self.pila.append([str(tree.tail[1]), self.valores.pop()])
            return
        for i in tree.tail:
            pass
            if i != ',':
                self.visit(i)

    def macthcall(self, tree):
        if not(self.macths.get(tree.tail[0])):
            raise Exception(f"{tree.tail[0]} NO HA SIDO CREADO")
        ma = self.macths[tree.tail[0]]
        print(ma['true'])
        self.valores.append('true')
        #self.valores.append(ma[str(tree.tail[2])])


   