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
print("3.1 Tests: ",larger_list([4,10,2,5],[-10,2,5,10]))  #5

#4. More than N
def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False

#4. Tests
print("4.1 Tests: ",more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3)) #True

#5. Combine Sort
def combine_sort(lst1, lst2):
    return sorted(lst1 + lst2)

print("5.1 Tests: ",combine_sort([4, 10, 2, 5], [-10, 2, 5, 10])) #[-10, 2, 2, 4, 5, 5, 10, 10]

#6. Every Three Numbers
def every_three_nums(start):
    if start >= 100:
        return []
    else:
        return list(range(start,101,3))

#6. Tests
print("6.1 Test: ",every_three_nums(91)) #[91,94,97,100]

#7. Remove Middle
def remove_middle(lst, start, end):
    return lst[:start] + lst[end+1:]

#7. Tests
print("7.1 Tests: ",remove_middle([4, 8, 15, 16, 23, 42], 1, 3)) #[4, 23, 42]

#8. More Frequent Item
def more_frequent_item(lst, item1, item2):
    if lst.count(item1) >= lst.count(item2):
        return item1
    else:
        return item2

#8. Tests
print("8.1 Tests: ",more_frequent_item([2, 3, 3, 2, 3, 2, 3, 2, 3], 2, 3))

#9. Double Index
def double_index(lst, index):
    if index >= len(lst):
        return lst
    else:
        new_lst = lst[0:index]
        new_lst.append(lst[index]*2)
        new_lst = new_lst + lst[index+1:]
        return new_lst

#9. Tests
print("9.1 Tests: ", double_index([1, 2, 3, 4], 2))
print("9.2 Tests: ",double_index([3, 8, -10, 12], 2))

#10. Middle Item
def middle_element(lst):
    med_index = int(len(lst) / 2)
    if len(lst) % 2 == 0:
        sum = lst[med_index] + lst[med_index - 1]
        return sum / 2
    else:
        return lst[med_index]        

#10. Tests
print(middle_element([5, 2, -10, -4, 4, 5]))


