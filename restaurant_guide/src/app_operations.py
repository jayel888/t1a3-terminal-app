import random

def  display_restaurants(restaurants):
    try:
        for restaurant in restaurants:
            print(f"{restaurant['Restaurant']} - CUISINE: {restaurant['Cuisine']}, ADDRESS: {restaurant['Address']}, {restaurant['Postcode']}, {restaurant['State']}, PH: {restaurant['Phone']}, PRICE: ${restaurant['Est Price PP']}, RATING (Out of 10): {restaurant['Rating']}")
    except KeyError as e:
        print(f"Error displaying restaurants: Missing key {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

def add_restaurant(restaurants):
    try:
        name = input("What is the name of the restaurant? ")
        cuisine = input("What type of cuisine? ")
        address = input("What is the address (Enter without State or Postcode, eg. 123 Food Street) ? ")
        
        while True:
            postcode = (input("What is the postcode? "))
            if postcode.isnumeric() and len(postcode) == 4:
                break
            print("Invalid postcode. Please enter 4 numbers.")
            
        state = ""
        if postcode[0] == '3':
            state = 'VIC'
        elif postcode[0] == '2':
            state = 'NSW'
        elif postcode[0] == '0':
            state = 'NT'
        elif postcode[0] == '4':
            state = 'QLD'
        elif postcode[0] == '5':
            state = 'SA'
        elif postcode[0] == '6':
            state = 'WA'
        elif postcode[0] == '7':
            state = 'TAS'
        else:
            state = input("Which state is it located in? ")

        phone = input("What is their phone number? ")

        while True:
            try:
                price = int(input("What is the price per head? "))
                if price >= 0:
                    break
            except ValueError:
                pass
            print("Invalid input. Please enter a number.") 
            
        while True:
            try:
                rating = int(input("Enter rating between 0 - 10: "))
                if rating in range(0,11): 
                    break
            except ValueError:
                print("Invalid number. Please enter a number between 0 - 10") 
            except Exception as e:
                print(f"An unexpected error occured: {e}")
            

        restaurant = {"Restaurant":name, "Cuisine":cuisine, "Address":address, "Postcode":postcode, "State":state, "Phone":phone, "Est Price PP": price, "Rating":rating }
        restaurants.append(restaurant)
        print("Restaurant successfully added.")
    except ValueError:
        print("Error: Invalid input. Price and Rating must be an integer.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

def filter_restaurants(restaurants):
    filter = int(input("select rating: "))
    try:
        return [restaurant for restaurant in restaurants if restaurant['Rating'] > filter]
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return []
                

def random_restaurant(restaurants):
    rand_rest = random.choice(restaurants)
    print(rand_rest)

