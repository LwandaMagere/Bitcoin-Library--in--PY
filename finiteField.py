class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num < 0: # check that num is between 0 and prime -1 inclusive. If not, we get an invalid FieldElement
                                    # and raise a ValueError
            error = 'Num {} not in field range 0 to {}'.format(num, prime -1)
            raise ValueError(error)
        self.num = num  # The rest of the _init_ method assigns the initialization values to the object
        self.prime = prime
    
    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other): # checks if two object of the class FieldElements are equal. This is 
                            # only true when the num and prime properties are equal.
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

    def __ne__(self, other):
        return not (self == other)

    def __add__(self, other):
        if self.prime != other.prime: #We have to ensure that the elements are from the same finite field
                                    # otherwise this calculation doesn't have meaning
            raise TypeError('Cannot add two numbers in different Fields')
        num = (self.num + other.num) % self.prime # Addition in a finite field is defined with modulo operator
        return self.__class__(num, self.prime)# we have to return an instance of the class

    def __pow__(self, exponent):
        num = (self.num ** exponent) % self.prime
        return self.__class__(num, self.prime)


a = FieldElement(7, 13)
b = FieldElement(6, 13)
c = FieldElement(12, 13)

print(a+b==c)

print(a == b)

print (a == a)