# prime numbers

num=12
for x in range(2,11):
    
 if num%2==0:
    print("is not prime ")
 else:
    print("num is prim") 
        
        
num=15 
for x in range(2,4):
    
    if num%x==0:
        print("not prime")
    else:
        print("num is prime") 

def prime(h):
     flag = True
     
     for x in range(2,h):
         if h%x == 0:
             flag = False
             break
         
     return flag

print()
print(prime(11))

   
        
        
      
        
    