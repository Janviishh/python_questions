num = int(input('enter the number'))
if num == 1:
    print('not a prime number')
if num >1 :
    for i in range(2,num) :
        if num %i ==  0:
          print('not a prime no')
          break
    else:
    
       print(f'{num} is a prime number')        