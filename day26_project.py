#Nato Project

# { new_key:new_value for (index,row) in df.iterrows() }

import pandas

user_name = input("Enter a word: ").upper()
data = pandas.read_csv("./nato_files/nato_phonetic_alphabet.csv")

all_codes = { row.letter:row.code for (index,row) in data.iterrows() }

name_list = [all_codes[letter] for letter in user_name]
print(name_list)
