import pandas

data= pandas.read_csv("Squirrel_Census_-_Squirrel_Data.csv")
gray_suirrel=len(data[data["Primary Fur Color"]=="Gray"])
black_squirrel=len(data[data["Primary Fur Colour"]=="Black"])
cinammon_squirrel=len(data[data["[Primary Fur Colour"]=="Cinnamon"])

data_dict={
    "Fur_Colour":["gray_squirrel","blck_squirrel","cinammon_squirrel"],
    "Count":[gray_suirrel,black_squirrel,cinammon_squirrel]
}

data_file=pandas.DataFrame(data_dict)
data_file.to_csv("Squirrel Count.csv")
