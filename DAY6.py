n1=float(input("percentage in maths="))
n2=float(input("percentage in chemistry="))
n3=float(input("percentage in physics="))
n4=float(input("percentage in english="))
n5=float(input("percentage in physical education="))
overallpercentage=(n1+n2+n3+n4+n5)/5

if overallpercentage<50:
    print("Grade=F")
elif overallpercentage >= 50 and overallpercentage<60:
    print("Grade=D")
elif overallpercentage >= 60 and overallpercentage<70:
    print("Grade=C")
elif overallpercentage >= 70 and overallpercentage<80:
    print("Grade=B")
elif overallpercentage >= 80 and overallpercentage<90:
    print("Grade=A")
else:
    print("Grade=A+")


N1=float(input("enter first number-"))
N2=float(input("enter second number-"))
N3=float(input("enter third number-"))

print("Cube =",N1**3,"square=",N1**2)
print("Cube =",N2**3,"square=",N2**2)
print("Cube =",N3**3,"square=",N3**2)







