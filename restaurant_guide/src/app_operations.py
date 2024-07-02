import random # used for random_restaurant function, which generates a random restaurant based on filters
import string # imported to use string.punctuation moduie to make sure no special characters are used in certain inputs

def  display_restaurants(restaurants):
    try:
        for restaurant in restaurants:
            print(f"{restaurant['Restaurant']} - CUISINE: {restaurant['Cuisine']}, ADDRESS: {restaurant['Address']}, {restaurant['Postcode']}, {restaurant['State']}, PH: {restaurant['Phone']}, PRICE: ${restaurant['Est Price PP']}, RATING (Out of 10): {restaurant['Rating']}")
    except KeyError as e:
        print(f"Error displaying restaurants: Missing key {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")

def add_restaurant(restaurants):
    while True:
        try:
            name = input("What is the name of the restaurant? ")
            if name != "":
                break
            print("Name cannot be left blank.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

    while True:
        try:
            cuisine = input("What type of cuisine? ")
            if not cuisine or any(char.isdigit() for char in cuisine) or any(char in string.punctuation for char in cuisine):
                print("Field cannot be left blank, contain any numbers, or contain special characters.")
            else:
                break
        except Exception as e:
            print(f"An unexpected error occured: {e}") 

    while True:
        try:
            address = input("What is the address (Enter without State or Postcode, eg. 123 Food Street) ? ")
            if address != "":
                break
            print("Field cannot be left blank. Please write NA if unknown.")
        except Exception as e:
            print(f"An unexpected error occured: {e}") 

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

    while True:
        try:
            phone = input("What is their phone number? ").replace(" ", "")
            if phone.isnumeric() and len(phone) == 8 or 10:
                break
            print("Invalid Input. Please input only 10 digits, for landline include area code.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

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
            while True:
                try:
                    price_limit = int(input("Enter maximum price per head limit: "))
                    if price_limit > 0:
                        return [restaurant for restaurant in restaurants if restaurant['Est Price PP'] < price_limit]
                    print("Input invalid, please enter a number greater than 0")                   
                except ValueError:
                    print("Input must be a number greater than 0")
                except Exception as e:
                    print(f"An unexpected error occured: {e}")
                    return []
        elif filter.lower() == "rating":
            while True:
                try:
                    min_rating = int(input("Enter minimum rating: "))
                    if 0 <= min_rating <= 10:
                        return [restaurant for restaurant in restaurants if restaurant['Rating'] >= min_rating]
                    print("Input invalid. Please enter number between 0-10")
                except ValueError:
                    print("Input must be a number between 0 - 10")
                except Exception as e:
                    print(f"An unexpected error occured: {e}")
                    return []
        else: 
            print("Please enter 'Rating' or 'Price'.")
          
def random_restaurant(restaurants):
    while True:
        try:
            price = input("Enter the maximum price you are willing to pay: ")
            if not price.isnumeric():
                print("Invalid input. Please enter a numeric value for price.")
                continue #skips the rest of the loop to prompt user for correct input

            price = int(price)
            filtered_restaurants = [rest for rest in restaurants if rest['Est Price PP'] <= price]

            if filtered_restaurants:
                rand_rest = random.choice(filtered_restaurants)
                print(f"Random Restaurant: {rand_rest['Restaurant']} - CUISINE: {rand_rest['Cuisine']}, ADDRESS: {rand_rest['Address']}, {rand_rest['Postcode']}, {rand_rest['State']}, PH: {rand_rest['Phone']}, PRICE: ${rand_rest['Est Price PP']}, RATING (Out of 10): {rand_rest['Rating']}")
            else:
                print("No restaurants found within the specified price range.")
            break
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

