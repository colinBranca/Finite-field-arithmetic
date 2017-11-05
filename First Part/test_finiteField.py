from finiteField import FiniteField

field = FiniteField(79)


a = field(109)
print 'a = {}'.format(a)

b = field(204)
print 'b = {}'.format(b)

#test addition
plus = a + b
print 'a + b = {}'.format(plus)

#test opposite
opposite = -a
print '- a = {}'.format(opposite)

#test substraction
minus = a - b
print 'a - b = {}'.format(minus)

#test multiplication
product = a * b
print 'a * b = {}'.format(product)

#test inverse
inverse = a.inverse()
print '1 / a = {}'.format(inverse)

#test division
mul = a * inverse
print 'a / a = {}'.format(mul)

#test division
quotient = a / b
print 'a / b = {}'.format(quotient)

#test power with b as finiteField
power = a**b
print 'a^b = {}'.format(power)

#test power with b as integer
power2 = a**4
print 'a^4 = {}'.format(power2)
