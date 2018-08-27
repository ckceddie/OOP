# OOP Bike

# define the Bike class

class bike(object):
    def __init__ (self , price , max_speed):
        self.price = price
        self.max_speed = max_speed
        self.miles = 0


    def displayInfo(self):
        print "bike's price is " + str(self.price)
        print "maximum speed : " + str(self.max_speed)
        print "the total miles : "+str(self.miles)
        return self
    

    def ride(self):
        print "Riding : "
        self.miles += 10
        print "the miles is "+str(self.miles)
        return self

    def reverse(self):
        print "Reversing : " 
        self.miles -= 5
        print "the miles is "+str(self.miles)
        return self


# create instances and run methods
bike1 = bike(99.99, 12)
bike1.displayInfo()
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

bike2=bike(1000,20)
bike2.displayInfo()

