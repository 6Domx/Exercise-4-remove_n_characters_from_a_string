# Pseudocode
# 1. Ask a user to input a string 
# 2. Analyze the string given by the user
# 3. Ask the user for a number less than the amount of characters of the string given
# 4. Print the string but remove the first n characters, where n is the given value of the user

while True:
    character_input = input("Please type a word: ")
    print("Your word: ", character_input)

    number_input = input("Please give us a number: ")
    if number_input.isdigit():
        number_input = int(number_input)
    else:
        print("Invalid, please input a number.")

        break

    new_character = print("Your new word if we remove the first ", number_input, " letter/s is: ", 
                          character_input[number_input: ])

    break