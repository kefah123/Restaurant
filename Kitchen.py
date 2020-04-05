from Cook import Cook
from Station import Station
import random


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
            id_no = len(self.cooks) + random.randint(0, 75) + name[0]
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
            else:
                print("That cook does not currently exist in the kitchen.")

    def promote_cook(self, id_no, wage):
        for cook in self.cooks:
            if id_no == cook.get_id_no():
                cook.set_wage(wage)
            else:
                print("That cook does not currently exist in the kitchen.")

    def find_station(self, station_name):
        for station in self.stations:
            if station_name == station.get_name():
                return station
            else:
                print("That station does not currently exist in the kitchen.")

    def fire_employee(self, id_no):
        for cook in self.cooks:
            if id_no == cook.get_id_no():
                self.cooks.remove(cook)

