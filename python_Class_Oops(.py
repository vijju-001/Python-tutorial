#class is template
#class is going to have everything needed for the program to execute
#class in general is called collection of objects
#class is to form a structure

##var = "Sudarshan"
##def fun():
##    print("Poojary")
##
##print(var)
##fun()
#It is called unstructured way calling functionality


##class Netzwerk:
##    var = "Sudarshan"
##    def fun():
##        print("Poojary")
##
##print(Netzwerk.var)
##Netzwerk.fun()

##class Netzwerk:
##    var = "Sudarshan"
##    def fun():
##        print("Poojary")
##n_obj = Netzwerk
##print(n_obj.var)
##n_obj.fun()

#Above all non constructured based class
#class without a constructure
#n_obj = external object references - it will creat separate memory -
#it is single memory,single onject referencesa


#with Constructured
#just use () it is called construtrueed
#in constructered n_obj is instant objt not normal object
##class Netzwerk:
##    var = "Sudarshan"
##    def fun(self):
##        print("Poojary")
##
##
##n_obj = Netzwerk()
##print(n_obj.var)
##n_obj.fun()

##class Netzwerk:
##    
##    def fun(Hemu,name):
##        print(name)
##
##    def new(Hemu,name):
##        print(name)
##
##
##n_obj = Netzwerk()
##n_obj.fun("kohli")
##n_obj.new("kohli")

class Netzwerk:
    def__init__(hemu,name):
        hemu.name = name
    
    def fun(hemu):
        print(hemu.name)

    def new(hemu):
        print(hemu.name)


n_obj = Netzwerk("kohli")
n_obj.fun()
n_obj.new()

#here self and hemu is reference ,it is important for class.
