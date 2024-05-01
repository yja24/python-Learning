#file handling
file=open('myfile.txt','w')
#print("xyz")
file.write("Jack")
file.write("&Jones")
file.write("\nAdidas")
file.close()

file=open("myfile.txt",'a')
file.write("\nNike")



file=open("myfile.txt",'a+')
file.write("\nNB")

file=open("myfile.txt",'r')
print(file.read())

myfile=open("newfile.txt",'w')
myfile.write("Hello")
myfile.write('\nbonjour')

myfile=open("newfile.txt",'a')
myfile.write("\nnamaste")
myfile.write('\nこんにちは')

myfile=open("newfile.txt",'r')
print(myfile.read(12))