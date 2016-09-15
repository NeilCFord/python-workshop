# import modules

# initialize variables

# define functions
    # read in file, replace newline characters, convert to uppercase and return

    # write out converted text to file

    # keyphrase = concantonated keywords times (integer of (length of message
    # divided by length of keyword) plus one)

# get user input
# encrypt or decrypt
# keywords -> convert to uppercase

# keyphrase = keyword times (integer of (length of message divided by length
# of keyword) plus one)

# encrypt
    # read in plaintext file
    # generate keyphrase
    # loop through message
        # if character is space, append to plaintext message
        # determine alphabet index of message character and equivilent keyphrase
        # character. increase each index by 1
        # add index values together to get cypher character index
        # handle values greater than 26 (1 - 26)
        # append cypher character to encrypted message
    # write out encripted file



# decrypt
    # read in encripted file
    # generate keyphrase
    # loop through message
        # if character is space, append to plaintext message
        # determine alphabet index of message character and equivilent
        # keypharse character. increase each index by 1
        # add 26 to message index then subtract keyphrase index.
        # handle values greater than 26 using modulo maths
        # append plaintext character to decrypted message
    # write our plaintext file
