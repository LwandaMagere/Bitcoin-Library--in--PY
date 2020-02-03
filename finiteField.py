# Constructing a Finite Field in Python

#We want to represent each finite field element, so in Python, we’ll be creating a class
#that represents a single finite field element. Naturally, we’ll name the class
#FieldElement .

class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0: # We first check that num is between 0 and prime-1 inclusive. If not, we get an 
                                    #invalid FieldElement and we raise a ValueError , which is what we should raise when
                                    #we get an inappropriate value.
            error = 'Num {} not in field range 0 to {}'.format(num, prime - 1)
            raise ValueError(error)
        self.num = num # The rest of the __init__ method assigns the initialization values to the object.
        self.prime = prime 

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime #The __eq__ method checks if two objects of class FieldElement are 
                                                                   #equal.This is only true when the num and prime properties are equal.
    def __ne__ (self, other):
        return not(self == other)
    
    def __add__ (self, other):
        if self.prime != other.prime: # We have to ensure that the elements are from the same finite field, otherwise this
                                      #calculation doesn’t have any meaning.
            raise TypeError('Cannot add two numbers in different Field')
        num = ( self.num + other.num) % self.prime
        return self.__class__(num, self.prime) #We have to return an instance of the class, which we can conveniently access with
                                               #self.__class__ . We pass the two initializing arguments, num and self.prime ,
                                               #for the __init__ method we saw earlier.
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot subtract two numbers in different Fields')    
        num = (self.num - other.num) % self.prime
        return self.__class__(num, self.prime)

    def __mul__ (self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot multiply two numbers in different Fields')
        num = (self.num * other.num) % self.prime
        return self. __class__ (num, self.prime)

    def __pow__ (self, exponent):
        num = (self.num ** exponent) % self.prime
        return self.__class__(num, self.prime)
    
    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError('Cannot divide two numbers in differeent Fields')
        # use Fermat's little theorem:
        # self.num**(p-1) % p == 1
        # this means:
        # 1/n == pow(n, p-2, p)
        # we return an element of the same class
        num = self.num * pow(other.num, self.prime -2, self.prime) % self.prime
        return self.__class__(num, self.prime)

   # def __pow__(self, exponent):
    #    n = exponent % (self.prime -1) # Make the exponent into something within the 0 to p–2 range, inclusive.
     #   num = pow(self.num, n, self.prime)
      #  return self.__class__(num, self.prime)

class Point:
    def __init__(self, x, y, a, b):
        self.a = a
        self.b = b 
        self.x = x
        self.y = y 
        if self.y**2 != self.x**3 + a * x + b: # We check here that the point is actually on the curve.
            raise ValueError('({},{}) is not on the curve'.format(x,y)) 

    def __eq__(self, other): #Points are equal if and only if they are on the same curve and have the same coordinates.
        return self.x == other.x  and self.y == other. y and self.a == other.a and self.b == other.b
    
    def __ne__(self, other):
        return not (self == other)
    
def on_curve(x, y):
        return y**2 == x**3 + 5 * x + 7

print(on_curve(2,4))
print(on_curve(-1, -1))
print(on_curve(5,7))



p1 = Point(-1, -1, 5, 7)        
p2 = Point(-1, -2, 5, 7)



a = FieldElement(7, 13)
b = FieldElement(6, 13)
print(a == b)

#Coding Addition and Subtraction in Python

a = FieldElement(7, 13)
b = FieldElement(12, 13)
c = FieldElement(6, 13)

print(a + b == c)
print(a - b == c)
print(a * b == c)
print(a ** 3 == b)
print(a ** -3 == b)
