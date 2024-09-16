class Jugador:
    def __init__(self,nombre,fichas=5): #muestra el nombre y la cantidad de fichas, si no se asigna un numero, por defecto es 5
        self.nombre = nombre
        self.fichas = fichas

    def __repr__(self):
            return f'Jugador: {self.nombre}, fichas: {self.fichas} ' #devuelve el nombre y las fichas

    def darFicha(self, cuantas=1):
        """Agrega la cantidad especificada de fichas al jugador."""
        self.fichas += cuantas

    def sacarFicha(self, cuantas=1):
        if(cuantas > self.fichas):
            raise ValueError(f"no hay fichas suficiente (no podes sacar {cuantas}, el jugador tiene solo {self.fichas} fichas)")
    #si el numero de fichas a sacar es mayor al total que hay, va a salir un mensaje de error
        self.fichas -= cuantas # La cantidad de fichas del jugador se reduce en cuantas

    def tieneFicha(self, cuantas=1):
        """Devuelve True si hay al menos el jugador tiene la cantidad especificada de fichas."""
        return self.fichas >= cuantas #compara si el valor actual es mayor o igual a la cantidad que se quiere verificar

    def sinFichas(self):
        """Devuelve True si el jugador no tiene fichas."""
        return self.fichas == 0 #si el valor actual de fichas es 0 devuelve true)