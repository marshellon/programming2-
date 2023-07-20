import matplotlib.pyplot as plt
from avarageYear import AverageYear
from averageMonth import AverageMonth
import sys

# Good to abstract away the common code of both kinds of plotters.
class TemperaturePlotter:
    def __init__(self, data_route, plot_type):
        self.data_route = data_route
        self.plot_type = plot_type

    def plot_temperature(self):
        """
        function:   
                 Plot the mean of the temperture per 5 years of the data

        input:
                NAN specified in __init__
        output:
                Plot of the data
        """

        if self.plot_type == "1":
            av = AverageYear(self.data_route)
            f = open(self.data_route, "r")
            amount_of_lines = (len(f.readlines()) - 1) / 5
            temp_temperture_list = [av.calculate_average() for _ in range(round(amount_of_lines))]

            individual_temp_list_year = []
            for temperatures in temp_temperture_list:
                for temperature in temperatures:
                    individual_temp_list_year.append(temperature)

            plt.plot(individual_temp_list_year)
            plt.grid()
            plt.title("Average temperature per 5 years")
            plt.show()

        elif self.plot_type == "2":
            av = AverageMonth(self.data_route)
            f = open(self.data_route, "r")
            amount_of_lines = (len(f.readlines()) - 1) / 5
            temp_temperture_list = [av.calculate_average_month() for _ in range(round(amount_of_lines))]

            individual_temp_list_month = []
            for temperatures in temp_temperture_list:
                for temperature in temperatures:
                    individual_temp_list_month.append(temperature)

            plt.plot(individual_temp_list_month)
            plt.grid()s
            plt.title("Average temperature per month per 5 years")
            plt.show()


# Getting all the input from the user
data_route = sys.argv[1]
plot_type = sys.argv[2]

# Create an instance of TemperaturePlotter and plot the temperature
plotter = TemperaturePlotter(data_route, plot_type)
plotter.plot_temperature()
