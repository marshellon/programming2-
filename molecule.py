from atom import Atom

class Molecule():
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

    

