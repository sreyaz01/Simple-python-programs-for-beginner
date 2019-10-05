print('programm to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings')

#taking list from user

l=[]
n=int(input('enter how many times you want to enter string = '))
for i in range(n):
    n1=input('type your string here = ')
    l.append(n1)

#finding strings which meets certain condition and and storing it in a new list 

l1=[]
for i in range(len(l)):
    n2=l[i] #acessing every sring in list creted by user
    if n2[0]==n2[-1] and len(n2)>=2: #checking condition
        l1.append(n2)
    
        
#Finding count of a new list and giving result to user
print('Processing your input....')
print('counting strings.....')
print('count of string is',len(l1))
