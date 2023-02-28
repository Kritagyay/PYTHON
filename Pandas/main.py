# with open ("weather_data (1).csv")as file:
#     data=file.readlines()
#     print(data)


# import csv
#
# with open ("weather_data (1).csv") as file:
#     data=csv.reader(file)
#     temperature=[]
#     for imp_data in data:
#         # print(imp_data)
#         if imp_data[1] != 'temp':
#             temperature.append(int(imp_data[1]))
#
#     print(temperature)

import pandas as pd
# data=pd.read_csv("weather_data (1).csv")
# print(data)
# print(data["temp"])

# data_dict=data.to_dict()
# print(data_dict)

# data_list=data["temp"].to_list()
# print(data_list)

# print(sum(data_list)/(len(data_list)))
# print(data["temp"].mean())
# print(data["temp"].max())

#get the data of row
# print(data[data.day=="Wednesday"])

# print(data[data.temp==data["temp"].max()])

# monday=data[data.day=="Monday"]
# print(monday.condition)
# temp=int(monday.temp)
# print(temp*9/5+32)

data_dict = {
    "student":["ajay","soham","Angel","Venom"],
    "scores":[15,58,65,36]
}

data = pd.DataFrame(data_dict)
print(data)

data.to_csv("data.csv")