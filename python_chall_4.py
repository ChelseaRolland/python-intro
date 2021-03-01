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

#6.1: Check Name
def check_for_name(sentence, name):
    return name.lower() in sentence.lower()

#6.1: Check Name - Tests
print("Check Name 6.1: ", check_for_name("My name is Jamie", "Jamie"))
print("Check Name 6.2: ", check_for_name("My name is jamie", "Jamie"))
print("Check Name 6.3: ", check_for_name("My name is Samantha", "Jamie"))

#7.1 Every Other Letter
def every_other_letter(word):
    new_word = ""
    for i in range(0, len(word), 2):
        new_word += word[i]
    return new_word

#7.1 Every Other Letter - Tests
print("Every Other Letter 7.1: ",every_other_letter("Codecademy"))
print("Every Other Letter 7.2: ", every_other_letter("Hello world!"))
print("Every Other Letter 7.3: ", every_other_letter(""))

#8.1 Reverse
def reverse_string(word):
    new_word = ""
    for i in range(0, len(word)):
        new_word += word[-1 - i]
    return new_word

    #another way to solve this
    #reverse = ""
    #for i in range(len(word)-1, -1, -1):
        #reverse += word[i]
    #return reverse

#8.1 Reverse - Tests
print("Reverse String 8.1: ", reverse_string("Codecademy"))
print("Reverse String 8.2: ", reverse_string("Hello world!"))
print("Reverse String 8.2: ", reverse_string(""))

#9.1 Make Spoonerism
def make_spoonerism(word1, word2):
    #ex: Belly Jeans --> Jelly Beans
    return word2[0] + word1[1:] + " " + word1[0] + word2[1:]

#9.1 Make Spoonerism - Tests
print("Make Spoonerism 9.1: ", make_spoonerism("Codecademy", "Learn"))
print("Make Spoonerism 9.2: ", make_spoonerism("Hello", "world!"))
print("Make Spoonerism 9.3: ", make_spoonerism("a", "b"))

#10.1 Add Exclamation
def add_exclamation(word):
    new_word = word
    if len(word) < 20:
        for ex in range(len(word),20):
            new_word += "!"
        return new_word
    else:
        return word

#10.1 Add Exclamation - Tests
print("Add Exclamation 10.1: ", add_exclamation("Codecademy"))
print("Add Exclamation 10.2: ", add_exclamation("Codecademy is the best place to learn"))
