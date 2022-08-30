##var = 10/0
##print(var)

##try:
##    var =  10/0
##    print(var)
##except:
##    print("sorry")
##print("welcome")

##try:
##    var =  "a" + 5
##    print(var)
##except:
##    print("sorry")
##print("welcome")

##try:
##    var =  10/0
##    print(var)
##except TypeError:
##    print("sorry")
##print("welcome")

##try:
##    var =  "a"+ 10
##    print(var)
##except TypeError:#default exception
##    print("sorry")
##print("welcome")

##try:
##    var =10/0
##    print(var)
##except ZeroDivisionError:#default exception
##    print("sorry")
##print("welcome")

##try:
##    var =  "a"+ 10
##    print(var)
##except TypeError:
##    print("sorry")
##except:
##    print("Oops")
##print("welcome")


##try:
##    var =  "a"+ 10
##    print(var)
##except:
##    print("sorry")
##except TypeError:
##    print("Oops")
##print("welcome")
##except:
##    print("sorry")


##try:
##    var =10/0
##    print(var)
##except TypeError as ex:
##    print(ex)
##except ZeroDivisionError as ex:
##    print(ex)
##    print("krishna")
##except:
##    print("Oops")
##print("welcome")

##try:
##    var =10/0
##    print(var)
##except (TypeError,ZeroDivisionError) as ex:
##    print(ex)
##except:
##    print("Oops")
##print("welcome")


##try:
##    var =10/5
##    print(var)
##except (TypeError,ZeroDivisionError) as ex:
##    print(ex)
##except:
##    print("Oops")
##else:
##    print("welcome")

##try:
##    var =10/0
##    print(var)
##except (TypeError,ZeroDivisionError) as ex:
##    print(ex)
##except:
##    print("Oops")
##else:
##    print("welcom")

##try:
##    var =10/0
##    print(var)
##except (TypeError,ZeroDivisionError) as ex:
##    print(ex)
##except:
##    print("Oops")
##else:
##    print("welcome")
##finally:
##    print("hhhhhhhhh")

##try:
##    var =10/4
##    
##    print(var)
##except (TypeError,ZeroDivisionError) as ex:
##    print(ex)
##except:
##    print("Oops")
##else:
##    print("welcome")
##finally:
##    print("hhhhhhhhh")

##try:
##    var =10
##    if var>5:
##        raise IndexError
##
##except IndexError:
##    print("kkkfhfhfhfh")

##try:
##    var =10
##    if var>5:
##        raise IndexError
##
##except IndexError as ex:
##    print(ex)

##try:
##    var =10
##    if var>5:
##        raise IndexError("Darshan is the best person in the world")
##
##except IndexError as ex:
##    print(ex)

##try:
##    var =10
##    if var>5:
##        raise MyError("Darshan is the best person in the world")
##
##except MyError as ex:
##    print(ex)


##try:
##    var =10
##    if var>5:
##        raise TypeError("Darshan is the best person in the world")
##
##except TypeError as ex:
##    print(ex)


##try:
##    var =10
##    if var>5:
##        raise ZeroDivisionError("Darshan is the best person in the world")
##
##except ZeroDivisionError as ex:
##    print(ex)


#IMP QUESTION: How can you raise user defined Exception5


##class MyError(Exception):
##    pass
##try:
##    var =10
##    if var>5:
##        raise MyError("Darshan is the best person in the world")
##
##except MyError as ex:
##    print(ex)


##class MyError(Exception):
##    var = "Dhoni is my hero"
##try:
##    var =10
##    if var>5:
##        raise MyError
##
##except MyError as ex:
##    print(ex.var)

##class MyError(Exception):
##    var = "Dhoni is my hero"
##try:
##    var =10
##    if var>5:
##        raise MyError
##
##except MyError:
##    print(MyError.var)

##if 2>1:
##    print("2>1")




if 
