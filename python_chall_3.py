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
def exponents(bases, powers):
    new_list = []
    for base in bases:
        for power in powers:
            new_list.append(base**power)
    return new_list


#5 Tests
print("Exponents: ",exponents([2, 3, 4], [1, 2, 3]))  #[2, 4, 8, 3, 9, 27, 4, 16, 64]

#6 Larger Sum
def larger_sum(lst1, lst2):
    #Initializing the sums
    sum1 = 0
    sum2 = 0

    #Looping thru each lst for the sums
    for num in lst1:
        sum1 += num
    
    for num in lst2:
        sum2 += num
    
    #Comparing each sum to see which 1 is the largest
    if sum1 >= sum2:
        return lst1
    else:
        return lst2


#6 Test
print("Larger Sum: ",larger_sum([1, 9, 5], [2, 3, 7]))  #[1,9,5]

#7 Over 9000
def over_nine_thousand(lst):
    #Sum until it gets over 9000
    #Over 9000, then return the sum and stop
    #Under 9000, then return the sum of all elements
    #If empty, then return 0
    if len(lst) == 0:
        return 0
    sum = 0
    for num in lst:
        if sum < 9000:
            sum += num
        else:
            break
    return sum

#7 Tests
print("Over 9000 7.1: ",over_nine_thousand([8000, 900, 120, 5000]))  #9020
print("Over 9000 7.2: ", over_nine_thousand([8000, 900, 12, 5]))     #8917
print("Over 9000 7.3: ", over_nine_thousand([]))                     #0

#8 Max Num
def max_num(nums):
    #Should return highest number in list
    #Create variable to store 1st element to start comparison
    maxi = nums[0]
    #Loop thru each elements in list
    for num in nums:
        #If the maxi variable is less than next element, then reset it to new element
        if maxi < num:
            maxi = num
    return maxi

#8 Test
print("Max Num 8.1: ",max_num([50, -10, 0, 75, 20]))        #75
print("Max Num 8.2: ", max_num([0, 100, 0, 75, 20]))        #100
print("Max Num 8.3: ", max_num([111, 15, 33, 81, 555]))     #555

#8.A Min Num
def min_num(nums):
    mini = nums[0]
    for num in nums:
        #If the mini variable is more than the next element, then reset it to the new element
        if mini > num:
            mini = num
    return mini


#8.A Test
print("Min Num 8.1: ", min_num([50, -10, 0, 75, 20]))     #-10
print("Min Num 8.2: ", min_num([0, 100, 0, 75, 20]))      #0
print("Min Num 8.3: ", min_num([111, 15, 33, 81, 555]))   #15

#9 Same Values
def same_values(lst1, lst2):
    #Should return list of indicies where the values were equal in lst1 and lst2
    
    #With For Loop
    #new_list = []
    # for index in range(len(lst1)):
    #     if lst1[index] == lst2[index]:
    #         new_list.append(index)

    #With List Comprehension
    #Utilze the range to find the index since range excludes the len num of lists and will be the size of the list due to 0 indexing
    new_list = [i for i in range(len(lst1)) if lst1[i] == lst2[i]]
    return new_list

#9 Test
print("Same Values 9.1: ",same_values([5, 1, -10, 3, 3], [5, 10, -10, 3, 5]))       #[0,2,3]
print("Same Values 9.2: ", same_values([3,-1,9], [45,1,9]))                         #[2]
print("Same Values 9.3: ", same_values([-33, -100, -10, 4], [-33, -100, -10, 3]))   #[0,1,2]

#10 Reversed Lists
def reversed_list(lst1, lst2):
    for i in range(len(lst1)):
        #Checking for the 1s that are not true, if this pings once, then they do not equal
        if lst1[i] != lst2[len(lst2) - 1 - i]:
            return False    
    #if the above for loop doesn't have any pings for False, then the elements match thus returning true
    return True


#10 Tests
print("Reversed List 10.1: ",reversed_list([1, 2, 3], [3, 2, 1]))
print("Reversed List 10.2: ",reversed_list([1, 5, 3], [3, 2, 1]))
