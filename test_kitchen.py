import unittest
from Kitchen import Kitchen
from Station import Station
from Cook import Cook


class TestKitchen(unittest.TestCase):

    def setUp(self):
        self.myKitchen = Kitchen()

    def test_add_station(self):
        self.myKitchen.add_station("Saute")
        self.assertIn(Station("Saute"), self.myKitchen.get_stations())

    def test_add_cook(self):
        self.myKitchen.add_cook("Efah", 23, 14, "morning", "Grill")
        self.assertNotIn(Cook("Efah", 23, 14, "morning", "E0h", "Grill"), self.myKitchen.get_cooks())

        self.myKitchen.add_station("Grill")
        self.myKitchen.add_cook("Efah", 23, 14, "morning", "Grill")
        self.assertIn(Cook("Efah", 23, 14, "morning", "E0h", "Grill"), self.myKitchen.get_cooks())
        self.myKitchen.add_cook("Kwasi", 23, 14, "night", "Grill")

        self.assertIn(Cook("Kwasi", 23, 14, "night", "K1i", "Grill"), self.myKitchen.get_cooks())

    def test_find_cook(self):
        self.myKitchen.add_station("Saute")
        self.myKitchen.add_cook("Kwasi", 23, 14, "swing", "Saute")

        testingCook = self.myKitchen.find_cook("K0i")
        self.assertEqual(testingCook, Cook("Kwasi", 23, 14, "swing", "K0i", "Saute"))

        self.assertFalse(self.myKitchen.find_cook("GFDG435435"))

    def test_promote_cook(self):
        self.myKitchen.add_station("Saute")
        self.myKitchen.add_cook("Kwasi", 23, 14, "swing", "Saute")
        self.myKitchen.promote_cook("K0i", 16)
        testingCook = self.myKitchen.find_cook("K0i")
        self.assertEqual(testingCook.get_wage(), 16)

        self.assertFalse(self.myKitchen.promote_cook("453", 25))

    def test_find_station(self):
        self.myKitchen.add_station("Apps")
        self.assertEqual(self.myKitchen.find_station("Apps"), Station("Apps"))
        self.assertFalse(self.myKitchen.find_station("Grill"))

    def test_fire_employee(self):
        self.myKitchen.add_station("Saute")
        self.myKitchen.add_cook("Kwasi", 23, 14, "swing", "Saute")
        self.myKitchen.fire_employee("K0i")
        self.assertFalse(self.myKitchen.find_cook("K0i"))

    def test_update_station_dish(self):
        self.myKitchen.add_station("Apps")
        self.myKitchen.update_station_dish("Apps", "Fried calamari", ("Scallions", "Calamari"))
        station = Station("Apps")
        station.update_dish("Fried calamari", ("Scallions", "Calamari"))
        self.assertEqual(self.myKitchen.find_station("Apps"), station)

    def test_update_station_difficulty(self):
        self.myKitchen.add_station("Apps")
        self.myKitchen.update_station_dish("Apps", "Fried calamari", ("Scallions", "Calamari"))
        self.myKitchen.update_station_difficulty("Apps", "moderate")
        station = Station("Apps")
        station.update_dish("Fried calamari", ("Scallions", "Calamari"))
        station.set_difficulty("moderate")
        self.assertEqual(self.myKitchen.find_station("Apps"), station)

    def test_find_dish_using_ingredient(self):
        self.myKitchen.add_station("Apps")
        self.myKitchen.add_station("Saute")
        self.myKitchen.update_station_dish("Apps", "Fried calamari", ("Scallions", "Calamari"))
        self.myKitchen.update_station_dish("Saute", "Ahi tuna", ("Scallions", "Tuna"))
        self.myKitchen.update_station_dish("Apps", "Nachos",("Scallions","Nachos"))
        self.assertEqual({"Fried calamari", "Ahi tuna", "Nachos"}, self.myKitchen.find_dish_using_ingredient("Scallions"))


if __name__ == '__main__':
    unittest.main()
