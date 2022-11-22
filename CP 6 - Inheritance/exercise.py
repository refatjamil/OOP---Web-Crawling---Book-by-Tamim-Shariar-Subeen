class Vehicel:

    def __init__(self, name, manufacturer, color):
        self.name = name
        self.manufacturer = manufacturer
        self.color = color


    def start(self):
        print(self.name,"Starting....BOOoommM!")

    def dirve(self):
        print(self.name, "Driveing..")

    def stop(self):
        print(self.name, "Stop") 

 

class MotorCycle(Vehicel):
    def __init__(self, name, manufacturer, color,wheel):
        self.wheel = wheel
        self.name = name
        super().__init__(name, manufacturer, color)

    def motogear(self,gear):
        print(self.name, "power is",gear)

    def company(self):
        print(self.manufacturer,"Beasd and",self.wheel,"wheel")       


class Car(Vehicel):
    """Car class"""

    def __init__(self, name, manufacturer, color, year):
        super().__init__(name,manufacturer,color)
        self.color = color
        self.year = year
        self.wheels = 4
    
    def change_gear(self,gear_name):
        """Method for changing gear"""
        print(self.name,"is chaning gear to",gear_name)

    def car_dt(self):
        print("name:",self.name,"manufac:",self.manufacturer,)    

if __name__ == "__main__":
    mc = MotorCycle("Apace RTR","TVS","Red",2)
    c = Car("Mustang 5.0 GT Coupe","Ford","Red", 2017)


    mc.motogear(150)
    c.change_gear("right")
    c.car_dt()