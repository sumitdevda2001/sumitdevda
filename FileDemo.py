file=open("tops1.txt","w+")
file.write("This is w+ operation using python.")
print("File Current Position : ",file.tell())
file.seek(10)
print(file.read())
file.close()
