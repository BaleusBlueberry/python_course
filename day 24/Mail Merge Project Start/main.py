#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as F:
    raw_names = F.readlines()

with open("Input/Letters/starting_letter.txt") as empty_letter:
    data = empty_letter.readlines()

# def replace():

for name in raw_names:
    new_name = name.replace("\n", "")
    letter_name = new_name + " invitation"
    new_line = data[0]
    new_line = new_line.replace("[name]", new_name)
    new_data = data.copy()

    new_data[0] = new_line
    print(new_data)
    finished_letter = ""
    for line in new_data:
        finished_letter += line

    with open(f"Output/readyToSend/{letter_name}.txt", "x") as letter_file:
        letter_file.write(finished_letter)



