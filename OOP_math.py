class Math(object):
    def __init__(self):
        self.results = 0

    def add(self,*num):
        for i in num:
            self.results+=i 
        return self

    def subtract(self,*num):
        for i in num:
            self.results-=i
        return self

    def result(self):
        print "===================================="
        print "The result is " + str(self.results)
        print "===================================="
        return self 

md=Math()
md.add(2).add(2,5).subtract(3,2).result()