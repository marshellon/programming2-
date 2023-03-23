from atom import Atom

class Molecule(Atom):
    def __init__(self,atom:list):
        self.atom  = atom
    
    def __str__(self):
        molecule = ''

        for atom,number in  self.atom:
            if number != 1:
               molecule += "".join(atom.symbol + str(number))
            elif number == 1:
  
                molecule += "".join(atom.symbol)
        
        return molecule
    

    def __add__(self,other):
        return self.__str__()+ other.__str__()

       
        



        
hydrogen = Atom('H', 1, 1)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)

water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
print(co2+water)

