#! python3

'''A453 Programming Project
CONTROLLED ASSESSMENT MATERIAL 3
September 2014 for June 2015 to June 2016

One simple encryption technique is the Caesar cipher. This involves taking
the letters of the alphabet and offsetting them by a fixed number of positions
to replace letters in the original message (plaintext) by the offset characters

For example, an offset of 5 gives the following:

  Original Alphabet:    ABCDEFGHIJKLMNOPQRSTUVWXYZ
  Offset by 5 gives:    FGHIJKLMNOPQRSTUVWXYZABCDE

  The message COMPUTING IS FUN
  becomes     HTRUZYNSL NX KZS

Analyse the requirements for this program and design, develop, test and
evaluate a program to enter, encrypt and decrypt messages. You must use a
high-level language in order to implement the Caesar cipher.'''

# import modules

# initialize variables

encryptedMessage = ""
decryptedMessage = ""

plainAlphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cypherAlphabet = "FGHIJKLMNOPQRSTUVWXYZABCDE"

# get user input
# encrypt or decrypt

choice = input("Encrypt or Decrypt message? e/d ")

# message -> convert to uppercase

message = input("Enter your message: ")
message = message.upper()

# encrypt
if choice == "e":

    # loop through message

    for x in range(len(message)):

        # if character is space, append to encrypted message

        if message[x] == " ":
            encryptedMessage = encryptedMessage + " "
        else:

            # else determine alphabet index and look up equivalent cypher
            # character.
            # append cypher character to encrypted message

            y = plainAlphabet.index(message[x])
            encryptedMessage = encryptedMessage + cypherAlphabet[y]

    result = encryptedMessage

else:
    # decrypt
    # loop through message

    for x in range(len(message)):
        # if character is space, append to plaintext message

        if message[x] == " ":
            decryptedMessage = decryptedMessage + " "
        else:

            # else determine  cypher alphabet index and look up equivalent
            # plaintext character.
            # append plaintext character to decrypted message

            y = cypherAlphabet.index(message[x])
            decryptedMessage = decryptedMessage + plainAlphabet[y]

        result = decryptedMessage

# print result.

print(result)
