# Cost of ground shipping

def cost_ground_ship(weight):
  flat_charge = 20.00
  if weight <= 2:
    return flat_charge + 1.50 * weight
  elif 2 < weight <= 6:
    return flat_charge + 3.00 * weight
  elif 6 < weight <= 10:
    return flat_charge + 4.00 * weight
  else:
    return flat_charge + 4.75 * weight

# Cost of drone shipping

def cost_drone_ship(weight):
  flat_charge = 0.00
  if weight <= 2:
    return flat_charge + 4.50 * weight
  elif 2 < weight <= 6:
    return flat_charge + 9.00 * weight
  elif 6 < weight <= 10:
    return flat_charge + 12.00 * weight
  else:
    return flat_charge + 14.25 * weight

# Cost of premium shipping

cost_premium = 125.00

# Function for cheapest method

def cheapest_ship(weight):
  ground = cost_ground_ship(weight)
  drone = cost_drone_ship(weight)
  premium = cost_premium = 125.00
  if ground < drone and ground < premium:
    print("The ground shipping method is the cheapest for you. With your package it is cost $" + str(ground) + ".")
  elif drone < ground and drone < premium:
    print("The drone shipping method is the cheapest for you. With your package it is cost $" + str(drone) + ".")
  else:
    print("The premium shipping method is the cheapest for you. It is cost $" + str(premium) + ".")

#TEST CODE

print(cost_ground_ship(8.4))
#$53.60
print(cost_drone_ship(1.5))
#$6.75
cheapest_ship(17)
#$100.75 ground
cheapest_ship(4.8)
#$34.40 ground
cheapest_ship(41.5)
#$125.00 premium
