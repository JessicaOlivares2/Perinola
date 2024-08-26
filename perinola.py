#from random import randint
#class Dado:
#    def __init__(self, caras=6):
#        if (caras <= 0):
#            raise ValueError("El numero de caras no puede ser negativo")
#        self.numero = 1
#        self.caras = caras
#    def __repr__(self):
#        return f"Dado de {self.caras} caras: {self.numero}"
#    def tirar(self):
#        self.numero = randint(1, self.caras)
#        return self.numero    
    
from random import choice


class Perinola:
    def __init__(self):
        self.cara_visible = ("Toma 1")
    def __repr__(self):
        return f"Salio: {self.cara_visible}"
    def tirar(self):
        caras = ("Pon 1", "Toma 2", "Todos Ponen",
        "Toma 1", "Pon 2", "Toma Todo")
        self.cara_visible = choice(caras)
        return self.cara_visible
    
