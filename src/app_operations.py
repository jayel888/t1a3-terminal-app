import random # used for random_restaurant function, which generates a random restaurant based on filters
import string # imported to use string.punctuation moduie to make sure no special characters are used in certain inputs
import pandas as pd

df = pd.read_json('../data/restaurant_list.json')

def  display_restaurants(restaurants): # Function to display all restaurants stored in .json file.
    try:
        # for restaurant in restaurants:
        #     print(f"{restaurant['Name']} - CUISINE: {restaurant['Cuisine']}, ADDRESS: {restaurant['Address']}, {restaurant['Postcode']}, {restaurant['State']}, PH: {restaurant['Phone']}, PRICE: ${restaurant['Est Price PP']}, RATING (Out of 10): {restaurant['Rating']}")
        print(df.to_string()) 
    except KeyError as e:
        print(f"Error displaying restaurants: Missing key {e}") # Error handling if key is non existent
    except Exception as e:
        print(f"An unexpected error occured: {e}")

def add_restaurant(restaurants): # Function to add a new restaurant to the list
    while True: # while loop when prompting for Restaurant Name, keeps prompting user for valid input.
        try:
            name = input("What is the name of the restaurant? ")
            if not name == "": # ensures name field cannot be left blank.
                break
            print("Name cannot be left blank.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

    while True: # While loop prompting for restaurant cuisine. 
        try:
            cuisine = input("What type of cuisine? ")
            if not cuisine or any(char.isdigit() for char in cuisine) or any(char in string.punctuation for char in cuisine): # scans each character in input to ensure no numbers or special characters are be input.
                print("Field cannot be left blank, contain any numbers, or contain special characters.")
            else:
                break # if requirements are met, break loop
        except Exception as e:
            print(f"An unexpected error occured: {e}") 

    while True:
        try:
            address = input("What is the address (Enter without State or Postcode, eg. 123 Food Street)? ")
            if address == "": #
                print("Address cannot be left blank.")
            else:
                break
        except Exception as e:
            print(f"An unexpected error occured: {e}") 

    while True:
        try: 
            postcode = (input("What is the postcode? "))
            if postcode.isnumeric() and len(postcode) == 4:
                break
            print("Invalid input. Postcode must be 4 digits only.")
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
            phone = input("What is their phone number (enter 'NA' if unknown)? ").replace(" ", "")
            if phone.isnumeric() and len(phone) == 10 or len(phone) == 8:
                break
            elif phone.lower() == "na":
                break
            print("Invalid phone number. Please provide valid landline or mobile number, or enter 'NA' if unknown.")
        except Exception as e:
            print(f"An unexpected error occured: {e}")

    while True:
        try:
            price = int(input("What is the average price per head? $"))
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
        

    restaurant = {"Name":name, "Cuisine":cuisine, "Address":address, "Postcode":postcode, "State":state, "Phone":phone, "Est Price PP": price, "Rating":rating }
    restaurants.append(restaurant)
    global df
    df = pd.DataFrame(restaurants)
    print("Restaurant successfully added.")

def remove_restaurant(restaurants):
    try:
        restaurant_to_remove = input("Enter the name of the restaurant you want to remove: ")

        for r, restaurant in enumerate(restaurants):
            if restaurant['Name'].lower() == restaurant_to_remove.lower():
                removed_restaurant = restaurants.pop(r)
                global df
                df = pd.DataFrame(restaurants)
                print(f"Removed {removed_restaurant['Name']} from the list.")
                return
        print("Restaurant not found. Names must match exactly. Press 1 to view all restaurants.")
    except KeyError as e:
        print(f"Error removing restaurant: Missing key {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def filter_restaurants(restaurants):
    df = pd.DataFrame(restaurants)
    while True:
        filter_by = input("Do you want to filter by 'Price' or 'Rating'? ").strip().lower()
        if filter_by == "price":
            try:
                max_price = float(input("Enter maximum price per head: "))
                filtered_df = df[df['Est Price PP'] <= max_price]
                if filtered_df.empty:
                    print("No restaurants found within the specified price limit.")
                else:
                    print(filtered_df.to_string(index=False))
                return
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        elif filter_by == "rating":
            try:
                min_rating = float(input("Enter minimum rating: "))
                filtered_df = df[df['Rating'] >= min_rating]
                if filtered_df.empty:
                    print("No restaurants found with the specified rating or higher.")
                else:
                    print(filtered_df.to_string(index=False))
                return
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}")
        else:
            print("Invalid input. Please enter 'Price' or 'Rating'.")    


def random_restaurant(restaurants):
    while True:
        try:
            price = input("Enter the maximum price you are willing to pay (or type 'any' for no limit): ")
            if price.lower() == "any":
                filtered_restaurants = restaurants
                break
            elif price.isnumeric():
                price = int(price)
                filtered_restaurants = [rest for rest in restaurants if rest['Est Price PP'] <= price]
                break
            else:
                print("Invalid input. Please enter a numeric value for price or 'any' for no limit.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    if filtered_restaurants:
        rand_rest = random.choice(filtered_restaurants)
        df = pd.DataFrame([rand_rest])
        print("\nRandom Restaurant:")
        print(df.to_string(index=False))
    else:
        print("No restaurants found within the specified price limit.")
