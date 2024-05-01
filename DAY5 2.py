#COMPARISON OPERTORS
#true and false
x=int(input("enter value-"))
y=int(input("enter value-"))

#greater and lesser than operator
print('x<y',x<y)
print('x>y',x>y)

# = equal to operator 
print("x==y",x==y)

# != not equal to operator 
print("x not equal to y:",x!=y)

#greater than equal to 
print("x>=y",x>=y)

#less than equal to
print("x<=y",x<=y)


#logical operator and
p=(input('enter current password-'))
q=(input('enter new password-'))
r=(input("confirm new password-"))

if p!=q and q==r :
    print("password has been changed")
if p==q and p==r:
    print("current and new password cannot be same")
if p!=q and q!=r:
    print('confirm password does not match')

#or
alphabet= input("enter a alphabet-")

if (alphabet=='a' or alphabet=="e" or alphabet=="i" or
alphabet=="o" or alphabet=="u",):
    print(alphabet," is a vowel")
else:
    print(alphabet,"is a consonant")

#membership operator
mycollection=[1,2,3,4,5,12]
n1=int(input('enter number-'))
print(n1 in mycollection)
print(n1 not in mycollection)


#identity operator
mydata1=[1,2,3,4]
mydata2=[5,6,7,8]
mydata3=mydata1
print(mydata1 is not mydata3)