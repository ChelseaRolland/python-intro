import csv
import json

#Math and Calculations
print(5+2)
print(9-8)
print(7*11)
print(8/11)
print(28 % 3)
print(7**4)


#Starting with basic strings and concatenation
print("Hello there you")
my_name = "Chelsea Rolland"
print("Hello there " + my_name)
string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."
num = 17

print(string1 + string2 + string3 + string4 + string5 + string6 + str(num))

#operator equals notation
total_price = 0
new_sneakers = 50.00
total_price += new_sneakers
nice_sweater = 39.00
fun_books = 20.00
total_price += nice_sweater + fun_books
print("The total price is", total_price)

#Multi level strings
poem = """ JANUARY
Delightful display
Snowdrops bow their pure white heads
To the sun's glory.
"""
print(poem)

#Recap
my_age = 27
half_my_age = 16.5
greeting = "Hello there fellow dude"
name = "Chelsea"
greeting_with_name = greeting + ", " + name
print(greeting_with_name)

#Boolean Expressions
print((5 * 2) - 1 == 8 + 1) #True
print(13 - 6 != (3 * 2) + 1) #False
print(3 * (2 - 1) == 4 - 1) #True

my_baby_bool = "true"
print(type(my_baby_bool)) #string

my_baby_bool_two = True
print(type(my_baby_bool_two)) #boolean

#If statements
# Enter a user name here, make sure to make it a string
#user_name = "Davature"
#user_name = "Dave"
user_name = "angela_catlady_87"

if user_name == "Dave":
  print("Get off my computer Dave!")

if user_name == "angela_catlady_87":
  print("I know it is you, Dave! Go away!")

#Boolean Operator: AND
statement_one = (2 + 2 + 2 >= 6) and (-1 * -1 < 0) #False
print(statement_one)

statement_two = (4 * 2 <= 8) and (7 - 1 == 6) #True
print(statement_two)

credits = 120
gpa = 3.4

if credits >= 120 and gpa >= 2.0:
  print("You meet the requirements to graduate!")

#Boolean Operator: OR
statement_one = (2 - 1 > 3) or (-5 * 2 == -10) #True
print(statement_one)

statement_two = (9 + 5 <= 15) or (7 != 4 + 3) #True
print(statement_two)

credits = 118
gpa = 2.0

if credits >= 120 or gpa >= 2.0:
  print("You have met at least one of the requirements.")

#Boolean Operator: NOT
statement_one = not (4 + 5 <= 9)
print(statement_one)

statement_two = not (8 * 2) != 20 - 4
print(statement_one)

credits = 120
gpa = 1.8

if not credits >= 120:
  print("You do not have enough credits to graduate.")

if not gpa >= 2.0:
  print("Your GPA is not high enough to graduate.")

if not (credits >= 120) and not (gpa >= 2.0):
  print("You do not meet either requirement to graduate!")

#else statement
credits = 120
gpa = 1.9

if (credits >= 120) and (gpa >= 2.0):
  print("You meet the requirements to graduate!")
else:
  print("You do not meet the requirements to graduate.")

#else if statements
grade = 86

if grade >= 90:
  print("A")
elif grade >= 80:
    print("B")
elif grade >= 70:
    print("C")
elif grade >= 60:
    print("D")
else:
    print("F")

#Conditional Statement Review
print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

weight = 185
planet = 3

# Write an if statement below:
if planet == 1:
  print("Your planet is Venus")
  weight *= 0.91
elif planet == 2:
  print("You planet is Mars")
  weight *= 0.38
elif planet == 3:
  print("Your planet is Jupiter")
  weight *= 2.34
elif planet == 4:
  print("Your planet is Saturn")
  weight *= 1.06
elif planet == 5:
  print("Your planet is Uranus")
  weight *= 0.92
elif planet == 6:
  print("Your planet is Neptune")
  weight *= 1.19
else:
    print("This is not the planet you are looking for")

print("Your Weight", weight)

#Functions
def feb_favorite_game():
  print("So far my favorite game is Little Nightmares 2")

feb_favorite_game()

def new_games(game1, specs = "PS5"):
  print(game1 + " will come out on the " + specs + ".")

new_games("Spiderman Miles Morales")
new_games("Little Nightmares 2", "PS4")

def num_squared(x,y):
  x_squared = x ** 2
  y_sqared = y ** 2
  return x_squared, y_sqared

def calculate_age(current_year, birth_year):
  age = current_year - birth_year
  return age
  
#print(current_year) #doesn't work due to scope
#print(age) #doesn't work due to scope

def repeat_stuff(stuff, num_repeats = 10):
  return stuff * num_repeats

print(repeat_stuff("Row ", 3))
print(repeat_stuff("Row ", 3) + "Your Boat. ")
lyrics = repeat_stuff("Row ", 3) + "Your Boat. "
print(lyrics)
song = repeat_stuff(lyrics)
print(song)

#Lists
heights = [61, 66, 85, 45, 65]
little_nightmares_two_char = ["Mono", "Six", 1, 6]
naruto_shippudden_char_ages = [["Naruto", 16], ["Sasuke", 17], ["Shikamaru", 16]]

#Lists zip method
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
dogs_names = ['Elphonse', 'Dr. Doggy DDS', 'Carter', 'Ralph']

names_and_dogs_names = zip(names, dogs_names)
list_of_names_and_dogs_names = list(names_and_dogs_names)
print(list_of_names_and_dogs_names)

#Empty lists & Append
empty_list = []
empty_list.append(1)
empty_list.append(2)
empty_list.append(3)
empty_list.append("Mono")
empty_list.append("Six")
print(empty_list)

#Adding more than 1 item to a list at a time
orders = ['daisy', 'buttercup', 'snapdragon', 'gardenia', 'lily']
new_orders = orders + ["lilac", "iris"]
broken_prices = [5, 3, 4, 5, 4] + [4]
print(new_orders)
print(broken_prices)

#Ranges
list1 = range(9)  #defalut starting is 0, excludes the input
print(list(list1))

list2 = range(5,14) #cutomize the starting point, and still excludes the 2nd input
print(list(list2))

list3 = range(1,100,10) #3rd input is the # it will skip to the next output
print(list(list3))

#list4 = range(100,10) #must have 0 if doing all 3 inputs so it will know where to start
list4 = range(0,100,10)
print(list(list4))

#List 1 Review
first_names = ["Ainsley", "Ben", "Chani", "Depak"]
age = []
age.append(42)
all_ages = [32, 41, 29] + age
name_and_age = zip(first_names, all_ages)
ids = range(4)
all_customers = zip(list(name_and_age), ids)
  #Answer: [(('Ainsley', 32), 0), (('Ben', 41), 1), (('Chani', 29), 2), (('Depak', 42), 3)]
all_customers = zip(ids, first_names, all_ages)
  #Answer: [(0, 'Ainsley', 32), (1, 'Ben', 41), (2, 'Chani', 29), (3, 'Depak', 42)]
print(list(all_customers))

#Operations on Lists

#Length
print(len(first_names))

list1 = range(2, 20, 3)
list1_len = len(list1)
print(list1_len)

#Selecting Elements #1
employees = ['Michael', 'Dwight', 'Jim', 'Pam', 'Ryan', 'Andy', 'Robert']
index4 = employees[4]
print(len(employees))
print(employees[6])

#Selecting Elements #2
shopping_list = ['eggs', 'butter', 'milk', 'cucumbers', 'juice', 'cereal']
print(len(shopping_list))
last_element = shopping_list[-1]
element5 = shopping_list[5]
print(last_element, element5)

#Slicing
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
beginning = suitcase[0:2]  # ['shirt','shirt']
beginning = suitcase[0:4]  # ['shirt', 'shirt', 'pants', 'pants']
print(beginning)
middle = suitcase[2:4]  # ['pants','pants']
print(middle)

#Slicing 2
suitcase = ['shirt', 'shirt', 'pants', 'pants', 'pajamas', 'books']
start = suitcase[:3]  # ['shirt','shirt','pants']
end = suitcase[4:]  # ['pajamas','books']

#Counting
votes = ['Jake', 'Jake', 'Laurie', 'Laurie', 'Laurie', 'Jake', 'Jake', 'Jake', 'Laurie', 'Cassie',
'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie', 'Cassie', 'Jake', 'Jake', 'Cassie', 'Laurie']
jake_votes = votes.count("Jake")
print(jake_votes)

#Sort
### Exercise 1 & 2 ###
addresses = ['221 B Baker St.', '42 Wallaby Way', '12 Grimmauld Place','742 Evergreen Terrace', '1600 Pennsylvania Ave', '10 Downing St.']
# Sort addresses here:
addresses.sort()
print(addresses)
### Exercise 3 ###
names = ['Ron', 'Hermione', 'Harry', 'Albus', 'Sirius']
names.sort()
print(names)
### Exercise 4 ###
cities = ['London', 'Paris', 'Rome', 'Los Angeles', 'New York']
sorted_cities = cities.sort()
print(sorted_cities)

#Sorting 2
games = ['Portal', 'Minecraft', 'Pacman', 'Tetris', 'The Sims', 'Pokemon']
games_sorted = sorted(games)
print(games_sorted)

#Tuples --> immutable aka can't be changed and when you have data in a specific order that you do not want to change
my_info = ("Chelsea", 27, "Programmer")
print(my_info)
print(my_info[0])
print(my_info[1])
print(my_info[-1])
#my_info[0] = "Coven" #Can't work due to immutable of portions

#Unpacking a Tuple
name, age, occupation = my_info
print(name)
print(age)
print(occupation)

one_element_tuple = (4)
print(one_element_tuple)
one_element_tuple = (4,)
print(one_element_tuple)

#Loops
dog_breeds = ['french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']

for breed in dog_breeds:
  print("beginning of loops - Dog Breeds: ",breed)

board_games = ['Settlers of Catan', 'Carcassone','Power Grid', 'Agricola', 'Scrabble']

sport_games = ['football', 'football - American','hockey', 'baseball', 'cricket']

for game in board_games:
  print("Board Games: ",game)

for sport in sport_games:
  print("Sports Games: ",sport)

promise = "I will not chew gum in class"

for i in range(5):
  print(promise)

students_period_A = ["Alex", "Briana", "Cheri", "Daniele"]
students_period_B = ["Dora", "Minerva", "Alexa", "Obie"]

for student in students_period_A:  # Alex, Briana, Cheri, Daniele
  students_period_B.append(student)
  print(student)

#Breaks
dog_breeds_available_for_adoption = [
    'french_bulldog', 'dalmatian', 'shihtzu', 'poodle', 'collie']
dog_breed_I_want = 'dalmatian'

for breed in dog_breeds_available_for_adoption:
  print(breed)
  if breed == dog_breed_I_want:
    print("They have the dog I want!")
    break

#Continue
ages = [12, 38, 34, 26, 21, 19, 67, 41, 17]
for age in ages:
  if age < 21:
    continue
  print(age)

#While Loops
all_students = ["Alex", "Briana", "Cheri", "Daniele","Dora", "Minerva", "Alexa", "Obie", "Arius", "Loki"]
students_in_poetry = []

while len(students_in_poetry) < 6:
  student = all_students.pop()
  students_in_poetry.append(student)

print(students_in_poetry)

#Nested Loops
sales_data = [[12, 17, 22], [2, 10, 3], [5, 12, 13]]
scoops_sold = 0
for sale in sales_data:
  print(sale)
  for location in sale:
    scoops_sold += location

  print(scoops_sold)

#List Comprehensions --> Makes new lists out of existing lists
heights = [161, 164, 156, 144, 158, 170, 163, 163, 157]
can_ride_coaster = [height for height in heights if height > 161]
print(can_ride_coaster)

celsius = [0, 10, 15, 32, -5, 27, 3]
fahrenheit = [degree * 9/5 + 32 for degree in celsius]
print(fahrenheit)

#Loops Review
single_digits = list(range(10))
print("Single Digits Lists: ",single_digits)

squares = []
cubes = []

for num in single_digits:
  print(num)
  squares.append(num**2)
  cubes.append(num**3)

print("Squares: ",squares)
print("Cubes: ",cubes)

i = 1
while i <= 10:
  print(i)
  i += 1

for i in range(3):
  print(i)

desired_lists = [-1,0,1,2,3]
copied_desired_list = [i - 1 for i in range(5)]
print(copied_desired_list)

#Strings
my_name = "Chelsea"
first_initial = my_name[0]
print("First Initial: ", first_initial)

#Slicing String
first_name = "Rodrigo"
last_name = "Villanueva"

new_account = last_name[:5]
print("Slicing Strings 1.1: ", new_account)
temp_password = last_name[2:6]
print("Slicing Strings 1.2: ", temp_password)

#Concatenating Strings
def account_generator(first_name, last_name):
	return first_name[:3] + last_name[:3]

first_name = "Julie"
last_name = "Blevins"
new_account = account_generator(first_name, last_name)

print("String Concatenation 1.1: ", new_account)

#Addition String Slicing (Length of string)
first_name = "Reiko"
last_name = "Matsuki"

def password_generator(first_name, last_name):
    	return first_name[len(first_name) - 3:] + last_name[len(last_name) - 3:]

temp_password = password_generator(first_name,last_name)

print("Slicing via Length of Strings: ", temp_password)

#Negative Indices
company_motto = "Copeland's Corporate Company helps you capably cope with the constant cacophony of daily life"
second_to_last = company_motto[-2]
print("Negative Indicies 1.1:",second_to_last)
final_word = company_motto[-4:]
print("Negative Indicies 1.2: ",final_word)

#Strings are Immutable (Unchangeable)
first_name = "Bob"
last_name = "Daily"

#first_name[0] = "R" --> Doesn't work due to immutable property
fixed_first_name = "R" + first_name[1:] #changing the 1st letter of a word
print("Fixed First Name with Slicing: ", fixed_first_name)

#Escape Characters
password = "theycallme\"crazy\"91"
print("Escape Characters: ", password)

#Iterating through Strings
def get_length(word):
	counter = 0
	for letter in word:
		counter += 1
	return counter

print("Iterating through Strings 1.1: ", get_length("love"))
print("Iterating through Strings 1.2: ", get_length("baconator"))
print("Iterating through Strings 1.3: ", get_length("spider-man"))

#Strings and Conditionals pt.#1
def letter_check(word, letter):
    counter = 0
    for char in word:
        if char == letter:
            counter += 1
    if counter > 0:
        return True
    else:
        return False

print("String and Conditionals 1.1: ",letter_check("strawberry", "a"))

#String and Conditionals pt.#2
def contains(big_string, little_string):
    return little_string in big_string

print("Contains 1.1: ", contains("watermelon", "melon"))
print("Contains 1.2: ", contains("watermelon", "berry"))

def common_letters(string_one, string_two):
    common = []
    for letter in string_one:
        if (letter in string_two) and not (letter in common):
            common.append(letter)
    return common

print("Common Letters 1.1: ", common_letters("banana", "cream"))
print("Common Letters 1.2: ", common_letters("manhattan", "san francisco"))

#String Methods
poem_title = "spring storm"
poem_author = "William Carlos Williams"

poem_title_fixed = poem_title.title();
print(poem_title)
print("String Methods -  Title: ", poem_title_fixed)

poem_author_fixed = poem_author.upper()
print(poem_author)
print("String Methods - Upper: ", poem_author_fixed)

#Splitting Strings
line_one = "The sky has given over"
line_one_words = line_one.split()
print("String Method - Split: ", line_one_words)

authors = "Audre Lorde,Gabriela Mistral,Jean Toomer,An Qi,Walt Whitman,Shel Silverstein,Carmen Boullosa,Kamala Suraiyya,Langston Hughes,Adrienne Rich,Nikki Giovanni"

author_names = authors.split(",")
print("String Methods - Split Delimiters 1.1: ", author_names)

author_last_names = []
for name in author_names:
    author_last_names.append(name.split()[-1])

print("String Methods - Split Delimiters 1.2: ", author_last_names)

spring_storm_text = \
"""The sky has given over 
its bitterness. 
Out of the dark change 
all day long 
rain falls and falls 
as if it would never end. 
Still the snow keeps 
its hold on the ground. 
But water, water 
from a thousand runnels! 
It collects swiftly, 
dappled with black 
cuts a way for itself 
through green ice in the gutters. 
Drop after drop it falls 
from the withered grass-stems 
of the overhanging embankment."""

spring_storm_lines = spring_storm_text.split("\n")
print("String Splitting 3: ",spring_storm_lines)

#Joining Strings
reapers_line_one_words = ["Black", "reapers", "with", "the", "sound", "of", "steel", "on", "stones"]

reapers_line_one = " ".join(reapers_line_one_words)
print("Joining: ", reapers_line_one)

winter_trees_lines = ['All the complicated details', 'of the attiring and', 'the disattiring are completed!', 'A liquid moon', 'moves gently among', 'the long branches.', 'Thus having prepared their buds', 'against a sure winter', 'the wise trees', 'stand sleeping in the cold.']

winter_trees_full = "\n".join(winter_trees_lines)
print("Joining String 2: ", winter_trees_full)

#.strip() method
love_maybe_lines = ['Always    ', '     in the middle of our bloodiest battles  ', 'you lay down your arms', '           like flowering mines    ','\n' ,'   to conquer me home.    ']

love_maybe_lines_stripped = []
for line in love_maybe_lines:
    love_maybe_lines_stripped.append(line.strip())
print(".strip method 1.1: ", love_maybe_lines_stripped)

love_maybe_full = "\n".join(love_maybe_lines_stripped)
print(".strip method 1.2: ", love_maybe_full)

#Replace
toomer_bio = \
    """
Nathan Pinchback Tomer, who adopted the name Jean Tomer early in his literary career, was born in Washington, D.C. in 1894. Jean is the son of Nathan Tomer was a mixed-race freedman, born into slavery in 1839 in Chatham County, North Carolina. Jean Tomer is most well known for his first book Cane, which vividly portrays the life of African-Americans in southern farmlands.
"""

toomer_bio_fixed = toomer_bio.replace("Tomer","Toomer")
print("replace method: ", toomer_bio_fixed)

#.find() method
god_wills_it_line_one = "The very earth will disown you"

disown_placement = god_wills_it_line_one.find("disown")
print("find() method: ", disown_placement)

#.format() method
def poem_title_card(title, poet):
    return "The poem \"{}\" is written by {}.".format(title, poet)

print("format() method: ", poem_title_card("I Hear America Singing", "Walt Whitman"))

def poem_description(publishing_date, author, title, original_work):
    poem_desc = "The poem {title} by {author} was originally published in {original_work} in {publishing_date}.".format(publishing_date = publishing_date, author = author, title = title, original_work = original_work)
    return poem_desc


my_beard_description = poem_description(
    author="Shel Silverstein", title="My Beard", original_work="Where the Sidewalk Ends", publishing_date="1974")

print("format() method 2: ", my_beard_description)

user_name = "::::::::Eloise :::::::::::"
user_name_fixed = user_name.strip(":").strip()
print("Username: ", user_name)
print("Username Fixed: ", user_name_fixed)

#Dictionaries
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print("Dictionaries 1.1: ", sensors)
print("Dictionaries 1.2: ", num_cameras)

#Creating Dictionaries
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
print("Dictionaries: 1.3: ", translations)

#Only Numbers, Strings, and Tuples can be keys since they are immuatable; values can be any data type
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}

#Empty Dictionary
my_empty_dictionary = {}

#Adding a key to Dictionaries
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print("Adding Keys to Dictionaries: ", animals_in_zoo)

#Adding Mutliple Keys
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print("Adding Multiple Keys to Dictionary: ", user_ids)

#Overwritting Values in Dictionaries
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck", "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}

oscar_winners["Supporting Actress"] = "Viola Davis"
oscar_winners["Best Picture"] = "Moonlight"

print("Overwritting Values: ", oscar_winners)

#List Comprehensions to Dictionaries
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks }
print("List Comprehension with Dictionaries: ", drinks_to_caffeine)

#Creating Dictionaries Recap
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print("Plays Dictionary: ", plays)

plays["Purple Haze"] = 1
plays["Respect"] = 94

library = {"The Best Songs": plays, "Sunday Feelings": {}}
print("Library Dictionary: ", library)

#Using Dictionaries

#Getting a key
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

print("Get Dictionary Key Value 1.1: ",zodiac_elements["earth"])
print("Get Dictionary Key Value 1.2: ",zodiac_elements["fire"])
print("Get Dictionary Key Value 1.3: ",zodiac_elements["water"])
print("Get Dictionary Key Value 1.4: ",zodiac_elements["air"])

#Get an Invalid Key
#print(zodiac_elements["energy"]) --> Doesn't work
#Check if does
key_check = "energy"
if key_check in zodiac_elements: #this will be false so it will never access the invalid key
    print(zodiac_elements["energy"])
zodiac_elements["energy"] = "Not a Zodiac element"
print(zodiac_elements["energy"])

#Try/Expect --> similar to try/catch block in java and javascript
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120}
caffeine_level["matcha"] = 30
try:
    print(caffeine_level["matcha"])
except KeyError:
    print("Unknown Caffeine Level")

#.get() for Dictionaries
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

tc_id = user_ids.get("teraCoder", 100000)
print("get() method with Dicitonaries 1.1: ", tc_id)
stack_id = user_ids.get("superStackSmash", 100000)
print("get() method with Dicitonaries 1.2: ", stack_id)

#Deleting a Key --> .pop() for Dictionaries
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

health_points += available_items.pop("stamina grains", 0)
print("Games - HP 1.1: ", health_points)
health_points += available_items.pop("power stew", 0)
print("Games - HP 1.2: ", health_points)
health_points += available_items.pop("mystic bread", 0)
print("Games - HP 1.3: ", health_points)
print("Game - Remaining Items: ", available_items)
print("Game - Current HP: ", health_points)

#Get all Keys
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()
print("dict_keys - .keys() 1.1: ", users)
print("dict_keys - .keys() 1.1: ", lessons)

#Get all Values --> .values()
total_exercises = 0
for lesson in num_exercises.values():
    total_exercises += lesson

print("dict_values - .values()", total_exercises)

#Get all Items .items() --> will return a tuple
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

for position,percent in pct_women_in_occupation.items():
    print("Women make up " + str(percent) + " percent of " + position + "s.")
    print("Women make up {} percent of {}s.".format(percent, position))

#Review Using Dictionaries
tarot = {1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}
spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for num, card in spread.items():
    print("Your {} is the {} card.".format(num, card))

#Files
with open("welcome.txt") as text_file:
    text_data = text_file.read()

print("Text Data - Files 1.1: ", text_data)

#Iterating through multiple lines
with open("song_lyrics.txt") as song_lyrics:
    for line in song_lyrics.readlines():
        print(line)

#Reading a Line
with open("song_lyrics.txt") as song:
    first_line = song.readline()
    second_line = song.readline()
    print("1st Line: ", first_line)
    print("2nd Line: ", second_line)

#Writing a File
with open("generated_file.txt", "w") as gen_file:
    gen_file.write("Woah this is really cool to test out! \n")

#Appending a File
with open("generated_file.txt", "a") as gen_file:
    gen_file.write("So I am adding to this with using the appending option \n")

#Classic file manipulation with .close() --> its best to use with
gen_file = open("generated_file.txt", "a")
gen_file.write("Testing out the old way of doing things before the with keyword \n")
gen_file.close()

#CSV --> Comma Separated Values
#Opening and Reading users.csv
with open("users.csv") as users_file:
    print(users_file.read())

#Read a CSV File
with open("users.csv", newline="") as users_csv:
    list_of_email_addresses = []
    #Converts the lines in csv file to dictionaries
    user_reader = csv.DictReader(users_csv)
    for user in user_reader:
        list_of_email_addresses.append(user["Email"])
    print(list_of_email_addresses)

#Reading a different type of CSV file
with open("addresses.csv", newline="") as addresses_csv:
    addresses_reader = csv.DictReader(addresses_csv, delimiter = ";")
    for row in addresses_reader:
        print(row["Name"])
        print(row["Address"])
        #print(row["Address"].strip("\n")) --> didn't work will see why
        print(row["Telephone"])

#Writing a CSV file
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

with open("logger.csv", "w") as logger_csv:
    log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
    log_writer.writeheader()
    for row in access_log:
        log_writer.writerow(row)

#Reading JSON
with open("message.json") as message_json:
    message_reader = json.load(message_json)
    print(message_reader["age"])
    print(message_reader["eyeColor"])
    print(message_reader["balance"])
    print(message_reader["name"])

#Writing a JSON file
data_payload = [
    {'interesting message': 'What is JSON? A web application\'s little pile of secrets.', 'follow up': 'But enough talk!'}
]

with open("data_ex_1.json", "w") as json_file:
    json.dump(data_payload, json_file)

#Classes
print(type(5))  #<class "int">
my_dict = {"name": "Chelsea", "favorite colors": ["vermillion", "jade green", "teal"]}
print(type(my_dict))    #<class "dict">
my_list = ["random", 4, "dailies", 110]
print(type(my_list))    #<class "list">

#structure of class, for now leave the pass as we are intentially leaving class blank for now
class Facade:
    pass

#Instantiation
facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)    #<class "__main__.Facade">

#Class Variables aka: properties/fields
class Grade:
    minimum_passing = 65

my_grade = Grade()
print(my_grade.minimum_passing) #65

#Methods
class Rules:
    def washing_brushes(self):
        return "Point bristles towards the basin while washing your brushes."

class Circle:
    pi = 3.14
    def area(self, radius):
        return self.pi * radius ** 2

#Creating the Cirlce object
circle = Circle()
#Find the radius 1st

#1 
pizza_area = circle.area(12 / 2)
print("Pizza Area: ", pizza_area)

#2
teaching_table_area = circle.area(36 / 2)
print("Teaching Table Area: ", teaching_table_area)

#3
round_room_area = circle.area(11460 / 2)
print("Round Room Area: ", round_room_area)

#Constructors
class Cylinder:
    def __init__(self, height, radius):
        print("Your circle's diameter is {}, based on the radius: {}".format((radius * 2), radius))
        self.height = height
        self.radius = radius

    pi = 3.14
        
    def surface_area(self):
        return 2 * self.pi * self.radius * (self.height + self.radius)
    
    def volume(self):
        return self.pi * self.height * (self.radius ** 2)

cyclinder_1 = Cylinder(height = 13, radius = 33)
print(cyclinder_1.surface_area())
print(cyclinder_1.volume())

#Instance Variables
class Store:
    pass

alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

#Attribute Functions
can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for element in can_we_count_it:
    if hasattr(element, "count"):
        print(str(type(element)) + " has the count attribute!")
    else:
        print(str(type(element)) + " does not have the count attribute :(")

#Self
class Circle:
    pi = 3.14
    def __init__(self, diameter):
        print("Creating circle with diameter {d}".format(d=diameter))
        self.radius = diameter / 2

    def __repr__(self):
        return "Circle with radius {}".format(self.radius)

    def circumference(self):
        return 2 * self.pi * self.radius

medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print("Circumference for Medium Pizza: ", medium_pizza.circumference())
print("Circumference for Teaching Table: ", teaching_table.circumference())
print("Circumference for Round Room: ", round_room.circumference())

#dir()
print("dir(5): ", dir(5))
def this_function_is_an_object(tech_field):
    return "{} is a new exciting and growing industry in tech".format(tech_field)

print(this_function_is_an_object("Extended Reality"))
print(this_function_is_an_object("Artifical Intelligence"))
print(this_function_is_an_object("Internet of Things (IoT)"))

#Calling dir() on function itself
print(dir(this_function_is_an_object))

#String Representation
print("Medium Pizza: ", medium_pizza)
print("Teaching Table: ", teaching_table)
print("Round Room: ", round_room)

#Review of OOP with Python
class Student:
    attendence = {}
    def __init__(self, name, year):
        self.name = name
        self.year = year
        self.grades = []

    def __repr__(self):
        return self.name

    def add_grade(self, grade):
        if type(grade) is Grade:
            self.grades.append(grade)
    
    def get_average(self):
        sum = 0
        for grade in self.grades:
            sum += grade.score
        return sum / len(self.grades)

class Grade:
    minimum_passing = 65
    def __init__(self, score):
        self.score = score
    
    def __repr__(self):
        return self.score
    
    def is_passing(self):
        return self.score > self.minimum_passing

roger = Student("Roger van der Weyden", 10)
roger.attendence = {
    "01-05-2021": True,
    "01-06-2021": False,
    "01-07-2021": True,
    "01-08-2021": True
}
sandro = Student("Sandro Botticelli", 12)
sandro.attendence = {
    "01-05-2021": True,
    "01-06-2021": False,
    "01-07-2021": True,
    "01-08-2021": False
}
pieter = Student("Pieter Bruegel the Elder", 8)
pieter.attendence = {
    "01-05-2021": False,
    "01-06-2021": False,
    "01-07-2021": True,
    "01-08-2021": True
}

new_grade = Grade(100)
pieter.add_grade(new_grade)
pieter.add_grade(Grade(95))
pieter.add_grade(Grade(80))
pieter.add_grade(Grade(75))
print("isPassing(): ", new_grade.is_passing())
print("get_average(): ", pieter.get_average())

#Inheritance with Python
class Bin:
    pass

class RecyclingBin(Bin):
    pass

#Exceptions
# Define your exception here:
class OutOfStock(Exception):
    "This item is out of stock!"

# Update the class below to raise OutOfStock
class CandleShop:
    name = "Here's a Hot Tip: Buy Drip Candles"

    def __init__(self, stock):
        self.stock = stock

    def buy(self, color):
        if self.stock[color] < 1:
            raise OutOfStock
        else:
            self.stock[color] = self.stock[color] - 1

candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

# This should raise OutOfStock: It does
#candle_shop.buy('green')

#inheritance --> overriding methods
class Message:
    def __init__(self, sender, recipient, text):
        self.sender = sender
        self.recipient = recipient
        self.text = text

class User:
    def __init__(self, username):
        self.username = username
    
    def edit_message(self, message, new_text):
        if message.sender == self.username:
            message.text = new_text

class Admin(User):
    def edit_message(self, message, new_text):
        message.text = new_text

#super()
class PotatoSalad:
    def __init__(self, potatoes, celery, onions):
        self.potatoes = potatoes
        self.celery = celery
        self.onions = onions

class SpecialPotatoSalad(PotatoSalad):
    def __init__(self, potatoes, celery, onions):
        super().__init__(potatoes, celery, onions)
        self.paprika = 40

#Interfaces
class InsurancePolicy:
    def __init__(self, price_of_item):
        self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
    def __init__(self, price_of_item):
        super().__init__(price_of_item)
    
    def get_rate(self):
        return .001 * self.price_of_insured_item

class HomeInsurance(InsurancePolicy):
    def __init__(self, price_of_item):
        super().__init__(price_of_item)
    
    def get_rate(self):
        return .00005 * self.price_of_insured_item

#Polymorphism
a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

#Polymorphism: same name for method, however doing different actions depending on type of data
print(len(a_list))
print(len(a_dict))
print(len(a_string))

#Dunder Methods
class Atom:
    def __init__(self, label):
        self.label = label
    def __add__(self, other):
        return Molecule([self, other])

class Molecule:
    def __init__(self, atoms):
        if type(atoms) is list:
            self.atoms = atoms

sodium = Atom("Na")
chlorine = Atom("Cl")
salt = Molecule([sodium, chlorine])
salt = sodium + chlorine

#Dunder Methods 2
