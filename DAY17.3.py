import random
#random
ans=random.random()
print(ans)

#randint
ans1=random.randint(69,88)
print(ans1)

#randrange
ans3=random.randrange(1,20,2)
print(ans3)

#choice
ans4=random.choice([1,4,14,19,20,12])
print(ans4)

#shuffle
n1=[1,4,14,19,20,12]
ans5=random.shuffle(n1)
print(n1)

#sample
mylist=["JBL","APPLE","SAMSUNG","MSI",1, 2,3]
print(random.sample(mylist,k=2))

#uniform
print(random.uniform(10,44))

#triangular
print(random.triangular(11,22,15))
