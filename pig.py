# pig.py
# Converts an input string into it's Pig Latin version of itself
# NF 9/28/2026

import string

print("Welcome to the pig latin translator!")
phrase = str(input("Please enter a phrase to translate: "))

words = phrase.split()

# Preliminaries setting up letter classifications
pigLatin = ""
lowercase = {chr(i) for i in range(ord('a'), ord('z') + 1)}
uppercase = {chr(i) for i in range(ord('A'), ord('Z') + 1)}
alphabet = lowercase | uppercase 
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
consonents = alphabet - set(vowels)

# "Translate each word"
for word in words:
        if word[0] in vowels:
                pigLatin += word + "way "
        else:  # Handle leading consonents
                index = 0
                while index < len(word) and word[index] in consonents :
                        index += 1 # Count the number of consonents
                
                if word[0] in uppercase:
                        if word.isupper(): # If full word is upper, keep upper
                                pigLatin += word[index:].upper() + \
                                            word[:index].upper() + "AY "
                        else: # If leading caps, make sure new front is caps
                                wordLength = len(word)
                                if index > 1:
                                        pigLatin += word[index].upper() + \
                                                word[(index + 1):] + \
                                                word[0].lower() + \
                                                word[1:index] + "ay "
                                else: 
                                        pigLatin += word[index].upper() + \
                                                word[(index + 1):] +\
                                                word[0].lower() + "ay "
                else:
                        pigLatin += word[index:] + word[:index] + "ay "

print(pigLatin)