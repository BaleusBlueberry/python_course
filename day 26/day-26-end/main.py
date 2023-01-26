student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass
import csv
import pandas
# student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
# dict_words = {index.letter:row.code for (index, row) in student_data_frame.iterrows()}
    #Access index and row
    #Access row.student or row.score


alpabet = pandas.read_csv("nato_phonetic_alphabet.csv")


game_is_on = True
while game_is_on:
    user_choise = input("please write a sentence to translate: ").upper()
    chosen_list = [*user_choise]

    
    answer = {let:alpabet[alpabet.letter == let].code.item() for let in chosen_list if let in list(alpabet.letter)}
    print(answer)




# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

