#1. Divisble By Ten
def divisible_by_ten(num):
    count = 0
    for input in num:
        if input % 10 == 0:
            count+=1
    return count

#1 Tests
print("Divisible By Ten: ", divisible_by_ten([20, 25, 30, 35, 40]))

#2 Grettings
def add_greetings(names):
    greetings = ["Hello, " + name for name in names]
    return greetings

#2 Tests
print("Greetings: ",add_greetings(["Owen", "Max", "Sophie"])) #Greetings:  ['Hello, Owen', 'Hello, Max', 'Hello, Sophie']

#3 Delete starting Even Numbers
def delete_starting_evens(lst):
    while (len(lst) > 0 and lst[0] % 2 == 0):
        lst = lst[1:]
    return lst

#3 Tests
print("Delete Starting Evens 3.1: ",delete_starting_evens([4, 8, 10, 11, 12, 15])) #[11, 12, 15]
print("Delete Starting Evens 3.2: ", delete_starting_evens([4, 8, 10]))  # []

#4 Odd Indices
def odd_indices(lst):
    new_list = []
    for i in range(1, len(lst), 2):
        new_list.append(lst[i])
    return new_list        


#4 Tests
print("Odd Indices 4.1: ", odd_indices([4, 3, 7, 10, 11, -2]))  #[3, 10, -2]

#4.A Even Indices
def even_indices(lst):
    new_list = []
    for i in range(0, len(lst), 2):
        new_list.append(lst[i])
    return new_list

#4.A Tests
print("Even Indices 4.A.1: ", even_indices([4, 3, 7, 10, 11, -2]))  #[4, 7, 11]

#5 Exponents


#5 Tests
