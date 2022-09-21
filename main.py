choice = str(input("Do you want encrypt or decrypt? "))
if choice != "encrypt" and choice != "decrypt":
    quit()
message = str(input("What message do you want to encrypt/decrypt? ")).replace(" ", "")
key = str(input("With which key do you want to encrypt/decrypt this message? ")).replace(" ", "")

key_index = 0
outpout_message = ""
alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

for letter in message:
    letter_number_format = 0
    if choice == "encrypt":
        letter_number = (alphabet.index(letter) + 1) + (alphabet.index(key[key_index]) + 1)


        if letter_number > 52:
            letter_number_format = letter_number - 52
        else:
            letter_number_format = letter_number
    else:
        letter_number = (alphabet.index(letter) + 1) - (alphabet.index(key[key_index]) + 1)

        if letter_number < 1:
            letter_number_format = letter_number + 52
        else:
            letter_number_format = letter_number

    outpout_letter = alphabet[letter_number_format - 1]
    outpout_message = outpout_message + outpout_letter
    if key_index >= len(key) - 1:
        key_index = 0
    else:
        key_index = key_index + 1

print("Your encrypt message is:", outpout_message)