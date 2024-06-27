from file_operations import import_restaurants_list, save_restaurants_list
from app_operations import display_restaurants, add_restaurant

FILE_PATH = 'restaurant_guide/data/restaurant_list.json'

def main():
    restaurants = import_restaurants_list(FILE_PATH)

    add_restaurant(restaurants)
    display_restaurants(restaurants)


main ()

