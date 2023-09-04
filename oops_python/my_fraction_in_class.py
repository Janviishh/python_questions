from my_fraction_in_class import Fraction
# The above class represents a fraction.
class Fraction:
    def __init__(self,n,d) :
        """
        The above function is the constructor for a class with two parameters, n and d.
        
        :param n: The parameter "n" is used to represent the name of an object or entity. It could be a
        string or any other data type that represents the name of the object
        :param d: The parameter "d" in the above code represents the value for the attribute "d" of the
        object being initialized
        """
        self.num=n
        self.den=d
    def __str__(self):
        return "{}/{}".format(self.num,self.den) 
'''y=fraction(5,3)
print(y)'''

def __add__(self,other):
  temp_num=self.num*other.den+self.den*other.num
  temp_den=self.den*other.den
  return "{}/{}".format(temp_num,temp_den)
x=Fraction(3,4)
y=Fraction(3,2)
z=x+y
print(z)
