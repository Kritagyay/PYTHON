import pandas as pd
data=pd.read_csv("nato_phonetic_alphabet.csv")
# print(data)
data_dict=data.to_dict()

phonetic_dicrt={row.letter:row.code for(index,row) in data.iterrows()}

# print(phonetic_dicrt)
end_of_game=True
while end_of_game:
    word=input("Enter the word:").upper()
    try:
        output_list=[phonetic_dicrt[letter] for letter in word]
        print(output_list)
        end_of_game=False
    except KeyError:
        print("Sorry, only letters in the alphabet please!")












