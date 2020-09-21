


class car:
    def __init__(self,make="unknown",model="unknown",color="unknown",price=-1,year=-1):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.price = price

newCar = car()
newCar = car('ford','mustang','orange','25000','2020')
print(newCar.model)
