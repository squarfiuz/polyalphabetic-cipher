import argparse

parser = argparse.ArgumentParser(description="Encrypt/Decrypt a message.")
parser.add_argument("--mode", choices=["encrypt", "decrypt"], help="The mode of the program to be executed.")
parser.add_argument("--message", help="The message to encrypt/decrypt (a-z A-Z).")
parser.add_argument("--key", help="The key to encrypt/descrypt the message (a-z A-Z).")

args = parser.parse_args()

key_index = 0
outpout_message = ""
alphabet = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")

for letter in args.message:
    letter_number_format = 0
    if args.mode == "encrypt":
        letter_number = (alphabet.index(letter) + 1) + (alphabet.index(args.key[key_index]) + 1)


        if letter_number > 52:
            letter_number_format = letter_number - 52
        else:
            letter_number_format = letter_number
    else:
        letter_number = (alphabet.index(letter) + 1) - (alphabet.index(args.key[key_index]) + 1)

        if letter_number < 1:
            letter_number_format = letter_number + 52
        else:
            letter_number_format = letter_number

    outpout_letter = alphabet[letter_number_format - 1]
    outpout_message = outpout_message + outpout_letter
    if key_index >= len(args.key) - 1:
        key_index = 0
    else:
        key_index = key_index + 1

print("Your encrypt message is:", outpout_message)