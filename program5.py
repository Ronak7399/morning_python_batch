# question 1

num = int(input("please enter number : "))
if (num % 2) == 0:
    print("{0} is even")
else:
    print("{0} is odd")
    
# question 2 

a =int(input("please enter number: "))
b =int(input("please enter number: "))

print(a)
print(b)

if a>b :
    print("number is small")
else :
    print("number is large")
    
# question 3

c =int(input("please enter number: "))
print(c)

if c>0 :
    print("number is positive")
elif c<0:
    print("number is negative")
else :
    print("number is zero")
    
# question 4

sub1=int(input("Enter marks of the first subject: "))
sub2=int(input("Enter marks of the second subject: "))
sub3=int(input("Enter marks of the third subject: "))
sub4=int(input("Enter marks of the fourth subject: "))
sub5=int(input("Enter marks of the fifth subject: "))
avg=(sub1+sub2+sub3+sub4+sub5)
if(avg>=90-100):
    print("Grade: A")
elif(avg>=80&avg<89):
    print("Grade: B")
elif(avg>=70&avg<79):
    print("Grade: C")
elif(avg>=60&avg<69):
    print("Grade: D")
else:
    print("Grade: F")

# question 5 

year=int(input("Enter year to be checked:"))
if(year%4==0 and year%100!=0 or year%400==0):
    print("The year is a leap year!")
else:
    print("The year isn't a leap year!")
    