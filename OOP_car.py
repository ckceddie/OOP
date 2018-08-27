class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed =speed
        self.fuel = fuel
        self.mileage = mileage


    def  display_all(self):
        if self.price > 10000 :
            tax = 0.15
        else:
            tax = 0.12
        print "============================================="
        print  "Price :" +str(self.price)
        print "Speed :" + str(self.speed)
        print "fuel :" + str(self.fuel)
        print 'mileage :' + str(self.mileage) + "mpg"
        print 'tax :' + str(tax)
        print "============================================="

        return self


myCar = Car(5000,5000,"FULL",10000)
myCar.display_all()

yourCar = Car(15000,5000,"FULL",10000)
yourCar.display_all()


myCar1 = Car(200,5000,"half",3000)
myCar1.display_all()

myCar2 = Car(300,5000,"FULL",10000)
myCar2.display_all()

myCar3 = Car(25000,5000,"FULL",10000)
myCar3.display_all()

myCar4 = Car(500000,5000,"FULL",10000)
myCar4.display_all()