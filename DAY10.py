#Take a year and check whether it is leap year or not.

#Write a program to enter two numbers and find the smallest out of them. Use conditional operator
n1=int(input("enter first number-"))
n2=int(input("enter second number-"))
if n1>n2:
    print("number second is smaller",n2)
elif n1==n2:
    print("both numbers are equal")
else:
    print("number first is smaller",n1)


#Take 2 numbers and display greatest number
n1=int(input("enter first number-"))
n2=int(input("enter second number-"))
if n1>n2:
    print("number first is greater",n1)
elif n1==n2:
    print("both numbers are equal")
else:
    print("number second is greater",n2)


 #Take age and whether it is less than 18 or not. If it is less than 18 then print not eligible for vote.

age=int(input("Enter your age-"))
if age<18:
    print("Not eligible to vote")
else:
    print("Eligible for voting")

#Write a program to check whether the blood donor is eligible or not for donating blood. The conditions laid down are as under. Use if statement.
#	•	Age should be above 18 year but not more than 55 year.

year1=int(input("enter your age-"))
if year1>18:
    if year1<55:
        print("eligible to donate")
    else:
        print("not eligible for blood donation")

else:
    print("not eligible for blood donation")

#Write a  program to find the maximum from given four numbers (using logical operator).


n1=float(input("enter first number-"))
n2=float(input("enter second number-"))
n3=float(input("enter third number-"))
n4=float(input("enter forth number-"))

if n1>n2 and n1>n3 and n1>n4:
    print("First number is the greatest")
elif n2>n1 and n2>n3 and n2>n4:
    print("second number is the greatest")
elif n3>n2 and n3>n1 and n3>n4:
    print("third number is the greatest")
elif n1==n2 and n2==n3 and n3==n4:
    print("all numbers are equal")
else:
    print("forth is the greatest")
    
#Take a number. If number is 1 then print Monday, 2 then print Tuesday and so on…

days=int(input("Enter any number from 1 to 7-"))
match days:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case 5:
        print("Friday")
    case 6:
        print("Saturday")
    case 7:
        print("Sunday")

#Take a number to print the square of a number if it is less than 10.
n1=int(input("Enter any number less than 10-"))
if n1<10:
    ans=n1**2
    print(ans)
else:
    print("number not valid")




#Write a program to make a Simple Calculator to Add, Subtract, Multiply or Divide Using match...case.
n1=float(input("enter number- "))
n2=float(input("enter number- "))
ans=input("add or subtract or multiply or divide- ")

match ans:
    case "add":
        print(n1+n2)
    case "subtract":
        print(n1-n2)
    case "multiply":
        print(n1*n2)
    case "divide":
        print(n1/n2)

#muliplication table
num=int(input("enter number-"))
print("Table of -",num)
for i in range(1,11):
    print(num,'X',i,"=",num*i)








