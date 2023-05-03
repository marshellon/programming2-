
from reader import Reader


class AverageYear:
    def __init__(self,path):
        self.path = path
        self.reader = Reader(self.path)
        self.month = ["Jan","Feb","Mar", "Apr",
                      "May","Jun","Jul","Aug",
                      "Sep","Oct","Nov","Dec"]

    def calculate_average(self):
        """
        calcualte the averages of the months over the course of 5 years
        """
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

# f = open("dSST.csv","r")
# amount_of_lines = (len(f.readlines()) -1) / 5
# temp_temperture_list =  [av.calculate_average() for x in range(round(amount_of_lines))]

# individual_temp_list = []
# for tempertures in temp_temperture_list:
#     for temperture in tempertures:
#         individual_temp_list.append(temperture)





