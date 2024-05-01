import os
print(os.system)

#print(os.environ)

print(os.getpid())

print(os.name)

try:
    file="UvFile.txt"
    f=open(file,'r')
    text=f.read()
    f.close()
except IOError:
    print(os.error)



    