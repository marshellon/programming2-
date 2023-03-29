from reader import Reader

class AverageYear:
    def __init__(self,path):
        self.path = path
        self.reader = Reader(self.path)
        self.month = ["Jan","Feb","Mar", "Apr",
                      "May","Jun","Jul","Aug",
                      "Sep","Oct","Nov","Dec"]

    def calculate_average(self):
        mean_year = []
        dict_list = self.reader.get_lines()
        for dict_number in range(len(dict_list)):
            mean = 0
            for month in self.month:
                value  = dict_list[dict_number][month].replace(".","")
                mean += int(value)
            mean_year.append(mean/12)
        return mean_year
        


# av =  AverageYear("dSST.csv")
# print(av.calculate_average())


# red = av.calculate_average()
# print(red)

