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

#2.1: Count X
def count_char_x(word, x):
    letter_count = 0
    for letter in word:
        if letter == x:
            letter_count += 1
    return letter_count
    #return word.count(x)

#2.1: Count X - Tests
print("Count X 2.1: ", count_char_x("mississippi", "s"))
print("Count X 2.2: ", count_char_x("mississippi", "m"))

#3.1: Count Multi X
def count_multi_char_x(word, x):
    splits = word.split(x)
    print(splits)
    return len(splits) - 1
    #return word.count(x)

#3.1: Count Multi X - Tests
print("Count Multi X 3.1: ", count_multi_char_x("mississippi", "iss"))
print("Count Multi X 3.2: ", count_multi_char_x("apple", "pp"))

#4.1: Substring Between
def substring_between_letters(word, start, end):
    first_index = word.find(start)
    last_index = word.find(end)
    if (first_index and last_index) != -1:
        # +1 so it will include the letters between the start and not the start
        return word[first_index + 1:last_index]
    else:
        return word

#4.1: Substring Between - Tests
print("Substring Between 4.1: ",substring_between_letters("apple", "p", "e"))
print("Substring Between 4.2: ",substring_between_letters("apple", "p", "c"))

#5.1 X Length
def x_length_words(sentence, x):
    sent_list = sentence.split()
    for word in sent_list:
        if len(word) < x:
            return False
    return True

#5.1 X Length - Tests
print(x_length_words("i like apples", 2))
print(x_length_words("he likes apples", 2))
