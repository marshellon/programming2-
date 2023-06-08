
class Csvconverter:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.header = self.read_header()

    def read_header(self):
        """
        reads the header of the csv file
        """
        with open (self.csv_path, "r") as file:
            header = file.readline().split(",")
        return header 
    
    def csv_to_json(self, lines):
        """
        csv to json

        input:
                lines from lines

        return :
                json dictionary

        """
        json = []
        for c, line in enumerate(lines):
            line = line.split(",")
            try:
                assert len(self.header) == len(line)
                json.append({h:line[c] for c,h in enumerate(self.header)})
            except AssertionError:
                print(f"Sukkel het werkt niet gassie. regel {line}  met regel nummer {c} is niet heeft niet zelde lengte")
        return json


   


    

            






            


