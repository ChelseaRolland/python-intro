#weight = 13
#weight = 4.8
weight = 41.5

#Ground Shipping
if weight <= 2:
  cost_ground = weight * 1.50 + 20.00
elif 2 < weight <= 6:
  cost_ground = weight * 3.00 + 20.00
elif 6 < weight <= 10:
  cost_ground = weight * 4.00 + 20.00
else:
  cost_ground = weight * 4.75 + 20.00

print("Cost of Ground: $",cost_ground)

#Ground Shipping Premium
cost_ground_premium = 125.00
print("Cost of Premium Ground: $",cost_ground_premium)

#Drone Shipping
if weight <= 2:
  cost_drone = weight * 4.50 + 0
elif 2 < weight <= 6:
  cost_drone = weight * 9.00 + 0
elif 6 < weight <= 10:
  cost_drone = weight * 12.00 + 0
else:
  cost_drone = weight * 14.25 + 0

print("Cost of Drone: $",cost_drone)
