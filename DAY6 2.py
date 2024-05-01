
i=10
while i>=1:
    print(i)
    i=i-1 


mydata = [10, 20.5, "Hello"]
for i in mydata:
    print("Value is ",i)


for i in reversed(range(0, 5, 1)):
    print("Value is ", i)

for i in range(5):
    print("Value is ", i)
else:
    print("No value left")

for i in range(5):
    if i == 3:
        break
print("Value is ", i)

for i in range(5):
    if i == 3:
        continue
print("Value is ", i)