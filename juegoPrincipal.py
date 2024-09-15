from perinola import Perinola
from apuesta import Apuesta
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