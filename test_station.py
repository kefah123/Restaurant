import unittest
from Station import Station


class TestStation(unittest.TestCase):
    def setUp(self):
        self.myStation = Station("Apps")
        self.myStation.set_difficulty("Moderate")
        self.myStation.update_dish("Fried Calamari",
                                   ("frozen calamari", "scallions", "black sesame seeds", "ponzu sauce"))

    def test_find_dish_by_ingredient(self):
        self.assertEqual([], self.myStation.find_dish_by_ingredient("frozen pork potstickers"))
        self.assertEqual(["Fried Calamari"], self.myStation.find_dish_by_ingredient("scallions"))
        self.myStation.update_dish("Potstickers",
                                   ("frozen pork potstickers", "scallions", "black sesame seeds", "sweet chili sauce"))
        self.assertEqual(["Fried Calamari", "Potstickers"], self.myStation.find_dish_by_ingredient("scallions"))


    def test_to_string(self):
        self.assertEqual("Station: Apps\nDifficulty: Moderate\nDishes:\nFried Calamari: frozen calamari,"
                         " scallions, black sesame seeds, ponzu sauce\n",self.myStation.to_string())


if __name__ == '__main__':
    unittest.main()
