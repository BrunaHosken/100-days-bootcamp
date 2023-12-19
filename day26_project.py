#Nato Project

import pandas

data = pandas.read_csv("./nato_files/nato_phonetic_alphabet.csv")
all_codes = { row.letter:row.code for (index,row) in data.iterrows() }

def generate_nato():
    user_name = input("Enter a word: ").upper()
    try:
        name_list = [all_codes[letter] for letter in user_name]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
        generate_nato()
    else:
        print(name_list)

generate_nato()