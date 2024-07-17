# function is a block of cod that runs when we call it 
# it can help in cod reuse

def ronakFunction():     # function defination 
    print("hello world")
    print("hello ronak")
    print(10+11)
    
ronakFunction()          # function calling
ronakFunction()    
ronakFunction()
ronakFunction()
ronakFunction()

# function with parameter (argyuments)


def sum(a,b):
    print(a/b)
    
sum(4,2)
sum(8,4)

def multiplication(a):
    print(a*a)
    
multiplication(24)
multiplication(25)
multiplication(88)
multiplication(16)

# function with return type 

def div(a,b):
    return a/b

x =div(30,40)

print(x)


def display(fname,lname):
    print("First name is", fname)
    print("lastname is", lname)
    
# need function 
display(lname="naik",fname="ronak") # use parameter name while calling

##############################################

def display2(*a):
    print("value : =>",a[10])
    for x in a:
        print(x)
        
display2(1,2,3,4,5,6,7,8,9,11,21,20,25,24,262,45)

