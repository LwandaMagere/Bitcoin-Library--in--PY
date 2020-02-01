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
    
a = FieldElement(7, 13)
b = FieldElement(6, 13)
print(a == b)