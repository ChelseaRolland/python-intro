#1. Sum Values
def sum_values(my_dictionary):
    total = 0
    for num in my_dictionary.values():
        total += num
    return total

#1 - Tests
print("Chall 1.1: ", sum_values({"milk":5, "eggs":2, "flour": 3}))
print("Chall 1.2: ", sum_values({10:1, 100:2, 1000:3}))

#2. Even Keys
def sum_even_keys(my_dictionary):
    total = 0
    for even in my_dictionary.keys():
        if even % 2 == 0:
            total += my_dictionary[even]
    return total

#2 - Tests
print("Chall 2.1: ", sum_even_keys({1:5, 2:2, 3:3}))
print("Chall 2.2: ", sum_even_keys({10:1, 100:2, 1000:3}))

#3. Add Ten
def add_ten(my_dictionary):
    for key in my_dictionary.keys():
        my_dictionary[key] += 10
    return my_dictionary

#3 - Tests
print("Chall 3.1: ", add_ten({1:5, 2:2, 3:3}))
print("Chall 3.2: ", add_ten({10:1, 100:2, 1000:3}))

#4.

#4 - Tests

#5.

#5 - Tests

#6.

#6 - Tests

#7.

#7 - Tests

#8.

#8 - Tests

#9.

#9 - Tests
