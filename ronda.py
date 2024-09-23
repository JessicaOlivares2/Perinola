class Ronda:
    def __init__(self): #contructor que no recibe argumentos y comience con una lista de jugadores vacia
        self.jugadores = []
    
    def __repr__(self):
            return f'Jugador: {self.jugadores} ' #

    def agregarJugador(self,jugador):
        if jugador.fichas <= 0:#verifica si el jugador no tiene fichas y manda un error si no tiene
            raise ValueError(f"el jugador no tiene fichas")
        self.jugadores.append(jugador)#agrega los jugadores que tengan fichas

    def sacarJugadoresSinFichas(self):
        self.jugadores = [j for j in self.jugadores if not j.sinFichas()]
       
    def jugadorEnTurno(self):
       return self.jugadores[0] #devuelve el primer jugador

    def pasarTurno(self):
        # Mueve el primer jugador al final de la lista
        if self.jugadores:
            jugador = self.jugadores.pop(0)  # Saca el primer jugador
            self.jugadores.append(jugador)  # Lo agrega al final
 
    def quedaUnSoloJugador(self):
        return len(self.jugadores) == 1 #len muestra la longitud de la cadena y pregunta si  hay un solo jugador