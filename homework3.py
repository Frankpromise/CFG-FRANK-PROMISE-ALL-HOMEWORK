"""
Create required phrase.
----------------------

You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you cab generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

NOTES:
    You can only generate the phrase if the frequency of unique characters in the characters string is equal or greater
    than frequency in the document string.

FOR EXAMPLE:
Test Case 1 - Returns False
    characters = "cbacba"
    phrase = "aabbccc"


    In this case you CANNOT create required phrase, because you are 1 character short!

IMPORTANT:
    The phrase you need to create can contain any characters including special characters,
    capital letter, numbers
    and spaces.

    You can always generate an empty string.

"""


def generate_phrase(characters, phrase):
    count = 0 # this count the number of characters that occur in the variable characters.
    # if the lenght of the character is less than the phrase, return false
    if len(characters) < len(phrase):
        return False
    
    # if the lenght of the phrase is 0 and the characters lenght is greater than 0
    # then we can create phrases. so we return true
    
    elif len(phrase) == 0 and len(characters) > 0:
        return True
    
    # otherwise, we can check for each letter or phrase that will occur in the characters
    # we can create phrase
    else:
        # loop o go through each word of phrase and characters 
        for i in phrase:
            for char in characters:
                # if the phrase letter matches with the characters letter
                if i==char:
                    # then increment the count variable
                    count+= 1
                    break # break the loop
                
            # if count is equal to the lenght of the phrase, it basically means we can get the letters
            # in the characters, sso we can return true
        if(count==len(phrase)):
            return True
        # otherwise return false
        else:
            return False
        





###################################################

#Test case 1 -- False

characters = "odeC stFir slrG"
phrase = "Code First Girls"

print(generate_phrase(characters, phrase))

###################################################

#Test case 2 -- False

characters = "A"
phrase = "a"

print(generate_phrase(characters, phrase))

###################################################

#Test case 3 -- True

characters = "odeC stFir slrG"
phrase = ""

print(generate_phrase(characters, phrase))

###################################################

#Test case 4 -- True

characters = "aheaollabbhb"
phrase = "hello"

print(generate_phrase(characters, phrase))






