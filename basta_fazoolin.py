import datetime

#Creating the Menus
class Menu:
    def __init__(self, name, items, start_time, end_time):
        self.name = name
        self.items = items
        self.start_time =  start_time
        self.end_time = end_time
    
    def __repr__(self):
        return "{} menu available from {} to {}".format(self.name, self.start_time, self.end_time)

    def calculate_bill(self, purchased_items):
        sum = 0
        for key, val in self.items.items():
            if key in purchased_items:
                sum += val
        return sum


brunch = Menu("brunch", {
    'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}, datetime.time(11), datetime.time(16))

early_bird = Menu("early_bird", {
    'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}, datetime.time(15), datetime.time(18))

dinner = Menu("dinner", {
    'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}, datetime.time(17), datetime.time(23))

kids = Menu("kids", {
    'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}, datetime.time(11), datetime.time(21))

print(brunch)
print(early_bird)
print(dinner)
print(kids)

print(brunch.calculate_bill(["pancakes", "home fries", "coffee"]))
print(early_bird.calculate_bill(["salumeria plate", "mushroom ravioli (vegan)"]))

#Creating the Franchises
class Franchise:
    def __init__(self, address, menus):
        self.address = address
        self.menus = menus
    
    def __repr__(self):
        return "This is the Basta Fazoolin with my Heart at {}".format(self.address)

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
print(flagship_store)
print(new_installment)


