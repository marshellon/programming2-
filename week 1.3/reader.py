from csvconverter import Csvconverter
import linecache as ln  

class Reader:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.csv_converter = Csvconverter(self.csv_path)
        self.pos = 2

    def add_observer(self):
        print("added observer")
        
    def remove_observer(self):
        print("remove observer")

    # I am missing the `notify_observers` method: how do you notify the 
    # observers of a change in the state of this class?

    
    def get_lines(self, nr=5):
        lines = [ln.getline(self.csv_path, nr+c) for c  in range(self.pos, self.pos+nr)]
        self.pos += nr
        # Who are you returning this to?
        # This is not the way an observable is supposed to work.
        return self.csv_converter.csv_to_json(lines)


red = Reader('dSST.csv')
print(red.get_lines()) #returns lines 2-6 as json
print("###########################################")
print(red.get_lines()) #returns lines 7-11 as json
print("###########################################")
print(red.get_lines()) #returns lines 12-16 as json 
