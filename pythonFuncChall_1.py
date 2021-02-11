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
    #total = wins + losses
    #win_ratio = (wins / total) * 100
    #win_ratio = (wins / (wins + losses)) * 100
    return (wins / (wins + losses)) * 100

#3 Tests
print(win_percentage(120, 80))
print(win_percentage(5, 5))
print(win_percentage(10, 0))
