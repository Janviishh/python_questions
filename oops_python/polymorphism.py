#METHOD OVERRIDING parent class and child class having same methods i.e. buy 
class Phone:
    def __init__(self,price,brand,camera):
      print ("inside phone constructur")
      self.__price=price
      self.brand=brand
      self.camera=camera
    def buy(self):
       print("buying a phone")
class Smartphone(Phone):
    def buy(self):
       print("buying a smartphone")
s=Smartphone(2000,"iphone",13)   
s.buy()    

#.super()is used toacces the methods of parent class
#Types of inheritence
#method overloading 
class Geomectry:
   def area(self,radius):
      return 3.14*radius*radius
   def area(self,l,b):
      return l*b
   #above is wrong because technically method overloading does not exist in python but we can do same thing by using below method
class Geomectry:
   def area(self,a,b=0):
      if b==0:
        print("circle",3.14*a*a)
      else:
         print("Rect",a*b)
obj=Geomectry()

obj.area(4) 
obj.area(4,5)         
#operator overloading
  