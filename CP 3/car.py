class Car:
    def __init__(self, n, c, m, y, cc):
        self.name = n
        self.manufacturing = m
        self.color = c 
        self.year = y
        self.cc = cc

    def start(self):
        print(f"{self.name} Starting the engine")

    def brake(self):
        print(f"{self.name} brake the engine")

    def drive(self):
        print(f"{self.name} drive the engine")

    def turn(self):
        print(f"{self.name} turn the engine")

    def chge(self):
        print(f"{self.name} chge the engine")        

 



car = Car("Corolla", "White", "corola company",2010,200)
car.start()
car.brake()
car.drive()
car.turn()
car.chge()

