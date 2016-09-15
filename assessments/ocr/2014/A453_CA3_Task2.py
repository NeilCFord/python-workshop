# initialize variables

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
output = ""

# get user input
# encrypt or decrypt

choice = input("Encrypt or Decrypt message? e/d ")

# message -> convert to uppercase

message = input("Enter your message: ")
message = message.replace(' ', '')
message = message.upper()

# keyword -> convert to uppercase
cipherword = input("Enter your cipher word: ")
cipherword = cipherword.upper()

# keyphrase = keyword times (integer of (length of message divided by length of keyword) plus one)

keyphrase = cipherword * (int(len(message)/len(cipherword))+1)

if choice == "e":
    # encrypt
    # loop through message

    for i in range(len(message)):

        # determine alphabet index of message character and equivilent keypharse character. increase each index by 1

        x = ALPHABET.index(message[i]) + 1
        y = ALPHABET.index(keyphrase[i]) + 1

        # add index values together to get cypher character index
        # handle values greater than 26 using modulo maths

        z = (x + y) % 26

        # append cypher character to encrypted message

        output = output + ALPHABET[z-1]

else:
    # decrypt
    # loop through message

    for i in range(len(message)):

        # determine alphabet index of message character and equivilent keypharse character. increase each index by 1

        x = ALPHABET.index(message[i]) + 1
        y = ALPHABET.index(keyphrase[i]) + 1

        # add 26 to message index then subtract keyphrase index.
        # handle values greater than 26 using modulo maths

        z = ((x + 26) - y) % 26

        # append plaintext character to decrypted message

        output = output + ALPHABET[z-1]

# print result.

print(output)
