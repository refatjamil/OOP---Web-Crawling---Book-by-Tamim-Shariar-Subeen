class Vehicle:
    """Base class for all vehicles"""

    def __init__(self,name,manufacturer,color):
        self.name = name
        self.maufacturer = manufacturer
        self.color = color

    def turn(self, direction):
        print("Turning", self.name, "to", direction)

class Car(Vehicle):
    """Car class""" 

    def __init__(self, name, manufacturer, color,year):

        self.name = name
        self.maufacturer = manufacturer
        self.color = color
        self.year = 2017
        self.wheels = 4

    def changer_gear(self,gear_name):
        """ Method of changer the gear """
        print(self.name, "is changing gear to", gear_name)

    def turn(self,direction):
        print(self.name, "is turning", direction)


if __name__ == "__main__":

    v = Vehicle("Softail Delux", "Harley-Davidson","Blue")
    v.turn("right")

    c = Car("Mustang 5.0 GT Coupe","Ford","Red","2017")
    c.turn("right")