#Python Coding Challenges #4 with String Methods

#1.1: Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
    #counter
    unique_ltr = 0
    #Loop through letter in letters to see which are in word
    for letter in letters:
    #Look in word to see if letter included if so then count it
        if letter in word:
            unique_ltr += 1
    #returning the # of unique characters inside
    #print("Unique Chararcters: ", unique_char)
    return unique_ltr

#1.1: Count Letters - Tests
print("Count Letters 1.1: ", unique_english_letters("mississippi"))
print("Count Letters 1.2: ", unique_english_letters("Apple"))
print("Count Letters 1.3: ", unique_english_letters("DudeExperience"))
