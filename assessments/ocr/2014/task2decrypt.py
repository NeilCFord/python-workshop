# task2decrypt.py

ALPHABET = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
output = ""

message = "JRFUBWBSNLLKBQ"
keyword = "GCSE"

# keyphrase = keyword times (integer of (length of message divided by length of keyword) plus one)

keyphrase = keyword * (int(len(message)/len(keyword))+1)

for i in range(len(message)):

    # determine alphabet index of message character and equivilent keypharse character. increase each index by 1

    x = ALPHABET.index(message[i]) + 1
    y = ALPHABET.index(keyphrase[i]) + 1

    # add index values together to get cypher character index
    # handle values greater than 26 using modulo maths

    z = ((x + 26) - y) % 26

    # append cypher character to encrypted message

    output = output + ALPHABET[z-1]
        
print(output)
