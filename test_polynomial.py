from polynomial import Polynomials
from finiteField import FiniteField

field = FiniteField(79)

poly = Polynomials(field)

f = poly([7, 3, 54, 900, 83, 0, 9])
print(f)
