import unittest
from Cook import Cook


class TestCook(unittest.TestCase):
    def test_to_string(self):
        myCook = Cook("Kwasi", 23, 14, "morning", 20, "apps")
        self.assertEqual("Name: Kwasi\nID: 20\nAge: 23\nWage: 14\nShift: morning\nStation: apps", myCook.to_string())


if __name__ == '__main__':
    unittest.main()
