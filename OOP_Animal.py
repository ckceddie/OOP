class Animal(object):
    def __init__(self,name):
        self.name = name
        self.health = 100

    def walk(self):
        # decreases health by one
        self.health-=1
        return self
    
    def run(self):
        # health decreases by five
        self.health-=5
        return self
    def dislpay_health(self):
        # display health: print to the terminal the animal's health.
        print "======================================================"
        print str( self.name) +"'s health is "+ str(self.health)
        print "======================================================"
        return self



dog3 = Animal("Edmond")
dog3.walk().walk().walk().dislpay_health()
dog3.run().run().dislpay_health()



class Dog(Animal):
    def __init__(self,name):
        super(Dog, self).__init__(name)
        # default health of 150
        self.health=150
        
    def pet(self):
        self.health+=5 
        return self 

    

dog1=Dog("carmen")
dog1.walk().walk().walk().run().run().pet().dislpay_health()


class Dragon(Animal):
    def __init__(self,name):
        super(Dragon,self).__init__(name)
        self.health=170
    
    def fly(self):
        self.health -=10
        return self 
    
    def dislpay_health(self):
        print " This is Dragon"
        super(Dragon,self).dislpay_health()
        return self

a=Dragon('vincent')
a.fly().dislpay_health()

