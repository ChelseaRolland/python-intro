#1. Append Size
def append_size(lst):
    lst.append(len(lst))
    return lst

#1. Tests
print("1.1 Test: ", append_size([28, 15, 38]))  #[28,15,38,3]
print("1.2 Test: ", append_size([23, 42, 108])) #[23,42,108,3]

#2. Append Sum
def append_sum(lst):
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    lst.append(lst[-1] + lst[-2])
    return lst

#2. Tests
print("2.1 Test: ", append_sum([1,1,2]))
print("2.2 Test: ", append_sum([3, 4, 5]))

#3. Larger List

