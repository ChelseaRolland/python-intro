description = "{} is {age} years old."
print(description.format("Bob", age=30))

my_name = "Coven"
your_name = input("Enter your name: ")
print(f"Hello {your_name}. My name is {my_name}.")

age = int(input("Enter your age: "))
#age_num = int(age)  #Changing into an integer
months = age * 12
print(f"You have lived for {months} months.")

seconds = age * 60 * 60 * 24 * 365

age = int(input("Enter your age: "))
side_job = True
print(age > 18 and age < 65 or side_job)
