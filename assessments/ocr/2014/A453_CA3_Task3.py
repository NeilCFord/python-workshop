# import modules

# initialize variables
ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
output = ""

# define functions


def file_read(file_name):
    # read in file, replace newline characters, convert to uppercase and return
    file_obj = open(file_name, 'r')
    file_content = file_obj.read()
    file_obj.close()
    file_content = file_content.replace('\n', ' ')
    file_content = file_content.upper()
    return file_content


def file_write(file_name, file_content):
    # write out file_content to file_name
    file_obj = open(file_name, 'w')
    file_obj.write(file_content)
    file_obj.close()


def make_keyphrase(word1, word2, message_len):
    # keyphrase = concantonated keywords times (integer of (length of message
    # divided by length of keyword) plus one)
    words = word1 + word2
    final_phrase = words * (int(message_len/len(words))+1)
    return final_phrase


# get user input
# encrypt or decrypt
choice = ""
while choice != "e" and choice != "d":
    choice = input("Encrypt or Decrypt message? e/d ")
    choice = choice.lower()

# keywords -> convert to uppercase
cipherword_1 = input("Enter your first cipher word: ")
cipherword_1 = cipherword_1.upper()
cipherword_2 = input("Enter your second cipher word: ")
cipherword_2 = cipherword_2.upper()

# encrypt
if choice == "e":
    # read in plaintext file
    message = file_read('A453_CA3_Task3_plaintext.txt')
    message_length = len(message)

    # generate keyphrase
    keyphrase = make_keyphrase(cipherword_1, cipherword_2, message_length)

    # loop through message
    for i in range(message_length):

        # if character is space, append to plaintext message
        if message[i] == " ":
            output = output + " "
        else:

            # determine alphabet index of message character and equivilent
            # keypharse character. increase each index by 1
            x = ALPHABET.index(message[i]) + 1
            y = ALPHABET.index(keyphrase[i]) + 1

            # add index values together to get cypher character index
            # handle values greater than 26 using modulo maths
            z = (x + y) % 26

            # append cypher character to encrypted message
            output = output + ALPHABET[z-1]

    # write out encripted file
    file_write('A453_CA3_Task3_encripted.txt', output)

# decrypt
else:
    # read in encripted file
    message = file_read('A453_CA3_Task3_encripted.txt')
    message_length = len(message)

    # generate keyphrase
    keyphrase = make_keyphrase(cipherword_1, cipherword_2, message_length)

    # loop through message
    for i in range(message_length):

        # if character is space, append to plaintext message
        if message[i] == " ":
            output = output + " "
        else:

            # determine alphabet index of message character and equivilent
            # keypharse character. increase each index by 1
            x = ALPHABET.index(message[i]) + 1
            y = ALPHABET.index(keyphrase[i]) + 1

            # add 26 to message index then subtract keyphrase index.
            # handle values greater than 26 using modulo maths
            z = ((x + 26) - y) % 26

            # append plaintext character to decrypted message
            output = output + ALPHABET[z-1]

    # write our plaintext file
    file_write('A453_CA3_Task3_decripted.txt', output)

print("Process complete")
