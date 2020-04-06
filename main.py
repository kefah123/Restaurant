from Kitchen import Kitchen


# This program simulates a simple restaurant kitchen

def main():
    the_spot = Kitchen()
    # Adding stations
    the_spot.add_station("Apps")
    the_spot.add_station("Grill")
    the_spot.add_station("Saute")
    the_spot.add_station("Cold")

    # Adding cooks
    the_spot.add_cook("Kwasi", 23, 14, "Morning", "Apps")
    the_spot.add_cook("Karyka", 21, 16, "Morning", "Grill")
    the_spot.add_cook("Qui", 29, 21, "Night", "Saute")
    the_spot.add_cook("Dana", 29, 21, "Night", "Grill")
    the_spot.add_cook("Yosef", 21, 14, "Night", "Apps")
    the_spot.add_cook("Lucy", 22, 14, "Morning", "Cold")

    # updating difficulties
    the_spot.update_station_difficulty("Apps", "Moderate")
    the_spot.update_station_difficulty("Grill", "Hard")
    the_spot.update_station_difficulty("Saute", "Hard")
    the_spot.update_station_difficulty("Cold", "Easy")

    # updating dishes
    the_spot.update_station_dish("Apps", "Fried Calamari",
                                 ("Frozen Calamari", "Scallions", "Black Sesame Seeds", "Ponzu Sauce"))
    the_spot.update_station_dish("Apps", "Avocado Fries",
                                 ("Frozen breaded avocado slices", "Sweet Chili Aioli", "Lime Wedge"))
    the_spot.update_station_dish("Saute", "Ahi Tuna",
                                 ("Raw Ahi Tuna", "Scallions", "Black Sesame Seeds", "Green Goddess Dressing",
                                  "Fried rice"))
    the_spot.update_station_dish("Grill", "Cheesesteak",
                                 ("Raw Steak", "Cheddar Cheese", "Hoagie Bun", "Onions", "Peppers"))
    the_spot.update_station_dish("Grill", "Cheeseburger",
                                 ("Raw beef patty", "Brioche Buns", "Lettuce", "Onions", "Tomatoes", "Cheddar Cheese"))
    the_spot.update_station_dish("Cold", "Cloudbreak Salad",
                                 ("Mixed greens", "Black beans", "Tomatoes", "Eggs", "Chicken", "Goat Cheese"))

    # Outputs to demonstrate functionality

    print("WELCOME TO THE SPOT ON THE DOCK!\n")

    print("OUR TEAM FOR THIS YEAR IS MADE UP OF:\n")
    for cook in the_spot.get_cooks():
        print(cook.to_string() + "\n")

    print("WE WILL BE RUNNING THE FOLLOWING STATIONS:\n")
    for station in the_spot.get_stations():
        print(station.to_string() + "\n")

    print("WE ARE CURRENTLY LOW ON BLACK SESAME SEEDS. THESE ARE THE DISHES THAT USE THEM: ")
    for dish in the_spot.find_dish_using_ingredient("Black Sesame Seeds"):
        print(dish)


main()
