#Python Coding Challenges #4 with String Methods

#1.1: Count Letters
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def unique_english_letters(word):
    #counter
    unique_ltr = 0
    #empty array to hold unique values
    unique_char = []
    #Loop through word to see which characters matches letters
    for letter in word:
    #Look in letters to see if letter included if so then count it
        if letter in letters and letter not in unique_char:
            unique_ltr += 1
            unique_char.append(letter)
    #returning the # of unique characters inside
    #print("Unique Chararcters: ", unique_char)
    return unique_ltr

#1.1: Count Letters - Tests
print("Count Letters 1.1: ", unique_english_letters("mississippi"))
print("Count Letters 1.2: ", unique_english_letters("Apple"))
print("Count Letters 1.3: ", unique_english_letters("DudeExperience"))
