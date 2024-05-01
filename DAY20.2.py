import os 
fd='myfile0'

file=open(fd,'w')
file.write("Way Down We Go")
file.close()
file=open(fd,"r")
text=file.read()
print(text)

file=os.popen(fd,'w')


fd="myfile0"
file=open(fd,'r')
text=file.read()
print(text)
os.close(file)