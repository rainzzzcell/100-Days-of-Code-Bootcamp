Placeholder = "[name]"

# Read the names from the invited_names.txt file
with open("./Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

# Read the starting letter template
with open("./Input/Letters/starting_letter.txt") as start_file:
    start_letter = start_file.read()

# Create a personalized letter for each name
for name in names:
    stripped_name = name.strip()
    letter = start_letter.replace(Placeholder, stripped_name)
    with open(f"./Output/ReadyToSend/letter_to_{stripped_name}.txt", mode="w") as final_text:
        final_text.write(letter)

#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp