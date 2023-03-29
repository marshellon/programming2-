from reader import Reader

class AverageMonth:
    def __init__(self,path):
        self.path = path
        self.reader = Reader(self.path)
        self.month = ["Jan","Feb","Mar", "Apr",
                      "May","Jun","Jul","Aug",
                      "Sep","Oct","Nov","Dec"]

    def calculate_average_month(self):
        mean_per_month = [0*i for i in range(12)]
        divission_number = 5 
        dict_list = self.reader.get_lines()

        for dict_number in range(len(dict_list)):
            tempertures = [int(dict_list[dict_number][month].replace('.','')) for month in self.month]
            mean_per_month=[x + y for x, y in zip(mean_per_month, tempertures)]
        
        mean_per_month=[x/divission_number for x in mean_per_month]
        
        return mean_per_month
                




        