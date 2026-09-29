# memes.py
# genuinely just messing around
# turns any input string into a mocking version of itself
# NF 9/28/2026

phrase = str(input("Please enter a word to meme-ify: "))

memeified = ""
for index, letter in enumerate(phrase):
        if index % 2 == 0: # All even-indexed letters are lowercase
                memeified += phrase[index].lower()
        else:              # And all odd-indexed letters are uppercase
                memeified += phrase[index].upper()


print(memeified)
