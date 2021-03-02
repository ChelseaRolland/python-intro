from datetime import datetime
from decimal import Decimal
import random

#DateTime Module
current_time = datetime.now()
print("Current Time: ", current_time)

#Random Module
random_list = []
random_list = [random.randint(1,100) for num in range(101)]
randomer_number = random.choice(random_list)
print("Random Number: ", randomer_number)

#Decimals
two_decimal_points = Decimal("0.2") + Decimal("0.69")
print("Decimal 2: ", two_decimal_points)

four_decimal_points = Decimal("0.53") * Decimal("0.65")
print("Decimal 4: ", four_decimal_points)

#DateTime In more Depth --> Review the python docs for more info

#datetime(year, month, day, hour, minute, second)
old_day = datetime(1575, 7, 13, 13, 9, 57)
print(old_day.year)
print(old_day.hour)
print(old_day.weekday())

print(datetime(2021,1,1) - datetime(2017,1,1))
print(datetime.now() - datetime(2018,1,1))

#Parsing a Date
parsed_date = datetime.strptime("Jan 05, 2009", "%b %d, %Y")
print(parsed_date.month)
print(parsed_date.year)

parsed_date = datetime.strptime("Jul 13, 2021", "%b %d, %Y")
print(parsed_date.month)
print(parsed_date.year)

#Rendering a Date as a string
date_string = datetime.strftime(datetime.now(), "%b %d, %Y")
print(date_string)
