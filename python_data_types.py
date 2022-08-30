##print("hi")

##print(help())

##Sublime as Python Editior
##it is same like idle to  run code


##More on  variables


##num = 5
##print(id(num))
# use to find out address of number

##name = "sudarshan"
##print(id(name))

##a = 10
##b = a
##print(a)
##print(b)
##print(id(a))
##print(id(b))
#if use multiple variable with same value it will get same address,it will point to same bpx address, not multliple box address
#that is why python is called more memory effient.
##print(id(10))


##in memory a=10,b=a,so b=10, a= 9,k=a, b=8 in this case a nad k is refering to 9, and b is refering
##to 8, no one is refering 10 , but 10 is there in the memory no one using it -
##---- this connect called garbage collection

#concept of constant variable



#DATA TYPES IN PYTHON
#FORMAT OF DATA have to use in python.date in format, we have to process data in particular format
#if we dont process data in particular data type we might face error or bugs
5
#None, Numeric,List,Tuple,set,string,range,dictionery

#NONE - when u have a variable, But that variables not assigned with any value it si none.
#other language null - in python none
#Numeric - int, float,complex,bool
#ex:
##num = 2.5 - float
##num = 5 -int
##num = a+bj - complex type j means square -1

##num = 6+7j
##print(type(num))

#complex menas we have a number + imaginary number

#####covert#float to intiger (int)
##a = 5.6
##b = int(a)
##print(type(b))
##print(b)
##
###int to float
##k = float(b)
##print(k)
##
###normal to complex
##k = 6
##b =5
##c = complex(b,k)
##print(c)
##
###BOOL it is means true and false
##print(b<k)
##
##bool = b<k
##print(type(bool))
##
##print(b>k)
##
####convert to number
##print(int(True))
##print(int(False))

#SEQUENCES = LIST, TUPLE,SET,STRING AND RANGE
#range
##range(0,10)
##print(list(range(0,10)))
##
##print(list(range(1,10,2)))

# all this comes under SEQUENCES
#key should be unique
##d = {}
##d.get()
##d.key()
##d.values()
##d.item()

