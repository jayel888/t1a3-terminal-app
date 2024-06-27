from file_operations import import_restaurants_list, save_restaurants_list
from app_operations import display_restaurants, add_restaurant, rating_restaurants

FILE_PATH = '../data/restaurant_list.json'

def main():
    restaurants = import_restaurants_list(FILE_PATH)

    # add_restaurant(restaurants)
    # display_restaurants(restaurants)
    rating_restaurants(restaurants)

main ()

