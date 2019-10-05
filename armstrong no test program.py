print('Program to test Armstrong Number')
n=int(input('Enter Number to check if it is armstrong number or not = '))
print('Checking your number...')

#Armstrong Number= for n digit no (1**n+2**n+......+n**n) = number itself

#Intialisng Count and sum for while loop
count=0
Sum=0

#For calculating digit in number(n)
tempn=n
while tempn>0:
    tempn=tempn//10
    count+=1
    
#Finding Armstrong number
tempn=n
while tempn>0:
    r=tempn%10
    Sum=Sum+(r**count)
    tempn=tempn//10

if Sum==n:
    print('your no is armstrong number')
else:
    print('Your no is not armstrong number')
    
    
