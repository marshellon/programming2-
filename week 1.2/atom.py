class Atom:
    def __init__(self,symbol,atomic_number,neutrons):
        self.atomic_number = atomic_number
        self.symbol = symbol
        self.neutrons = neutrons

    def proton_number(self):
        return self.atomic_number
    
    def mass_number(self):
        return self.atomic_number + self.neutrons

    def isotope(self,new_neutrons):
        self.neutrons = new_neutrons

    def __eq__(self,other):
        self.check_mass(other)
        return self.mass_number() == other.mass_number()

    def __gt__(self,other):
        self.check_mass(other)
        return self.mass_number() > other.mass_number()
    
    def __lt__(self,other):
        self.check_mass(other)
        return self.mass_number() < other.mass_number()
    
    def __le__(self,other):
        self.check_mass(other)
        return self.mass_number() <= other.mass_number()

    def check_mass(self,other):
        if self.atomic_number != other.atomic_number:
            raise ValueError("not the same atomic number")
        

# protium = Atom('H', 1, 1)
# deuterium = Atom('H', 1, 2)
# oxygen = Atom('O', 8, 8)
# tritium = Atom('H', 1, 2)
# tritium.isotope(3)

# assert tritium.neutrons == 3
# assert tritium.mass_number() == 4
# assert protium < deuterium
# assert deuterium <= tritium
# assert tritium >= protium
# print (oxygen > tritium) # <-- this should raise an Exception