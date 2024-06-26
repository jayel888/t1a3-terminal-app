import json

def import_restaurants_list(file_path):

    try:
        with open(file_path, 'r') as file:
            restaurants = json.load(file)
        return restaurants
    except FileNotFoundError:
        print(f"Error: The file {file_path} does not exist.")
        return []
    except Exception as e:
        print(f"An unexpected error occured: {e}")
        return []
    
def save_restaurants_list(file_path, restaurants):
    try:
        with open(file_path, 'w') as file:
            json.dump(restaurants, file, indent=4)
        print(f"List successfully updated. Saved to {file_path}.")
    except PermissionError:
        print(f"Error: Permission denied to write.")
    except Exception as e:
        print("An unexpected error occured", e)
