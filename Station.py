class Station:
    def __init__(self, name):
        self.name = name
        self.dishes = {}
        self.difficulty = ""

    def get_name(self):
        return self.name

    def get_dishes(self):
        return self.dishes

    def get_difficulty(self):
        return self.difficulty

    def set_name(self, name):
        self.name = name

    def set_difficulty(self, difficulty):
        self.difficulty = difficulty

    def update_dish(self, dish, ingredients):
        self.dishes[dish] = ingredients

    def get_dish_ingredients(self, dish):
        return self.dishes[dish]

    def find_dish_by_ingredient(self, ingredient):
        found_dishes = []
        for dish in self.dishes:
            if ingredient in self.dishes[dish]:
                found_dishes.append(dish)

        return found_dishes

    def to_string(self):
        s = "Station: " + self.name + "\nDifficulty: " + self.difficulty + "\nDishes:\n"
        for dish, ingredient in self.dishes.items():
            s += dish + ": " + ingredient
        return s

    def __eq__(self, other):
        return self.name == other.name

    def __hash__(self):
        return hash(self.name)

