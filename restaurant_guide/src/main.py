from file_operations import import_restaurants_list, save_restaurants_list
from app_operations import display_restaurants

FILE_PATH = '../data/restaurant_list.json'

def main():
    restaurants = import_restaurants_list(FILE_PATH)

    print(display_restaurants(restaurants))

main ()

