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
        print("The car belongs to Mr.Novin!")
        
		
car_1 = Eon("Eon","Hundai","Red",2011,500000)
car_1.display_owner()
car_1.display_info()





