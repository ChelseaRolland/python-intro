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

#4. Values that are Keys
def values_that_are_keys(my_dictionary):
    values_are_keys = []
    for key in my_dictionary.keys():
        for value in my_dictionary.values():
            if value == key:
                values_are_keys.append(value)
    return values_are_keys

#4 - Tests
print("Chall 4.1: ", values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print("Chall 4.2: ", values_that_are_keys({"a":"apple", "b":"a", "c":100}))

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
