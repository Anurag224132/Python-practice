f=open("harry.txt")
#content=f.read()
#print(content)
#for line in f:
   # print(line,end="")
#content=f.read(34455)
#print("1",content)
content=f.read(34455)
print("2","234",content)
f=open("harry.txt","rt")
#print(f.readline())
#print(f.readline())
#print(f.readline())
#print(f.readline())
print(f.readlines())

f.close()