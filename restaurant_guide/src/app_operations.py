def  display_restaurants(restaurants):
    try:
        for restaurant in restaurants:
            print(f"{restaurant['Restaurant']} - CUISINE: {restaurant['Cuisine']}, ADDRESS: {restaurant['Address']}, {restaurant['Postcode']}, {restaurant['State']}, PH: {restaurant['Phone']}, PRICE: ${restaurant['Est Price PP']}, RATING (Out of 10): {restaurant['Rating']}")
    except KeyError as e:
        print(f"Error displaying matches: Missing key {e}")
    except Exception as e:
        print(f"An unexpected error occured: {e}")