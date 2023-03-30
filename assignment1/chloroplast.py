from molecule import Molecule
from atom import Atom


class Chloroplast(Atom):
    def __init__(self):
        self.co2 = 0 
        self.water = 0

    def add_molecule(self,molecule:Molecule):
        hydrogen = Atom('H', 1, 1)
        carbon = Atom('C', 6, 6)
        oxygen = Atom('O', 8, 8)
        results = []

        print (f"{self.co2} co2 molecuels pressent in this chloroplast")
        print (f"{self.water} water molecules pressent in this chloroplast")

        if molecule != "H20" or molecule != "CO2":

            try:
                raise ValueError("wrong molecule")
            except ValueError as err:
                print("not the correct molecule")

        if molecule == "H20":
            print("here")
            self.water += 1
        if molecule == "CO2":
            self.co2 += 1

        if self.water == 6 and self.co2 == 12:

            self.water -= 6
            self.co2 -= 12

            # molecules needed 
            sugar = Molecule( [ (carbon, 6), (hydrogen, 12), (oxygen, 6) ] )
            o2 = Molecule( [ (oxygen, 2) ])
            results.append(sugar,o2)

        return results
  

  

hydrogen = Atom('H', 1, 1)
carbon = Atom('C', 6, 6)
oxygen = Atom('O', 8, 8)

water = Molecule( [ (hydrogen, 2), (oxygen, 1) ] )
co2 = Molecule( [ (carbon, 1), (oxygen, 2) ])
demo = Chloroplast()
els = [water, co2]


# res = demo.add_molecule(water)


# while (True):
#     print ('\nWhat molecule would you like to add?')
#     print ('[1] Water')
#     print ('[2] carbondioxyde')
#     print ('Please enter your choice: ', end='')
#     try:
#         choice = int(input())
#         res = demo.add_molecule(els[choice-1])
#         if (len(res)==0):
#             print (demo)
#         else:
#             print ('\n=== Photosynthesis!')
#             print (res)
#             print (demo)

#     except Exception:
#         print ('\n=== That is not a valid choice.')




