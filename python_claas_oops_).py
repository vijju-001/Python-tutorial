
##class team:
##    def __int__(self,name):
##        
##        self.name = name
##
##    def fun(self):
##        print(self.name,"one")
##
##    def fun(self):
##        print(self.name,"two")
##
##In = team("raina")
##In.fun()
##In.one()


##var = "a"
##var = "b"
##print(var)

#python dont support function overloading
#python has access specifier, public private
#private access specifier can also be called as "Data Hiding"

####
##class team:
##    def __init__(self,name):
##        
##        self.name = name
##
##    def fun(self):
##        print(self.name,"one")
##
##    def __one(self):#private access specifier which can also be called data hiding
##        print(self.name,"two")
##
##In = team("raina")
##In.fun()
##In.one()
##

##class team:
##    def __init__(self,name):
##        
##        self.name = name
##
##    def fun(self):
##        print(self.name,"one")
##
##class two(team):#single inheritance
##    def one(ram):
##        print(ram.name,"two")
###python support all inheritance
##In = two("raina")
##In.fun()
##In.one()



##class team:
##    def __init__(self,name,age):
##        
##        self.name = name
##        self.age = age
##
##    def fun(self):
##        print(self.name,"one",self.age)
##
##class two(team):#single inheritance
##    def one(ram):
##        print(ram.name,"two")
###python support all inheritance
##In = two("raina",33)
##In.fun()
##In.one()



##class team:
##    def __init__(self,name,age):
##        
##        self.name = name
##        self.age = age
##
##    def fun(self):
##        print(self.name,"one",self.age)
##
##class two(team):#single inheritance
##    def __init__(ram,name):
##        ram.name = name
##        team.__init__(ram,ram.name,33)
##        
##    def one(ram):
##        print(ram.name,"two")
###python support all inheritance
##In = two("raina",54)
##In.fun()
##In.one()

##class team:
##    def __init__(self,name,age):
##        
##        self.name = name
##        self.age = age
##
##    def fun(self):
##        print(self.name,"one",self.age)
##
##class two(team):#single inheritance
##    def __init__(ram,name):
##        ram.name = name
##        #team.__init__(ram,ram.name,33)
##        super().__init__(ram.name,33)
##    def one(ram):
##        print(ram.name,"two")
###python support all inheritance
##In = two("raina")
##In.fun()
##In.one()

##class computer:
##    def __init__(self,name,storage,ram):
##        self.name = name
##        self.storage = storage
##        self.ram = ram
##
##    def one(self):
##        print(self.name)
##
##    def two(self):
##        print(self.storage, self.ram)
##
##class comp(computer):
##    def __init__(seef,name):
##        seef.name = name
##        computer.__init__(seef,seef.name,33,23)
##    def three(seef):
##        print(seef.name)
##
##comp1 = comp("lenovo")
##comp1.one()
##comp1.two()
##comp1.three()



class computer:
    def __init__(self,name,storage,ram):
        self.name = name
        self.storage = storage
        self.ram = ram

    def one(self):
        print(self.name, self.ram)
    def two(self):
        print(self.storage)

class comp(computer):
    def __init__(selfone,name):
        selfone.name = name
       #computer.__init__(selfone,selfone.name,128,8)
        super().__init__(selfone.name,128,8)
    def three(selfone):
        print(selfone.name)

comp1 = comp("lenova")
comp1.one()
comp1.two()
comp1.three()
















        
##class computer:
##    def __init__(self,name,storage,ram):
##        self.name = name
##        self.storage = storage
##        self.ram = ram
##
##    def one(self):
##        print(self.name)
##
##    def two(self):
##        print(self.storage, self.ram)
##
##class comp(computer):
##    def __init__(seef,name):
##        seef.name = name
##        super().__init__(seef.name,33,23)
##    def three(seef):
##        print(seef.name)
##
##comp1 = comp("lenovo")
##comp1.one()
##comp1.two()
##comp1.three()
    

##class Sales:
##    def __init__(self, id):
##        self.id = id
##        id = 100

##val = Sales(123)
##print (val.id)



##s = "\t\tWelcome\n"
##print(s.strip())






##class Person:
##    def __init__(self, id):
##        self.id = id
##
##sam = Person(100)
##
##sam.__dict__['age'] = 49
##
##print (sam.age + len(sam.__dict__))







##class A:
##    def __init__(self, i = 0):
##        self.i = i
##
##class B(A):
##    def __init__(self, j = 0):
##        self.j = j
##
##def main():
##    b = B()
##    print(b.i)
##    print(b.j)
##
##main()




##class A:
##    def __init__(self):
##        self.calcI(30)
##        
##    def calcI(self, i):
##        self.i = 2 * i;
##
##class B(A):
##    def __init__(self):
##        super().__init__()
##        print("i from B is", self.i)
##        
##    def calcI(self, i):
##        self.i = 3 * i;
##
##b = B()




##def sayHello():
##    print('Hello World!')
##sayHello()
##sayHello()



##def printMax(a, b):
##    if a > b:
##        print(a, 'is maximum')
##    elif a == b:
##        print(a, 'is equal to', b)
##    else:
##        print(b, 'is maximum')
##printMax(3, 4)
