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

