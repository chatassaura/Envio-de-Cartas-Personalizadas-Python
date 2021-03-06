#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as people:
    people = people.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    l_text = letter.read()
    for person in people:
        clear_name = person.strip()
        new_text = l_text.replace('[name]', clear_name)
        with open(f"letter_for_{clear_name}.txt", mode="w") as new_letter:
            new_letter.write(new_text)

