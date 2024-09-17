for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print("")
d={
    "s":12,
    "u":21
}
s={
"w":23
}

d.update(s)
w=[]
for v in d.values():    

    w.append(v)
print(w)