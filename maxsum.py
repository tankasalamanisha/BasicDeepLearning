l = [19,81,2,41,61,59,28,69,76,88]

s = 0
for i in range(len(l)):
    for j in range(1,len(l)):
        s2= l[i]+l[j]
        if s2 > s:
            s= s2
print(s2)
