class Vehicle:
    """Base class for all vehicles"""

    def __init__(self,name,manufacturer,color):
        print("Creating a vehicel")
        self.name = name
        self.maufacturer = manufacturer
        self.color = color
        
    def turn(self, direction):
        print("Turning", self.name, "to", direction)


class Car(Vehicle):
    """Car class""" 

    def __init__(self, name, manufacturer, color,year):
        print("Creating a car")
        super().__init__(name,manufacturer,color)

        self.year = 2017
        self.wheels = 4

if __name__ == "__main__":
    
    v = Vehicle("rifat","pop","brown")
    print(v.name)
    print(v.turn("r"))

    c = Car("Mustang 5.0 GT Coupe","Ford","Red",2016)
    print(c.name,c.year,c.wheels)


    print(len(dir(Car)),"Car")
    print(dir(Car))
    
    print(len(dir(c)),"c")
    print(dir(c))

    print(len(dir(Vehicle)),"Vehicle")
    print(dir(Vehicle))    