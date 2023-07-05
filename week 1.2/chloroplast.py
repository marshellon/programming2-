from atom import Atom
from molecule import Molecule

class Chloroplast:
    def __init__(self):
        self.water = 0
        self.co2 = 0

    def add_molecule(self, molecule):
        try:
            if molecule == water:
                self.water += 1
            elif molecule == co2:
                self.co2 += 1
            else:
                raise ValueError('Is niet goed dude!!!!!')
        except: TypeError
        
        if self.water >= 12 & self.co2 >= 6:
            self.photosynthesis()
            print(" Starting photosynthesis")
        else:
            return []
    
    def photosynthesis(self):

        self.water = self.water - 12
        self.co2 = self.co2 - 6
        oxygen = Atom('O', 8, 8)
        glucose = Molecule([(carbon, 6), (hydrogen, 12), (oxygen, 6)])
        O = Molecule([(oxygen,2)])

        print([(glucose, 1), (O, 6)])

    def __str__(self):
        print("The amount of water and CO2")
        return f'Water: {self.water}\nCO2: {self.co2}'








#######################################################
hydrogen = Atom('H', 1, 1)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)

water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
demo = Chloroplast()
els = [water, co2]

while (True):
    print ('\nWhat molecule would you like to add?')
    print ('[1] Water')
    print ('[2] carbondioxyde')
    print ('Please enter your choice: ', end='')
    try:
        choice = int(input())
        res = demo.add_molecule(els[choice-1])
        if (len(res)==0):
            print (demo)
        else:
            print ('\n=== Photosynthesis!')
            print (res)
            print (demo)

    except Exception:
        print ('\n=== That is not a valid choice.')   



         

