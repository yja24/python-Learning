import os

filename=open("Uvfile2.txt",'w')
filename.write('yes no nope yeah')
filename.close()

filename="Uvfile2.txt"
os.rename(filename,'UVfile.txt')
print("rename successful")

os.mkdir("MyDirectory")
print("Directory created")

os.chdir("MyDirectory")
print("Directory changed")
print(os.getcwd())

