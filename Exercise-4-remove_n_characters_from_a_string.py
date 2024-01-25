# Pseudocode
# 1. Ask a user to input a string 
# 2. Analyze the string given by the user
# 3. Ask the user for a number less than the amount of characters of the string given
# 4. Print the string but remove the first n characters, where n is the given value of the user

while True:

# Character input and to show the user his given word.
    character_input = input("Please type a word: ")
    print("Your word: ", character_input)

# Number input for the user to input how many letters will be removed.
    number_input = input("Please give us a number: ")

# To make sure that the number input will only accept integers
    if number_input.isdigit():
        number_input = int(number_input)
    else:
        print("Invalid, please input a number.")

        break

# To make sure that the given number is not higher than the character length.
    if number_input > len(character_input):
        print("Invalid, number must be lower than the character length.")

        break

# For printing the new character after removing the n characters.
    new_character = print("Your new word if we remove the first ", number_input, " letter/s is: ", 
                          character_input[number_input: ])

