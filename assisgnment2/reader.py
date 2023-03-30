from csvconverter import Csvconverter
import linecache as ln  

class Reader:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.csv_converter = Csvconverter(self.csv_path)
        self.pos = 2

    
    def get_lines(self, nr=5):
        lines = [ln.getline(self.csv_path, nr+c) for c  in range(self.pos, self.pos+nr)]
        self.pos += nr
        return self.csv_converter.csv_to_json(lines)


# red = Reader('dSST.csv')
# print(red.get_lines()) #returns lines 2-6 as json
# print("###########################################")
# print(red.get_lines()) #returns lines 7-11 as json
# print("###########################################")
# print(red.get_lines()) #returns lines 12-16 as json 
