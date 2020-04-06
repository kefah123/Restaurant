from Cook import Cook
from Station import Station


class Kitchen:
    def __init__(self):
        self.cooks = set()
        self.stations = set()

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

    def find_cook(self, id_no):
        for cook in self.cooks:
            if id_no == cook.get_id_no():
                return cook
        print("That cook does not currently exist in the kitchen.")
        return False

    def promote_cook(self, id_no, wage):
        for cook in self.cooks:
            if id_no == cook.get_id_no():
                cook.set_wage(wage)
                return True
        print("That cook does not currently exist in the kitchen.")
        return False

    def find_station(self, station_name):
        for station in self.stations:
            if station_name == station.get_name():
                return station
        print("That station does not currently exist in the kitchen.")
        return False

    def fire_employee(self, id_no):
        for cook in self.cooks:
            if id_no == cook.get_id_no():
                self.cooks.remove(cook)
                return True
        print("That cook is not currently employed in the kitchen.")
        return False

    def update_station_dish(self, station_name, dish, ingredients):
        updated_station = self.find_station(station_name)
        if not updated_station:
            return
        else:
            self.stations.remove(Station(station_name))
            updated_station.update_dish(dish, ingredients)
            self.stations.add(updated_station)

    def update_station_difficulty(self, station_name, difficulty):
        updated_station = self.find_station(station_name)
        if not updated_station:
            return
        else:
            self.stations.remove(Station(station_name))
            updated_station.set_difficulty(difficulty)
            self.stations.add(updated_station)

    def find_dish_using_ingredient(self,ingredient):
        found_dishes = set()
        for station in self.stations:
            print(station.to_string())
            for dish in station.find_dish_by_ingredient(ingredient):
                found_dishes.add(dish)
        return found_dishes
