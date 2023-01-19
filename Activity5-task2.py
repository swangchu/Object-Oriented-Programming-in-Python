class Car:
    def __init__(self,c_name,c_brand,c_color,c_model,c_price):
        self.name = c_name
        self.brand = c_brand
        self.color= c_color
        self.model= c_model
        self.price= c_price

    def display_info(self):
        print("Car name:",self.name)
        print("Car brand:",self.brand)
        print("Car color:",self.color)
        print("Car model:",self.model)
        print("Car price:",self.price)

class Eon(Car):
    def display_owner(self):
        print("The car belongs to Mr. Novin!")


class Santro(Car):
    def display_info(self):
        print("-----------------------------")
        print("Car name:",self.name)
        print("Car brand:",self.brand)
        		

eon = Eon("Eon","Hundai","Red",2011,500000)
eon.display_owner()
eon.display_info()

santro=Santro("Santro","Hundai","Black",2011,600000)
santro.display_info()


