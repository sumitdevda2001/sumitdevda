d={110:"Aagam",345:"Sumit",879:"Shruti",908:"Ashesh",333:"Jaymin",111:"Khushvant",256:"Narottam",901:"Ami"}

print(d)
print(d[345])
d1=d.copy()
print(d1)
print(d.get(879))
print(d.items())
print(d.keys())
print(d.values())
print(d.pop(908))
print(d)
print(d.popitem())
d2={1:"Ami",2:"Ashesh"}
d.update(d2)
print(d)
d[112]="Jigar"
print(d)

for i in d:
    print(i,"   ",d[i])
