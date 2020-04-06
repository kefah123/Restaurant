from Station import Station


class Cook:
    def __init__(self, name, age, wage, shift, id_no, station_name):
        self.name = name
        self.age = age
        self.wage = wage
        self.shift = shift
        self.id_no = id_no
        self.station = Station(station_name)

    def get_id_no(self):
        return self.id_no

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_wage(self):
        return self.wage

    def get_shift(self):
        return self.shift

    def get_station(self):
        return self.station

    def set_station(self, station_name):
        self.station = Station(station_name)

    def set_name(self, name):
        self.name = name

    def set_age(self, age):
        self.age = age

    def set_wage(self, wage):
        self.wage = wage

    def set_shift(self, shift):
        self.shift = shift

    def to_string(self):
        s = "Name: " + self.name + "\n"
        s += "ID: " + str(self.id_no) + "\n"
        s += "Age: " + str(self.age) + "\n"
        s += "Wage: " + str(self.wage) + "\n"
        s += "Shift: " + self.shift + "\n"
        s += "Station: " + self.station.name
        return s


    def __eq__(self, other):
        return self.id_no == other.id_no

    def __hash__(self):
        return hash(self.id_no)

