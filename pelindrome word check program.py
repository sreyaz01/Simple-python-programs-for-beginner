print('Program to check if String is Pelindrome or Not')
str=input('Enter your String to check if its Palindrome or not = ' )
print("Processing...")

p=str.lower() #to avoide case sensitive issues coverting input in lower case

p1=p[: : -1] #Reversing string

#print(p)
#print(p1)

if p1==p:
    print("String is Palindrome")
else:
    print("String is not Palindrome")
