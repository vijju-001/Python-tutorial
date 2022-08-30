##var = {}
##print(type(var))
##
##var = {"djbravo",33,"india"}
##print(type(var))
##
##var = {"name":"djbravo","Age":33,"country":"india"}
##print(var)
##print(type(var))
###python dictionary is called key value pair
###no index based manipulation
###keys www store should be unique
##
##var = {"name":"djbravo","Age":33,"country":"india"}
##print(var[0])#dict is not work with help og index numbers that is why it is called no index based manipulation

##

##var = {"name":"djbravo","Age":33,"country":"india"}
##print(var["name"])
##
##var = {"name":"djbravo","Age":33,"name":"india"}
##print(var["name"])
##
##var = {"name":"djbravo","Age":33,"country":"india"}
##var ["name"] = "kohli"
##print(var)
##
##var = {"name":"djbravo","Age":33,"country":"india"}
##output = var["team"]
##print(output)
##
##var = {"name":"djbravo","Age":33,"country":"india"}
##output = var["team"]
##print(output)
###result as none because it is key error
##var = {"name":"djbravo","Age":33,"country":"india"}
##output = var.get["team","sorry"]
##print(output)
##print("welcom to india")
#we have use .get method that time andd mention sorry in var data

##var = {"name":"dhoni"}
##var1 = {"age":33}
##output = var + var1
##print(output)
##
##var = {"name":"dhoni"}
##var1 = {"age":33}
##var.update(var1)
##print(var)
###we can use .update method for joint
##
##var = {"name":"dhoni"}
##var1 = {"age":33}
##output = {**var, **var1}
##print(var)
##
##var = {"name":"sudarshan",3:"rohit",4.5:"ashwin",("a","b"):"welcom")
##print (var)
##
##var = {"true":"ab",1:"bc",1.0:"cd"}
##print(var["true"])


##var = {"name":"sudarshan",3:"rohit",4.5:"ashwin",("a","b"):"welcom"}
##for x in var:
##    print(x)
##    

##var = {"name":"sudarshan",3:"rohit",4.5:"ashwin",("a","b"):"welcom"}
##for x in var.keys():
##    print(x)
####    
##
##var = {"name":"sudarshan",3:"rohit",4.5:"ashwin",("a","b"):"welcom"}
##for x in var.items():
##    print(x)
##    
##
##var = {"name":"sudarshan",3:"rohit",4.5:"ashwin",("a","b"):"welcom"}
##for x in var.values():
##    print(x)

##
##for x in range(10):
##    print(x)
##
##for x in range (1,10):
##    print(x)
##
##for x in range (1,10,2):
##    print(x)   
##
##for x in range (10,1,-1):
##    print(x)   



#comprision means writing code in smallest way

##my_list = []
##for x in range(10):
##    if x%2 == 0:
##        my_list.append(x)
##
##print(my_list)
####
##my_list = [x for x in range(10) if x%2 == 0]
##print(my_list)
#list based

###output = {0:0,1:1,2:4,3:9}
##
##my_dict = {}
##for x in range(4):
##    my_dict[x] = x*x
##print(my_dict)
##
##my_dict = {x:x*x for x in range (4)}
##print(my_dict)




