message = str(input("What message do you want to encrypt? ")).replace(" ", "")
key = str(input("With which key do you want to encrypt this message? ")).replace(" ", "")

key_index = 0
encrypt_message = ""
alphabet = list("abcdefghijklmnopqrstuvwxyz")

for letter in message:
    encrypt_letter_number = (alphabet.index(letter) + 1) + (alphabet.index(key[key_index]) + 1)
    encrypt_letter_number_format = 0
    if encrypt_letter_number > 26:
        encrypt_letter_number_format = encrypt_letter_number - 26
    else:
        encrypt_letter_number_format = encrypt_letter_number
    encrypt_letter = alphabet[encrypt_letter_number_format - 1]
    encrypt_message = encrypt_message + encrypt_letter
    if key_index >= len(key) - 1:
        key_index = 0
    else:
        key_index = key_index + 1

print("Your encrypt message is:", encrypt_message)