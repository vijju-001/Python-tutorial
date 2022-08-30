

##var = []
##print(type(var))

##var = ["dhoni",55,66,44.5,"ab",["a","b"]]
##print(var)

##var = ["dhoni",55,66,44.5,"ab",["a","b"]]
##print(type(var))

##var = ["a","b","c"]
##var[1] = "d"
##print(var)

##var = ["a","b","c"]
##print(dir(var))

##var = ["a","b"]
##var1 = ["c","d"]
##print(var + var1)

##a = ["sudarshan","sriraj","hemu","karthik"]
##b = a #shallow copy #important topic for interview
##print(a)
##print(b)
##b [0] = "dhanu"
##print(a)
##print(b)

##a = ["sudarshan","sriraj","hemu","karthik"]
##b = a[:] #deep copy  #iimportant topic for interview
##print(a)
##print(b)
##b [0] = "dhanu"
##print(a)
##print(b)

##var = ["a","b","c"]
##var[0] = "sudarshan"
##print(var)
##print(type(var))

##var = ["a","b","c"]
##var.append("sudarshan")
##print(var)

##var = ["a","b","c"]
##var.extend(["kohli","sudarshan"])
##print(var)


##var = ["dhoni","ate","cat","apple","goat"]
##var.pop(2)
##print(var)

##var = ["dhoni","ate","cat","apple","goat"]
##var.remove("ate")
##print(var)

##var = ["dhoni","ate","cat","apple","goat"]
##var.clear()
##print(var)
  
##var = ["dhoni","ate","cat","apple","goat"]
##del var [4] #should be in sqaure brackets - important topic
##print(var)

##var = ["a","b","c","d"]
##var.extend(("dhoni","kohli"))
##print(var)


##var = ["a","b","c","d"]
##output = var.extend(("dhoni","kohli"))
##print(output)
##
###result is none because we are used here existiing varibale that is why it is showing none result
##var = ["a","b","c","d"]
##print(var.extend(("dhoni","kohli")))
###result is none because we are used here existiing varibale that is why it is showing none resu

##var = ["ram","shankar","garu",45,67,88,23,45,"raju","vikki"]
##var.sort()
##print(var)

##var = ["ram","shankar","garu","raju","vikki"]
##var.sort()
##print(var)

##var = ["ram","shankar","garu","raju","vikki"]
##var.sort(reverse = True)
##print(var)

##var = ["ram","shankar","garu","raju","vikki"]
##var.sort(key = len)
##print(var)
##var = ["ram","shankar","garu","raju","vikki"]
##output = sorted(var,reverse = True)
##print(output)

##var = ["ram","shankar","garu","raju","vikki"]
##output = sorted(var)
##print(output)
##
##
##var = ["ram","shankar","garu","raju","vikki"]
##output = sorted(var,key = len)
##print(output)

#Difference between sort and sorted
#sort- will not written the data,we should work on existing variable, do the operations and print existing variable
#sorted- It will written the data, takes existing variable and also copy to another variable





































































##var = ("ram","bhima")
##print(type(var))

##var = ("a","b")
##var[0] = "dhoni"
##print(var)

##var = ("a","b")
##print(dir(var))

##var = ("ram",)
##print(type(var))
##
##tup = (21,24,56,7,87,86,45)
##tup[1] =45
##print(dir(tup))

##tup.count(2)
##print(tup)

##s = {1,2,3,4,5,6,6,7,8,9}
##print(dir(s))


