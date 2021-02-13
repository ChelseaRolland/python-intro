#Let's make some pizzas
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "nushrooms"]
prices = [2, 6, 1, 3, 2, 7, 2]

num_pizzas = len(toppings)

print("We sell " + str(num_pizzas) + " different kinds of pizza!")

pizzas = list(zip(prices, toppings))
print(pizzas)

pizzas.sort()

cheapest_pizza = pizzas[0]
print("Cheapest Pizza: ", cheapest_pizza)
pricest_pizza = pizzas[-1]
print("Pricest Pizza: ", pricest_pizza)

three_cheapest = pizzas[:3]
print("Three Cheapest Pizzas: ", three_cheapest)

num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)
