# Program will calculate the total cost of a holiday based on the destination of the user.
# Each destination will have a cost for flight, hotel per night and car rental per day, stored in their own list
# User will specify the destination, the number of nights they will be staying and the number of days they will be renting a car.

# Capitalise first letter
def capitalise(destination):
    new_name = ""
    i = 0
    while i < len(destination):
        if i == 0:
            new_name = new_name + destination[0].upper()
        else:
            new_name = new_name + destination[i]
        i = i + 1
    return new_name


# Defined functions recieve desination. It searches each list for that destination and then uses that list to calculate the cost, which it then returns.
def plane_cost(destination): # total cost for the flight
    if destination == london[0]:
        return london[1]
    elif destination == madrid[0]:
        return madrid[1]
    elif destination == berlin[0]:
        return berlin[1]
    elif destination == brendon[0]:
        return brendon[1]
    
def hotel_cost(no_nights, destination): # total cost for the hotel
    if destination == london[0]:
        return london[2] * no_nights
    elif destination == madrid[0]:
        return madrid[2] * no_nights
    elif destination == berlin[0]:
        return berlin[2] * no_nights
    elif destination == brendon[0]:
        return brendon[2] * no_nights 
    
def car_rental(no_days, destination): # total cost for the car rental
    if destination == london[0]:
        return london[3] * no_days
    elif destination == madrid[0]:
        return madrid[3] * no_days
    elif destination == berlin[0]:
        return berlin[3] * no_days
    elif destination == brendon[0]:
        return brendon[3] * no_days 
    
def holiday_cost():
    return plane_cost(city_flight) + hotel_cost(num_nights, city_flight) + car_rental(rental_days, city_flight)

# Define the lists of destination. Name, Cost for flight, Cost of hotel per night, Cost of car rental per day
london = ["london", 550, 200, 75]
madrid = ["madrid", 450, 100, 50]
berlin = ["berlin", 450, 150, 60]
brendon = ["brendon", 1000, 5000, 6000]


########################## Get destination, number of nights of stay and number of days car rental. ##############################
validdestination = ("london, madrid, berlin, brendon")

while True:
    city_flight = input("Where would you like to go? London, Madrid, Berlin or Brendon?\n")
    city_flight = city_flight.lower()
    if city_flight in validdestination:
        break
    else:
        print("Please enter a valid destination.\n")

print(len(city_flight))
while True:
    try:
        num_nights = int(input("\nHow many nights would you like to stay for in " + capitalise(city_flight) + "?\n"))
        if num_nights <= 0:
            print("You must enter a value greater than 0 here.")
        else:
            break
    except ValueError:
        print("\nPlease only enter positive, whole numbers here.\n")

while True:
    try:
        rental_days = int(input("\nHow many days would you like to rent a car for in " + capitalise(city_flight) + "?\n"))
        if rental_days > num_nights + 1:
            print(f"\nYou cannot rent a car for longer than the duration of your stay. Please enter a value less than " + str(num_nights + 1) + ".\n")
        elif rental_days <= 0:
            print("You must enter a value greater than 0 here.")
        else:
            break
    except ValueError:
        print("\nPlease only enter numbers here.\n")
    

############### Calculate costs of stay. ##############################

print(f"\nThe cost of a flight to {capitalise(city_flight)} will be £{plane_cost(city_flight)}")
print(f"\nThe cost of a hotel in {capitalise(city_flight)} for {num_nights} nights will be £{hotel_cost(num_nights, city_flight)}.")
print(f"\nThe cost of the car rental in {capitalise(city_flight)} for {rental_days} days will be £{car_rental(rental_days, city_flight)}.")

################### Calculate total cost of stay #################
print(f"\n\nThe total cost of your trip to {capitalise(city_flight)} will be £{holiday_cost()}\n")