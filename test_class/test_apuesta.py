import pytest
from apuesta import Apuesta

def test_prueba():
    assert(True)

def test_constructor():
    a = Apuesta()
    assert(a.fichas == 0) #verifica que el valor iniciañ de fichas sea 0 (true) si no manda un AssertionError

def test_repr():
    a = Apuesta()
    msj = a.__repr__() #llama al metodo repr de la clase apuesta y lo almacena en la variable msj
    assert("Apuestas: " in msj)
    assert("fichas: " in msj)
    assert("0" in msj) # verifica que esten la cadena de texto y lo devuelve

def test_ponerFicha(): #verifica que el metodo ponerFicha añade el numero de fichas
    a = Apuesta()
    a.ponerFicha(8)
    assert(a.fichas == 8)

    a = Apuesta()
    a.ponerFicha(2)
    assert(a.fichas == 2)

    a = Apuesta()
    a.ponerFicha(2)
    assert(a.fichas == 2)
    a.ponerFicha(2)
    assert(a.fichas == 4)

def test_tomarFicha_sin_argumentos(): #verifica que el metodo tomarFicha funcione correctamente sin tener un argumento, por defecto quita 1 si no tiene uno
    a = Apuesta()
    a.fichas = 5
    a.tomarFicha()
    assert(a.fichas == 4)

    a = Apuesta()
    a.fichas = 10
    a.tomarFicha()
    assert(a.fichas == 9)

def test_tomarFicha_error(): #Verificar que se lanza un ValueError si se intenta quitar fichas cuando no hay suficientes.
    with pytest.raises(ValueError): #espera que devuelva un valueError cuando se llama en metodo tomar ficha sin haber antes añedido fichas
        a = Apuesta()
        a.tomarFicha()