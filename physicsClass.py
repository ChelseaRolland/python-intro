#temperature
def f_to_c(f_temp):
    c_temp = (f_temp - 32) * 5/9
    return c_temp

f100_in_celsius = f_to_c(100)
print("100 Fahrenheit to Celsius: ", f100_in_celsius)

def c_to_f(c_temp):
    f_temp = c_temp * (9/5) + 32
    return f_temp

c0_in_fahrenheit = c_to_f(0)
print("0 Celsius to Fahrenheit: ", c0_in_fahrenheit)

#Use Force
def get_force(mass, acceleration):
    return mass * acceleration

train_mass = 22680
train_acceleration = 10
train_distance = 100
train_force = get_force(train_mass, train_acceleration)

print("Train Force: ", train_force)
print("The GE train supplied " + str(train_force) + " Newtons of force.")

def get_energy(mass, c = 3 * 10**8):
    return mass * c**2

bomb_mass = 1

bomb_energy = get_energy(bomb_mass)
print("Bomb with Mass 1 energy: ",bomb_energy)
print("A 1kg bomb supplies " + str(bomb_energy) + " Joules.")

def get_work(mass, acceleration, distance):
    work = get_force(mass, acceleration) * distance
    return work

train_work = get_work(train_mass, train_acceleration, train_distance)
print("Train Work: ", train_work)
print("The GE train does " + str(train_work) + " Joules of work over " + str(train_distance) + " meters")