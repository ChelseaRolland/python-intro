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

    def available_menus(self, time):
        #List Compreshension to find the menus that are available in the alloted time from the users
        avail_menus = [menu for menu in self.menus if datetime.time(time) >= menu.start_time and datetime.time(time) <= menu.end_time]

        return avail_menus

flagship_store = Franchise("1232 West End Road", [brunch, early_bird, dinner, kids])
new_installment = Franchise("12 East Mulberry Street", [brunch, early_bird, dinner, kids])
print(flagship_store)
print(new_installment)
print(flagship_store.available_menus(12))
print(flagship_store.available_menus(17))
print(flagship_store.available_menus(19))

#Creating Businesses
class Business:
    def __init__(self, name, franchises):
        self.name = name
        self.franchises = franchises
    
    def __repr__(self):
        return "We are {} and we have {} franchises".format(self.name, len(self.franchises))

first_business = Business("Basta Fazoolin' with my Heart", [flagship_store, new_installment])

arepas_menu = Menu("Take a’ Arepa", {
    'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}, datetime.time(10), datetime.time(20))

arepas_place = Franchise("189 Fitzgerald Avenue", [arepas_menu])

second_business = Business("Take a' Arepa", [arepas_place])
