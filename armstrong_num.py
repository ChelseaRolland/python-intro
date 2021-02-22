#Checking Armstrong # for 3 Digits
#-------------------------------------

#input from the user
num =  int(input("Enter a number: "))

def three_armstrong_digits(num):
    #initalize sum
    sum = 0
    #find the sum of the cube of each digit
    temp = num
    while temp > 0:
        remainder = temp % 10
        sum += remainder ** 3
        temp //= 10

    if num == sum:
        print(num, " is an Armstrong number")
        return "True"
    else:
        print(num, " is not an Armstrong number")
        return "False"

print("3 Digit Armstrong Number: ",three_armstrong_digits(num))


#Checking Armstrong Num for n digits
#---------------------------------------
def n_digits_armstrong(num):
    # Changed num variable to string,
    # and calculated the length (number of digits)
    order = len(str(num))
    #initalize the sum
    sum = 0
    #find the sum of the order(# of digits) of each digit
    temp = num
    while temp > 0:
        remainder = temp % 10
        sum += remainder ** order
        temp //= 10
    
    if num == sum:
        print(num, " is an Armstrong Number")
        return "True"
    else:
        print(num, " is not an Armstrong Number")
        return "False"

print("N Digits Armstrong Number: ", n_digits_armstrong(num))

if len(str(num)) == 3:
    print("3 Digit Armstrong Number: ", three_armstrong_digits(num))
else:
    print("N Digits Armstrong Number: ", n_digits_armstrong(num))

