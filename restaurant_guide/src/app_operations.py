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
        address = input("What is the address? ")
        postcode = input("What is the postcode? ")
        state = input("What state is it located in? ")
        phone = input("What is their phone number? ")
        price = int(input("What is the price per head?"))
        rating = int(input("What do you rate it? (out of 10): "))

        restaurant = {"Restaurant":name, "Cuisine":cuisine, "Address":address, "Postcode":postcode, "State":state, "Phone":phone, "Est Price PP": price, "Rating":rating }
        restaurants.append(restaurant)
        print("Restaurant successfully added.")
    except ValueError:
        print("Error: Invalid input. Price and Rating must be an integer.")
    except Exception as e:
        print(f"An unexpected error occured: {e}")