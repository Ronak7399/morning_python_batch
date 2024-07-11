# number // string // boolean 
# list

# list => group oof datatype under single datatype name

data = [12,34,15,16,17,18,24,25,26,30,40]

print(data)
print(type(data))

values = [121212,12,34,"bascom",'jimit',True]

# we can acces list values using index

print(values) 
print(type(values))

print(values[4])
values[2] = "maru bascom"

print (values)
  
##### added values in list#####
  
mydata=[]    #empty list 
  
print(mydata)
  
mydata.append(12)
mydata.append(12.34)
mydata.append("ronak cod lern kar") 

print (mydata)
values.append("ronak cod lern kar")

print(values)

# values.clear() #empty the list

#print(valuesd)

print(len(values))  # find the size of the list

values.reverse()

print(values)

numbers = [1,14,12,156,17,18,35,45,65,78]

print(numbers)

numbers.sort()
numbers.reverse()

print(numbers)

numbers.remove(17)
print(numbers)

# list datatype deatail

number = [12,34,354,34,4,2,4,True,"bascom",[1,2,3]]

print(number[9])

a = [1,2,3,4,5]

print(a)
print(a[2])
a[2] = 6
print(a)

a.append(45)        
a.append(56)
print(a)

a.insert(4,10)
print(a)

a.pop()
a.pop()
print(a)

a.remove(4)
print(a)

a.extend([9,8,7])
print(a)

a.append([9,8,7])
print(a)

a.append('bascom')  # type: ignore
print(a)

list=['hello','hi','how are you','hola','hi']

name = "bascom bridge"
   # string is immutable
name = name.capitalize()
print(name)

# a.clear()
# print()

names = [] # empty string

b = a.copy()

print(b)
print(list.count('hi'))
print(list.index('hola'))
print(list)
list.reverse()
print(list)
list.sort()
print(list)

###########################################

# tuple

adress = (1,2,3,4,5,6,7,8,9) # immutable
print(adress)
print(type(adress))

print(len(adress))

###########################################

# num = 12

# if num in range(1,2)
#       print("He")

############################################

# dictionary
# key - value

user = {
    "name":"ronak",
    "age" : 24,
    "adress":"gandhinagar",
    "name": "rohan",
    "name": "majanubhai",
    True:[1,2,3],
    "Marks": (12,13,14)
 }

print(user)

g = ["name","adress","age"]
k = 10

data = {} 

print(data.fromkeys(g,k))  # many to one relation

print(user.get("name"))

print(user.items())

user.pop("age")

print(user)

user.popitem()
print(user)

user.setdefault("pata","valsad")

print(user)

user.update({"name":"udey bhai"})
print(user)

print(user.values())

# swap number without using third variable

a1 = 12
b1 = 13

print(a1)
print(b1)

a1= a1+b1 #25
b1= a1-b1 #25-13 # 12
a1= a1-b1 #25-12 #13







 
 