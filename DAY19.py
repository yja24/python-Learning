#binary data handling
f=open("test.bin","wb")
arr=bytearray("this is test".encode("ascii"))
f.write(arr)
f.close

f=open("test.bin","rb")
print(f.read())
f.close()