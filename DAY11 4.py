str1= "my name is Nothing."
str2= "yes,no,what,whynot"
str3="Hewlett packard"

#capitaltize
ans=str1.capitalize()
print(ans)

#casefold
ans=str1.casefold()
print(ans)

#center
ans=str1.center(40)
print(ans)

#count
ans=str2.count('yes')
print(ans)

#endswith
ans=str1.endswith(".")
print(ans)

#expandtabs()
ans=str3.expandtabs(3)
print(ans)

#find()
ans=str3.find("Hewlett packard")
print(ans)

#index
ans=str3.index("Hewlett packard")
print(ans)

#islanum
ans=str3.isalnum()
print(ans)

#isalpha
ans=str3.isalpha()
print(ans)

#isdigit
ans=str1.isdigit()
print(ans) 

#isidentifier
ans=str2.isidentifier()
print(ans)

#islower
ans=str2.islower()
print(ans)

#isnumberic
ans=str1.isnumeric()
print(ans)

#isspace
ans=str3.isspace()
print(ans)

#istitle
ans=str3.istitle()
print(ans)

#isupper
ans=str2.isupper()
print(ans)

#join
ans= "$".join(str3)
print(ans)

#lower()
ans=str3.lower()
print(ans)

#partition
ans=str1.partition("is")
print(ans)

#replace
ans=str2.replace("yes","yeah")
print(ans)

#startswith 
ans=str1.startswith("my")
print(ans)

#split
ans=str2.split()
print(ans)

#swapcase
ans=str3.swapcase()
print(ans)

#title()
ans=str2.title()
print(ans)

#upper
ans=str3.upper()
print(ans)

