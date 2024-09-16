import pytest
from jugador import Jugador

def test_prueba():
    assert(True)


def test_constructor():
    j = Jugador(nombre='Jugador')
    assert(j.fichas == 5) #verifica que el valor iniciañ de fichas sea 0 (true) si no manda un AssertionError
    assert(j.nombre == 'Jugador')


def test_repr():
    j = Jugador(nombre="_Jugador")
    msj = j.__repr__() #llama al metodo repr de la clase apuesta y lo almacena en la variable msj
    assert("Jugador: " in msj)  
    assert("fichas" in msj)
    assert("5" in msj) # verifica que esten la cadena de texto y lo devuelve

def test_darFicha():
    #verifica que el metodod funcione sin argumento
    j = Jugador(nombre="Jugador", fichas=5)
    j.darFicha()  # Por defecto, debería agregar 1 ficha
    assert j.fichas == 6  # Debería haber 6 fichas después de agregar 1 ficha

    #verifica que el metodo darFicha funcione
    j = Jugador(nombre="Jugador", fichas=4)
    j.darFicha(5)  # Por defecto, debería agregar 5 ficha
    assert j.fichas == 9  # Debería haber 9 fichas después de agregar 5 ficha


    j = Jugador(nombre="Jugador", fichas=10)
    j.darFicha(5)  # Especifica que se deben agregar 5 fichas
    assert j.fichas == 15  # Debería haber 15 fichas después de agregar 5 fichas
  
    #verifica que el metodo funcione cuando el jugadore tenga 0 fichas
    j = Jugador(nombre="Jugador", fichas=0)
    j.darFicha(3)  # Especifica que se deben agregar 3 fichas
    assert j.fichas == 3  # Debería haber 3 fichas después de agregar 5 fichas
  