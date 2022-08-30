##def fun():
##    print("Hello")
##    print("Welcome to HDFC")
##
##fun()
##fun()
##fun()

##def fun(var):
##    print("Hello", var)
##    print("Welcome to HDFC")
##
##fun("Hemu")
##fun("Shrre")
##fun("Deekshi")

##def fun(var,country):
##    print("Hello",var, "from",country)
##    print("Welcome to HDFC")
##
##fun("Hemu","India")
##fun("Shrre","Japan")
##fun("Deekshi","Austrelia")

##def fun(var="Dhoni",country="India"):
##    print("Hello",var, "from",country)
##    print("Welcome to HDFC")
##
##fun("Hemu")
##fun(country="Japan")
##fun("Deekshi","Austrelia")
##fun()
##fun("dhoni")

##def fun(var="Dhoni",country="India"):
##    if isinstance(var,str):
##        
##            print("Hello",var, "from",country)
##            print("Welcome to HDFC")
##
##fun("Hemu")
##fun(country="Japan")
##fun("Deekshi","Austrelia")
##fun()
##fun("dhoni")
##fun("ram","sidney")
##fun("kusha",98)

##def fun(var="Dhoni",country="India"):
##    if isinstance(var,str) and isinstance(country,str):
##        print("Hello",var, "from",country)
##        print("Welcome to HDFC")
##
##fun("Hemu")
##fun(country="Japan")
##fun("Deekshi","Austrelia")
##fun()
##fun("dhoni")
##fun("ram","sidney")
##fun("kusha",98)

##def passed_students(name):
##    print(name)
##
##passed_students("sudhu")

##def passed_students(*name):
##    print(name)
##
##passed_students("sudhu", "hemu","rama")

##def passed_students_details(**var):
##    print(var)
##
##passed_students_details(name = "sudhu",country="India")
##passed_students_details(name = "sadhu",country="japam")
##

##def students_marks(name, eng, kan):
##    total = eng+kan
##    return total, name
##print(students_marks("raina",56,78))


##class C_team:
##    var = "sudhu"
##    def fun():
##        print("hemu")
##
##my_team = C_team
##print(my_team.var)
##my_team.fun()

##class C_team:
##    
##    def fun(self):
##        print("hemu")
##        print("ram")
##
##my_team = C_team()
##my_team.fun()
##my_team.fun()

##class C_team:
##   def __init__(self,name):
##       
##       self.name = name
##       
##       def fun(self):
##           print(self.name)
##       def one(self):
##            print(self.name)
##
##My = C_team("ram")
##My.fun()
##My.one()



##class Bcom:
##    """This class is defined with functions that takes arguments"""
##
##    def __init__(self,name,age,country):
##
##        self.name = name
##        self.age = age
##        self.country = country
##
##    def fun(self):
##        print(self.name)
##
##    def one(self):
##        print(self.age,self.country)
##
##    def two(self):
##        print(self.country, self.name)
##
##    def three(self):
##        print(self.country)
##
##commerce = Bcom("sudhya",22,"India")
##commerce.fun()
##commerce.one()
##commerce.two()
##commerce.three()
##print(commerce.__doc__)




##class aaa:
##    """This class iss defined with functions that takes arguments"""
##
##    def __init__(self,name,age,country, marks):
##        self.name = name
##        self.age = age
##        self.country = country
##        self.marks = marks
##
##    def one(self):
##        print(self.name)
##
##    def two(self):
##        print(self.age)
##
##    def three(self):
##        print(self.country)
##
##    def four(self):
##        print(self.marks)
##
##    def five(self):
##        print(self.age, self.marks)
##
##
##bbb = aaa("rama",24,"srilanka",90)
##bbb.one()
##bbb.two()
##bbb.three()
##bbb.four()
##bbb.five()
##print(bbb.__doc__)

##def pypart(n):
##    for i in range(0,n):
##        for j in range(0, i+1):
##            print("*", end = "")
##
##        print("\r")
##
##n = 5
##pypart(n)

##
##def pypart(n):
##    my_list= []
##    for i in range(1, n+1):
##        my_list.append("*" *i)
##        print("\n".join(my_list))
##              
##
##n = 3
##pypart(n)
        
##
##def pypart(n):
##    k = 2*n -2
##    for i in range(0,n):
##        for j in range(0,k):
##            print(end = " ")
##        k = k-2
##        for j in range(0, i+1):
##            print("*",end = " ")
##
##        print("\r")
##n = 5
##pypart(n)


##def triangle(n):
##    k = n -1
##    for i in range(0,n):
##        for j in range(0,k):
##            print(end = " ")
##        k = k-1
##        for j in range(0, i+1):
##            print("*",end = " ")
##
##        print("\r")
##n = 5
##triangle(n)


##def numpat(n):
##    num = 1
##    for i in range(0,n):
##        num = 1
##        for j in range(0, i+1):
##            print(num,end = " ")
##            num = num+1
##
##        print("\r")
##n = 5
##numpat(n)


##def contnum(n):
##    num = 1
##    for i in range(0,n):
##        for j in range(0, i+1):
##            print(num,end = " ")
##            num = num+1
##
##        print("\r")
##n = 5
##contnum(n)


##
##def alphapat(n):
##    num = 65
##    for i in range(0,n):
##        num = 65
##        for j in range(0, i+1):
##            ch = chr(num)
##            print(ch,end = " ")
##            num = num+1
##
##        print("\r")
##n = 5
##alphapat(n)




def contalpha(n):
    num = 65
    for i in range(0,n):
        for j in range(0, i+1):
            ch = chr(num)
            print(ch,end = " ")
            num = num+1

        print("\r")
n = 5
contalpha(n)
