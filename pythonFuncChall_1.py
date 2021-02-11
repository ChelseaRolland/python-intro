#1. Tenth Power
def tenth_power(num):
    return num ** 10
#1 Tests
print(tenth_power(1)) #1
print(tenth_power(0)) #0
print(tenth_power(2)) #1024

#2. Square Root
def square_root(num):
    return num ** 0.5

#2 Tests
print(square_root(16))  #4
print(square_root(100)) #10

#3. Win Percentage
def win_percentage(wins, losses):
    return (wins / (wins + losses)) * 100

#3. Tests
print(win_percentage(120, 80)) #60.0
print(win_percentage(5, 5))    #50.0
print(win_percentage(10, 0))   #100.0

#4. Average
def average(num1, num2):
    return (num1 + num2) / 2

#4. Tests
print(average(1,100)) #50.5
print(average(1,-1))  #0.0
print(average(15,30)) #22.5

#5. Remainder
def remainder(num1, num2):
    return (num1 * 2) % (num2 / 2)

#5. Tests
print(remainder(15, 14)) #2.0
print(remainder(9,6))    #0.0

#6. First Three Multiples
def first_three_multiples(num):
    print(num * 1)
    print(num * 2)
    print(num * 3)
    return num * 3

#6. Tests
print(first_three_multiples(10))
print(first_three_multiples(0))

#7. Tip
def tip(total, percentage):
    return (total * percentage) / 100

#7. Tests
print(tip(10, 25))    #2.5
print(tip(0,100))     #0.0
print(tip(67.35, 30)) #20.205

#8. String Concatenation
def introduction(first_name, last_name):
    return last_name + ", " + first_name + " " + last_name

#8. Tests
print(introduction("Chelsea", "Rolland")) #Rolland, Chelsea Rolland
print(introduction("James", "Bond"))      #Bond, James Bond
print(introduction("Maya", "Angelou"))    #Angelou, Maya Angelou

#9. Dog Years
def dog_years(name, age):
    return name + ", you are " + str(age * 7) + " years old in dog years"

#9. Tests
print(dog_years("Coven", 7))
print(dog_years("Lola", 16))
print(dog_years("Baby", 0))

#10 All Operations
def lots_of_math(a,b,c,d):
    print(a + b)
    print(c - d)
    print((a + b) * (c - d))
    return ((a + b) * (c - d)) % a

print(lots_of_math(1,2,3,4))
print(lots_of_math(1,1,1,1))