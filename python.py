# a=open("text.txt","rt")
# print(a.readline())
# a.readline()
# print(a.readline())

# a.close()
# next program

# f=open("write.txt","wt")
# f.write("This is a new file for writing")
# f.write("\nEND")
# f.close
# f=open("write.txt","rt")
# print(f.read())
# f.close()
# f=open("write.txt","at")
# f.write("this is appendend text")
# f.close()
# next program
 
f=open("newfile.txt","x")
f.close()
import os
os.remove("write.txt")

