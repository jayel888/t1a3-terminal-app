from file_operations import import_restaurants_list, save_restaurants_list
from app_operations import display_restaurants, add_restaurant, filter_restaurants, random_restaurant

FILE_PATH = '../data/restaurant_list.json'

def main():
    restaurants = import_restaurants_list(FILE_PATH)

    if not restaurants:
        print("No data loaded or an error occured. Exiting.")
        return
    while True:
        print("\nWelcome to your Restaurant Tracker!\n")
        print("1: Display all restaurants")
        print("2: Add a new restaurant")
        print("3: Filter restaurants by Rating or Price.")
        print("4: Generate a random restaurant. (Perfect for when you can't decide what to eat)")
        print("5: Save updates and Exit")

        choice = input("\nSelect from the above: ")

        if choice == '1':
            display_restaurants(restaurants)
        elif choice == '2':
            add_restaurant(restaurants)
        elif choice == '3':
            prices = filter_restaurants(restaurants)
            display_restaurants(prices)
        elif choice == '4':
            random_restaurant(restaurants)
        elif choice == '5':
            break
        
        else:
            print("Invalid Choice. Please select a number between 1-5")
    
if __name__ == "__main__":
    main ()

