print('Program to Reverse a Tuple')
#creting a user define list
l=[]
n=int(input('enter how many times you enter data = '))
for i in range(n):
    n1=input('enter your input here to make a tuple = ')
    l.append(n1)

#converting list into tuple
t=tuple(l)
print('your input is',t , type(t))

#reversing tuple
t1=t[: : -1] #using slicing to reverse tuple
print('reversing your input now...')
print('reverse order of your input',t1)
