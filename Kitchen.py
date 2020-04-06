from Cook import Cook
from Station import Station

""" This class simulates a restaurant Kitchen"""
class Kitchen:
    def __init__(self):
        self.cooks = set()
        self.stations = set()
    """
    The add_cook method adds a new cook to the set of cooks if the cook is assigned an existing station
    It sets the cook's ID number with a concatenation of the first letter of their name, the length of the set, and the last letter
    of their name
    Parameters are the details of the cook
    """
    def add_cook(self, name, age, wage, shift, station_name):
        found_station = 0
        for station in self.stations:
            if station_name == station.get_name():
                found_station = 1

        if found_station == 1:
            id_no = name[0] + str(len(self.cooks)) + name[-1]
            self.cooks.add(Cook(name, age, wage, shift, id_no, station_name))
        else:
            print("That station does not currently exist in this kitchen. Use the 'add_station method to add a new "
                  "station.")

    def add_station(self, station_name):
        self.stations.add(Station(station_name))

    def get_cooks(self):
        return self.cooks

    def get_stations(self):
        return self.stations

    """
    The find_cook method searches the set of cooks for a specific cook by their ID number
    Parameter is the id number of the cook
    Returns the cook if found, returns false otherwise
    """
    def find_cook(self, id_no):
        for cook in self.cooks:
            if id_no == cook.get_id_no():
                return cook
        print("That cook does not currently exist in the kitchen.")
        return False
    """
    The promote_cook method searches the set of cooks for a specific cook by their ID number and modifies their wage
    Parameter is the id number of the cook and the new wage value
    Returns True if successful, false otherwise
    """
    def promote_cook(self, id_no, wage):
        for cook in self.cooks:
            if id_no == cook.get_id_no():
                cook.set_wage(wage)
                return True
        print("That cook does not currently exist in the kitchen.")
        return False

    """
    The find_station method searches the set of stations for a specific station by its name 
    Parameter is the name of the station
    Returns the station if found, returns false otherwise
    """
    def find_station(self, station_name):
        for station in self.stations:
            if station_name == station.get_name():
                return station
        print("That station does not currently exist in the kitchen.")
        return False

    """
    The fire_employee method searches the set of cooks for a specific cook by their ID number and removes them
    Parameter is the id number of the cook
    Returns True if successfully fired, returns false otherwise
    """
    def fire_employee(self, id_no):
        for cook in self.cooks:
            if id_no == cook.get_id_no():
                self.cooks.remove(cook)
                return True
        print("That cook is not currently employed in the kitchen.")
        return False

    """
    The update_station_dish method updates dishes and ingredients of a particular station
    Parameter is the name of the station, the new dish, the ingredients of the new dish
    """
    def update_station_dish(self, station_name, dish, ingredients):
        updated_station = self.find_station(station_name)
        if not updated_station:
            return
        else:
            self.stations.remove(Station(station_name))
            updated_station.update_dish(dish, ingredients)
            self.stations.add(updated_station)

    """
    The update_station_difficulty method updates the difficulty of a particular station
    Parameters are the name of the station and the new difficulty
    """
    def update_station_difficulty(self, station_name, difficulty):
        updated_station = self.find_station(station_name)
        if not updated_station:
            return
        else:
            self.stations.remove(Station(station_name))
            updated_station.set_difficulty(difficulty)
            self.stations.add(updated_station)

    """
    The find_dish_using_ingredient searches for all dishes in all stations that uses a particular ingredient
    Parameter is the ingredient
    Returns a set of dishes that uses the ingredient
    """
    def find_dish_using_ingredient(self,ingredient):
        found_dishes = set()
        for station in self.stations:
            for dish in station.find_dish_by_ingredient(ingredient):
                found_dishes.add(dish)
        return found_dishes
