# Day 25
# CSV/Pandas

# with open("./files/csv/weather_data.csv") as file:
#     contents = file.readlines()
#     print(contents)

# import csv

# with open("./files/csv/weather_data.csv") as file:
#     contents = csv.reader(file)
#     print(contents)
#     temperatures = []
#     for row in contents:
#         if row[1] != "temp":
#             print(row)
#             temperatures.append(int(row[1]))
#     print(temperatures)

import pandas

# data = pandas.read_csv("./files/csv/weather_data.csv")
# print(data)
# print("\n")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)

# temp_list = data["temp"].to_list()
# print(temp_list)

# average = sum(temp_list)/len(temp_list)
# print(average)

#average
# print(data["temp"].mean())

#max
# print(data["temp"].max())

#get data in collumn
# print(data.condition)

#get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]
# print(monday.condition)
# print((int(monday.temp[0]) * 9/5) + 32)

#Create a dataframe from scratch
# data_dict = {
#    "students": ["Amy", "James", "Ana"],
#    "scores": [76,56,65] 
# }

# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("./files/csv/new_data.csv")


data = pandas.read_csv("./files/csv/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

data_color_gray_count = len(data[data['Primary Fur Color'] == "Gray"])
data_color_black_count = len(data[data['Primary Fur Color'] == "Black"])
data_color_cinnamon_count = len(data[data['Primary Fur Color'] == "Cinnamon"])
print(data_color_gray_count)
print(data_color_black_count)
print(data_color_cinnamon_count)

data_dict = {
   "Color": ["Gray", "Black", "Cinnamon"],
   "Count": [data_color_gray_count,data_color_black_count,data_color_cinnamon_count] 
}

data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("./files/csv/squirrel_census.csv")