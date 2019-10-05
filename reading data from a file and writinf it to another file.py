
print('Program to read data from a file and copy it on another file')

def copy():
    try:
        fname=input('enter your file name to read file ') 
        f=open(fname+'.txt','r') #opening file to read data
        data=f.read() #storing all data in a variable
        ufile=input('enter your  newfile name to copy data on new file ')
        file=open(ufile+'.txt','a') #creating a new file to write data on it
        file.write(data) #writing data on file
        file.flush()
        file.close()
        f.close()
    except FileNotFoundError:
        print('file to copy data from is not found please enter valid file name')
        copy()

    
    
copy()
