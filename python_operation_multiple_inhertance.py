##class A:
##
##    def fun(self):
##        print("a")
##
##class B(A):
##
##    def fun(self):
##        print("b")
##
##class C(A):
##
##    def fun(self):
##        print("c")
##
##class D(C,B): #Multiple inheritance
##
##    def fun1(self):
##        print("d")
##
##d = D()
##d.fun()

##class A(object):
##
##    def fun(self):
##        print("a")
##
##class B(A):
##
##    def fun(self):
##        print("b")
##
##class C(A):
##
##    def fun(self):
##        print("c")
##
##class D(C,B): #Multiple inheritance
##
##    def fun1(self):
##        print("d")
##
##d = D()
##d.fun()

#Method Resolution Order
##It willgive priority to the near by search(during 3.X version of the python)
##During old version of oython i.e, 2.x search(during have done the deep search

##file_obj = open("devi.txt","w")
##file_obj.write("hello")
##file_obj.close()

##file_obj = open(r"C:\Users\sudar\Python Practise\devi.txt","w")
##file_obj.write("hello")
##file_obj.close()

##import tkinter #GUI, Forms, Frames, Buttons, Labels
##from tkinter import filedailog
##import os
##
##folder = filedailog.askdirectory()
##print(folder)
##
##file = os.path.join(folder,"sudhu.txt")
##
##file_obj = open(file, "w")
##file_obj.write("sudarshan")
##file_obj.close()


##import tkinter #GUI, Forms, Frames, Buttons, Labels
##from tkinter import filedialog
##import os
##
##folder = filedailog.askdirectory()
##print(folder)
##
##file = os.path.join(folder,"sudhu.txt")
##
##file_obj = open(file, "a")
##file_obj.write("sudarshan")
##file_obj.close()


import tkinter #GUI, Forms, Frames, Buttons, Labels
from tkinter import filedialog
import os

folder = filedialog.askdirectory()
print(folder)

file = os.path.join(folder,"sudhu.txt")

file_obj = open(file, "w")
file_obj.write("\n")
file_obj.write("suhhhhhhhhhhhhhdarshan")
file_obj.close()
