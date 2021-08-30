from Restaurante import Restaurante

class ListaDoble():
    def __init__(self):
        self.inicio = None
    
    def insertar(self, ingrediente): 
        nueva_pizza = Restaurante(ingrediente)
        if self.inicio is None:
            self.inicio = nueva_pizza
        else:
            tmp = self.inicio
            while tmp.siguiente is not None:
                tmp = tmp.siguiente
            tmp.siguiente = nueva_pizza
    
    def mostrar_ordenes(self):
        actual = self.inicio
        entro = False
        i = 1
        while actual is not None:
            print('\t'+str(i)+') Pizza de', actual.ingrediente)
            entro = True
            actual = actual.siguiente
            i += 1
        return entro
    
    def extraer(self):
        actual = self.inicio
        if actual is not None:
            pizza = actual.ingrediente
            tmp = actual.siguiente
            if tmp is not None:
                self.inicio = tmp
            else:
                self.inicio = None
            return str(pizza)
        return None