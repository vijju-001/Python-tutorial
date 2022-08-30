
#object "self" - created as hidden -why -because of constrcuture
#init = instant + initiliazer
#anything that has double underscore on either side is called "attributes" "magic methods"
#self is called object reference for inside class

##class My_Team:
##    """This is class defined with functions that takes arguments """
##
##    def __init__(self,name, age):
##        self.name = name
##        self.age = age
##
##    def first(self):
##        print(self.name)
##
##    def second(self):
##        print(self.age, self.name)
##
##n_team = My_Team("raina", 40)
##n_team.first()
##n_team.second()
##print(n_team.__doc__)

#n_team is called  single object instant reference for outside activity
#nn_team is  called constructor
#by default all the constructor will have one hiddenargument in the first position
#n_team is an object reference

class My_India:
    """This is class defined with functions that takes arguments """
    
    def __init__(self,name,country, age):
        self.name = name
        self.country = country
        self.age  = age

    def one(self):
        print(self.name)

    def two(self):
        print("He is", self.name,"from", self.country)

    def three(self):
        print(self.country)

    def four(self):
        print(self.age)


My_Nation = My_India("Yuvraj","India", 40)
My_Nation.one()
My_Nation.two()
My_Nation.three()
My_Nation.four()
print(My_Nation.__doc__)



#doc string means when ever we creat class we need to write something about class
#Just for calling the fuctions we use doc string





