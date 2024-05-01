#with statement for file
open("newfile","a")

with open("newfile.txt","a") as f:
    f.write("\nola`")
    f.writelines(["привет","\nDia dhuit"])
f.close


print(f.readable())
f=open("newfile.txt","r")
f.seek(2)
print(f.readline())

f=open("newfile.txt","r")
print(f.readline())
print(f.tell())

f=open("newfile2.txt","a")
f.truncate(1)
f.close