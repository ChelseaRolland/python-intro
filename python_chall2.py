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
def larger_list(lst1, lst2):
    if len(lst1) >= len(lst2):
        return lst1[-1]
    else:
        return lst2[-1]

#3. Tests
print(larger_list([4,10,2,5],[-10,2,5,10]))  #5

#4. More than N
def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False

#4. Tests
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3)) #True

#5. Combine Sort
def combine_sort(lst1, lst2):
    return sorted(lst1 + lst2)

print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10])) #[-10, 2, 2, 4, 5, 5, 10, 10]
