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
