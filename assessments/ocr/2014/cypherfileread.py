# initialize variables
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
output = ""

# read in plaintext file
fileObj = open('A453_CA3_Task3_plaintext.txt', 'r')
message = fileObj.read()
fileObj.close()

# remove newline characters and conver to uppercase
#message = message.replace(' ','')
message = message.replace('\n', '')
message = message.upper()
messageLength = len(message)

# print message and length for debugging/testing
print(message)
print(messageLength)

keyphrase = "RUBBERCHICKEN" * (int(messageLength / len("RUBBERCHICKEN")) +1)

print(keyphrase)

for i in range(len(message)):

    if message[i] == " ":
        output = output + " "

    else:

        # determine alphabet index of message character and equivilent keypharse
        # character. Increase each index by 1 (because we are used to the
        # alphabet having 26 letters)

        x = alphabet.index(message[i]) + 1
        y = alphabet.index(keyphrase[i]) + 1

        # add index values together to get cipher character index

        z = x + y

        # handle values greater than 26 (1 - 26)

        if z > 26:
            z = z - 26

        # append cipher character to encrypted message

        output = output + alphabet[z-1]

print(output)
