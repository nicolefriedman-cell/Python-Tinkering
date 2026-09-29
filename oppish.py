# oppish.py
# Converts an input string into it's "Oppish" version of itself
# Rule: consonents are appended with "op" while vowels are left alone
# NF 9/28/2026

print("Welcome to the oppish translator!")
phrase = str(input("Please enter a phrase to translate: "))

oppish = ""
vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']

for letter in phrase:
        if letter in vowels: # Filter out vowels
                oppish += letter
        elif (letter >= 'a' and letter <= 'z') or \
             (letter >= 'A' and letter <= 'Z'): # op-ify all ascii consonents 
                oppish += letter
                oppish += "op"
        else: # Arbitrarily leave non-letters alone
                oppish += letter

print(oppish)