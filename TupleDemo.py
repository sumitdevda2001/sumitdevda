t=(1,2,3,1.1,2.2,"tops",[10,20,30],True,"Java","python",10)

print(len(t))
print(t.count(1))
print(t.index(10))

for i in t:
    print(i)
print(22 in t)
print(t[6])
t[6].append(40)
print(t[6])
t.append(100)
