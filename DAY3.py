# if statement for even and odd

n1=int(input("enter value-"))
if n1%2 == 0:
    print("number is even")

if n1%2 == 1:
    print("number is odd")

# If else statement 
n2=int(input("enter value-"))
if n2%2 == 0:
    print("number is even")
else:
    print('number is odd')

#if elif else statement
x=int(input('enter value of x-'))
y=int(input("enter value of y-"))

if x==y:
    print('x and y are equal')

elif x<y:
    print("x is less than y")

else:
    print("x is greater than y")    


#match case statement
p=int(input("enter number-"))
match p:
    case 1: 
        print('correct')
    case 2:
        print('correct')
    case 3:
        print('incorrect')
    case _:
        print('invalid')

#nested if else statement 