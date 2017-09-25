from finiteField import FiniteField

field = FiniteField(79)
f = field.f

a = f(109)
print 'a = {}'.format(a)

b = f(2000)
print 'b = {}'.format(b)

plus = field.add(a, b)
print 'a + b = {}'.format(plus)

opposite = field.opposite(a)
print '- a = {}'.format(opposite)

minus = field.substract(b, a)
print 'b - a = {}'.format(minus)

product = field.multiply(a, b)
print 'a * b = {}'.format(product)

inverse = field.inverse(a)
print '1 / a = {}'.format(inverse)

mul = field.multiply(a, inverse)
print 'a / a = {}'.format(mul)

quotient = field.divide(a, b)
print 'a / b = {}'.format(quotient)

power = field.power(a, 15)
print 'a^15 = {}'.format(power)
