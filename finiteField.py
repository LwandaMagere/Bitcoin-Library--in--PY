
class FieldElement:
    def __init__(self, num, prime):
        # We first check that num is between 0 and prime -1 inclusive. If not, we get an
        # invalid FieldElement and we raise a ValueError.
        if num >= prime or num < 0:
            error = 'Num {}  not in field range 0 to {}'. format(num, prime -1)
            raise ValueError(error)
        #The rest of the __init__ method assigns the initialization values to the object
        self.num = num
        self.prime = prime

    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)
    # The __eq__ method checks if two objects of class FieldElement are equal.
    # This is only true when the num and prime properties are equal.
    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime

a = FieldElement(7, 13)
b = FieldElement(6, 13)

    