from perinola import Perinola
from apuesta import Apuesta
from jugador import Jugador
p = Perinola()
print(p)
print(p.cara_visible)

a = Apuesta()
print(a)
a.ponerFicha()
print(a)
a.tomarFicha()
print(a)
a.tomarTodas()
print(a)
a.tieneFicha()
print(a)
a.estaVacia()
print(a)

j = Jugador("Tomas", 15)
print(j)
j.darFicha(5)
print(j)
j.sacarFicha(10)
print(j)
print(j.tieneFicha(5))  
print(j.sinFichas())    
