#1. Append Size
def append_size(lst):
    lst.append(len(lst))
    return lst

#1. Tests
print("1.1 Test: ", append_size([28, 15, 38]))  #[28,15,38,3]
print("1.2 Test: ", append_size([23, 42, 108])) #[23,42,108,3]

#2. 