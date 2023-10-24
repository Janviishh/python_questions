# num = int(input('enter num'))
# fact = 1
# if num < 0:
#     print("factorial of 0 doesn't exist")
# if num == 0:
#     print("fact is 1")
# if num > 0:
#     for i in range(1,num+1) :
#         fact =fact *i   
#     print(fact)    


#     using recursion
def fact (a):
    if a == 0 :
     return 1
    else:
     return (a*(fact(a-1)))
num = int(input('enter a number here'))  
result = fact(num)    
print(result)  
