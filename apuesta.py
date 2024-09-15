class Apuesta:
    def __init__(self):
        self.fichas = 0 #inicia el atributo fichas en 0

    def __repr__(self):
        return f'Apuesta: {self.fichas} fichas' #muestra las fichas
    
    def ponerFicha(self, cuantas=1):
        self.fichas = self.fichas + cuantas #se agrega una cantidad al total de fichas
        #se agrega uno si no especifican

    def tomarFicha(self, cuantas=1):
        if(cuantas > self.fichas):
            raise ValueError(f"no hay fichas suficiente (no podes sacar {cuantas}, quedan {self.fichas})")
    #si el numero de fichas a sacar es mayor al total que hay va a salir un mensaje de error

    def tomarTodas(self):
        """Retira todas las fichas y devuelve el número de fichas retiradas."""
        fichas_tomadas = self.fichas #guarda el valor actual en la variable fichas_tomadas
        self.fichas = 0 #vacia la mesa (vacia el valor actual)
        return fichas_tomadas # devuelve lo que se saco

    def tieneFicha(self, cuantas=1):
        """Devuelve True si hay al menos la cantidad especificada de fichas."""
        return self.fichas >= cuantas #compara si el valor actual es mayor o igual a la cantidad que se quiere verificar

    def estaVacia(self):
        """Devuelve True si no hay fichas en la mesa."""
        return self.fichas == 0 #si el valor actual de fichas es 0 devuelve true (significa que no hay fichas en la mesa)