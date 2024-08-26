from random import randint
class Apuesta:
    def __init__(self,apuesta=0):
        if (apuesta <= 0):
            raise ValueError("El numero de apuesta no puede ser negativo")

    