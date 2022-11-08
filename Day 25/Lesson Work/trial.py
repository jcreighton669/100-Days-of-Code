# import csv
import pandas

# with open("weather_data.csv") as weather:
#     data = weather.readlines()
#
# print(data)

# with open("weather_data.csv") as weather:
#     data = csv.reader(weather)
#     temps = []
#     for row in data:
#
#         if row[1] != "temp":
#             temps.append(int(row[1]))
#         else:
#             temps.append(row[1])
# print(temps)

import pandas

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(len(temp_list))
#
# print(data["temp"].mean())
# print(data["temp"].max())
#
# # Get Data in Columns
# print(data["condition"])
# print(data.condition)

# Get Data in Rows
# print(data[data.day == "Monday"])
#
# print(data[data.temp == data.temp.max()])
#
# monday = data[data.day == "Monday"]
# print(monday.condition)
#
#
# def c_to_f(temp):
#     return (9 / 5) * temp + 32
#
#
# print(c_to_f(monday.temp))
#
# Create a dataframe from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")