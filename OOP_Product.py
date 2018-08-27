class Product(object):
    def __init__ (self,price,item_name,weight,brand):
        self.price = price
        self.item_name = item_name
        self.weight = weight
        self.brand = brand
        self.status = "for sale"

    def sell(self):
        self.status = "Sold"
        return self
    
    def add_tax(self,tax):
        self.tax = tax 
        self.price = float(self.price) + float(self.tax)
        print "============================================="
        print " The price now is " + str(self.price) + " < Tax included >"
        print "============================================="

        return self
    


    def Return(self,reason):
        if reason =="defective":
            self.price = 0
            self.status = "defective"

            print "Price changed : $ "+str(self.price) +" < defective > "
            print "============================================="
        if reason =="new":
            self.status = "for sale"
        if reason == " used":
            self.price = self.price * 0.2
            print "============================================="
            print "Price changed : $ "+str(self.price) +" < 20 percents discount applied because the box has been opened > "
            print "============================================="
        return self

    def display_all(self):
        print "============================================="

        print " price: " + str(self.price)
        print " price: " + str(self.item_name)
        print " price: " + str(self.weight)
        print " price: " + str(self.brand)
        print " price: " + str(self.status)  
        print "============================================="

        return self
#==== Create instance and run method ========
item1 = Product(3000,"Bag","5KG","LV")
item1.add_tax(9.5)
item1.Return("new")
item1.display_all()

#==== items2 ========
item2 = Product(3000,"shirt","1KG","banana")
item2.add_tax(9.5)
item2.Return("defective")
item2.display_all()