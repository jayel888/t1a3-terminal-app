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
    name = input("What is the name of the restaurant? ")
    cuisine = input("What type of cuisine? ")
    address = input("What is the address (Enter without State or Postcode, eg. 123 Food Street) ? ")
    
    while True:
        try: 
            postcode = (input("What is the postcode? "))
            if postcode.isnumeric() and len(postcode) == 4:
                break
            print("Invalid input. Postcode must be 4 digits")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
        
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
            print("Invalid input. Please enter a number.")
        except ValueError:
            print("Input must be a number.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
        
    while True:
        try:
            rating = int(input("Enter rating between 0 - 10: "))
            if rating in range(0,11): 
                break
            print("Invalid number. Please enter a number between 0 - 10") 
        except ValueError:
            print("Input must be a number.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")
        

    restaurant = {"Restaurant":name, "Cuisine":cuisine, "Address":address, "Postcode":postcode, "State":state, "Phone":phone, "Est Price PP": price, "Rating":rating }
    restaurants.append(restaurant)
    print("Restaurant successfully added.")

def filter_restaurants(restaurants):
    while True:
        filter = input("Do you want to sort by Price or Rating? ")
        if filter.lower() == "price":
            price_limit = int(input("Enter maximum price limit: "))
            try:
                return [restaurant for restaurant in restaurants if restaurant['Est Price PP'] < price_limit]
            except Exception as e:
                print(f"An unexpected error occured: {e}")
                return []
        elif filter.lower() == "rating":
            min_rating = int(input("Enter minimum rating: "))
            try:
                return [restaurant for restaurant in restaurants if restaurant['Rating'] >= min_rating]
            except Exception as e:
                print(f"An unexpected error occured: {e}")
                return []
        else: 
            print("Please enter 'Rating' or 'Price'.")



    # filter = int(input("select rating: "))
    # try:
    #     return [restaurant for restaurant in restaurants if restaurant['Rating'] > filter]
    # except Exception as e:
    #     print(f"An unexpected error occured: {e}")
    #     return []
                

def random_restaurant(restaurants):
    rand_rest = random.choice(restaurants)
    print(f"Random Restaurant: {rand_rest}")

