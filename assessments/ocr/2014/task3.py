# import modules
import ipdb
# initialize variables

alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
output = ""

# get user input
# encrypt or decrypt

choice = input("Encrypt or Decrypt message? e/d ")

# message -> convert to uppercase

#message = input("Enter your message: ")
#message = message.replace(' ','')
#message = message.upper()

# keyword -> convert to uppercase
keyword = input("Enter your keyword: ")
keyword = keyword.upper()

# keyphrase = keyword times (integer of (length of message divided by length of keyword) plus one)

keyphrase = keyword * (int(len(message)/len(keyword))+1)

# encrypt
if choice == "e":
    
    # loop through message
    # ipdb.set_trace()
    try:
        for i in range(len(message)):

            # determine alphabet index of message character and equivilent keypharse character. increase each index by 1

            x = alphabet.index(message[i]) + 1
            y = alphabet.index(keyphrase[i]) + 1
            print(x, y)

            # add index values together to get cypher character index

            z = x + y

            # handle values greater than 26 (1 - 25)

            if z > 26:
                z = z - 26

            # append cypher character to encrypted message

            output = output + alphabet[z-1]
    except:
        ipdb.set_trace()
        
print(output)
    

                           
# decrypt
    # loop through message
    # if character is space, append to plaintext message
    # else determine  cypher alphabet index and look up equivalent plaintext character.
    # append plaintext character to decrypted message

# print result.