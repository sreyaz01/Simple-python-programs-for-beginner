print('Program to reverse a no through while loop')
n=int(input('enter your no to reverse it '))
a=0
while n>0:
    r=n%10 #calculating reminder
    a=(a*10)+r #to calculate next no to devide
    n=n//10 #opration for while loop
print("now reversing no")
print ('result is ',a)
    
