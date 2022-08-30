
#simple pyramid pattern

##def pypart(n):
##    for i in range(0, n):
##        for j in range(0, i+1):
##            print("*", end = "")
##        print("\r")
##n = 10
##pypart(n)



##def pypart(n):
##    myList =[]
##    for i in range(1, n+1):
##        myList.append("*" *i)
##        print("\n".join(myList))
##n = 3
##pypart(n)


##def pypart2(n):
##    k = 2*n - 2
##    for i in range(0, n):
##        for j in range(0, k):
##            print(end = " ")
##        k = k - 2
##        for j in range(0, i+1):
##            print("*", end=" ")
##            
##        print("\r")
##n = 5
##pypart2(n)


##def pypart2(n):
##    k = 2*n - 2
##    for i in range (0, n):
##        for j in range (0, k):
##            print(end = " ")
##        k = k - 2
##        for j in range (0, i+1):
##            print("*", end = " ")
##        print("\r")
##n = 5
##pypart2(n)


##def triangle(n):
##    k = n - 1
##    for i in range (0, n):
##        for j in range (0, k):
##            print(end = " ")
##        k = k - 1
##        for j in range (0, i+1):
##            print("*", end = " ")
##        print("\r")
##n = 5
##triangle(n)


##def triangle(n):
##    k = n - 2
##    for i in range (0, n):
##        for j in range (0, k):
##            print(end = " ")
##        k = k - 2
##        for j in range (0, i+1):
##            print("*", end = " ")
##        print("\r")
##n = 30
##
##triangle(n)



##def numpat(n):
##    num = 1
##    for i in range(0, n):
##        num = 1
##        for j in range(0, i+1):
##            print(num, end = "")
##            num = num+1
##        print("\r")
##n = 5
##numpat(n)
            

##def contnum(n):
##    num = 1
##    for i in range(0, n):
##        for j in range(0, i+1):
##            print(num, end=" ")
##            num = num + 1
##        print("\r")
##n = 5
##contnum(n)

##def alphapat(n):
##    num = 65
##    for i in range(0, n):
##        num = 65
##        for j in range(0, i+1):
##            ch = chr(num)
##            print(ch, end=" ")
##            num = num + 1
##        print("\r")
##
##n = 5
##alphapat(n)

##def alphapat(n):
##    num = 65
##    for i in range(0, n):
##        ch = chr(num)
##        for j in range(0, i+1):
##            print(ch, end=" ")
##            num = num+1
##        print("\r")
##
##n = 5
##alphapat(n)

##def contalpha(n):
##    num = 65
##    for i in range(0, n):
##        for j in range(0, i+1):
##            ch =chr(num)
##            print(ch, end = " ")
##            num = num + 1
##        print("\r")
##
##n = 5
##contalpha(n)
