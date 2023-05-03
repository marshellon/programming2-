import matplotlib.pyplot as plt
from avarageYear import AverageYear
from averageMonth import AverageMonth
import sys

# getting all the input from the user
print("set the data route and pick the data that ypu want to plot choices: 1 for year. 2 for month")
data_route = sys.argv[1]
plot_type = sys.argv[2]

if plot_type == "1":
    av =  AverageYear(data_route)
    f = open(data_route,"r")
    amount_of_lines = (len(f.readlines()) -1) / 5
    temp_temperture_list =  [av.calculate_average() for x in range(round(amount_of_lines))]

    individual_temp_list_year = []
    for tempertures in temp_temperture_list:
        for temperture in tempertures:
            individual_temp_list_year.append(temperture)

    plt.plot(individual_temp_list_year)
    plt.grid()
    plt.title("average temperture per 5 years")
    plt.show()


# just check te sys input. if it is 2 than plot the months
if plot_type == "2":
    av =  AverageMonth(data_route)
    f = open(data_route,"r")
    amount_of_lines = (len(f.readlines()) -1) / 5 # the amount of cycles we have to do in the list comprehension
    temp_temperture_list =  [av.calculate_average_month() for x in range(round(amount_of_lines))] # use list comprehension to get all the years

    individual_temp_list_month = []
    for tempertures in temp_temperture_list:
        for temperture in tempertures:
            individual_temp_list_month.append(temperture)

    plt.plot(individual_temp_list_month)
    plt.grid()
    plt.title("average temperture per month per 5 years")
    plt.show()

