from atom import Atom
from molecule import Molecule

class Chloroplast:
    def __init__(self):
        self.water = 0
        self.co2 = 0
    
    def add_molecule(self,molecule:Molecule):
        molecule = str(molecule)
        try:
            if molecule == "H2O":
                self.water += 1
            elif molecule == "CO2":
                self.co2 +=  1 
        except: ValueError("not a water or carbon molecule")

        if self.water > 6 and self.co2 > 12:
            self.photosyntese()

    def photosyntese(self):
        sugar_molecules = []

        self.co2 -= 12
        self.water -= 6

        hydrogen = Atom('H', 1, 1)
        carbon = Atom('C', 6, 6)
        oxygen = Atom('O', 8, 8)

        sugar  = Molecule( [ (carbon,6), (hydrogen, 12) ,oxygen,6 ] )
        for _ in range(6):
           sugar_molecules.append(Molecule( [ (oxygen,2) ]))
        
        sugar_molecules.append(sugar)
        print(f"amount of CO2:{self.add_molecule}. Amount of water:{self.water}")
        print(sugar_molecules)


        
    



         

