#1. Tenth Power
def tenth_power(num):
    return num ** 10
#1 Tests
print(tenth_power(1))
print(tenth_power(0))
print(tenth_power(2))

#2. Square Root
def square_root(num):
    return num ** 0.5

#2 Tests
print(square_root(16))
print(square_root(100))

#3. Win Percentage
def win_percentage(wins, losses):
    return (wins / (wins + losses)) * 100

#3 Tests
print(win_percentage(120, 80))
print(win_percentage(5, 5))
print(win_percentage(10, 0))

#4. Average
def average(num1, num2):
    return (num1 + num2) / 2

#4 Tests
print(average(1,100))
print(average(1,-1))
print(average(15,30))

#5. Remainder
def remainder(num1, num2):
    numerator = num1 * 2
    denominator = num2 / 2
    return numerator % denominator

#5 Tests
print(remainder(15, 14))
print(remainder(9,6))