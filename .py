num = int(input('enter no'))
if num==1:
    print('not prime')
elif num>1:
  for i in range(2,num):
    if num%i ==0:
      print('not prime')
      break
  else :
    print(f'{num} is primne') 