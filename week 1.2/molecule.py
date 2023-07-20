from atom import Atom

class Molecule:
    def __init__(self,atom:list):
        self.atom = atom

    def __str__(self):
        molecule = ''

        for atom, amount in self.atom:
            if amount != 1:
                molecule += "".join(atom.symbol + str(amount))
            else:
                molecule += "".join(atom.symbol)
        return molecule
        
    def __add__(self,other):
        # This is incorrect
        # The add-method shoud return a new Molecule. In your realisation you
        # just return a string.
        return self.__str__() + other.__str__()




hydrogen = Atom('H', 1, 1)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)

water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
sugger = Molecule( [ (carbon,6), (hydrogen, 12) ,(oxygen,6) ] )
print (water) # H2O
print (co2) # CO2
print (water + co2) # H2OCO2
print(sugger)

