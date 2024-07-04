from file_operations import import_restaurants_list, save_restaurants_list
from app_operations import display_restaurants, add_restaurant, remove_restaurant, filter_restaurants, random_restaurant

FILE_PATH = './data/restaurant_list.json'


def main():
    restaurants = import_restaurants_list(FILE_PATH)

    if not restaurants:
        print("No data loaded or an error occured. Exiting.")
        return
    while True:
        print("\nWelcome to your Restaurant Tracker!\n")
        print("1: Display all restaurants")
        print("2: Add a new restaurant")
        print("3: Remove a restaurant")
        print("4: Filter restaurants by Price or Rating")
        print("5: Generate a random restaurant based on price")
        print("6: Save all changes and Exit")
        
        choice = input("\nSelect from the above: ")

        if choice == '1':
            display_restaurants(restaurants)
        elif choice == '2':
            add_restaurant(restaurants)
        elif choice == '3':
            remove_restaurant(restaurants)    
        elif choice == '4':
            filtered_restaurants = filter_restaurants(restaurants)
            if filtered_restaurants:
                display_restaurants(filtered_restaurants)
        elif choice == '5':
            random_restaurant(restaurants)
        elif choice == '6':
            try:
                save_restaurants_list(FILE_PATH, restaurants)
                break
            except Exception as e:
                print(f"Error saving restaurants list: {e}")
        else:
            print("Invalid Choice. Please select a number between 1-5")
    
if __name__ == "__main__":
    main ()

