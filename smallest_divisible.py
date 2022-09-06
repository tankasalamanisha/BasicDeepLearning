l = [1,2,3,4,5,6,7,8,9,10]

l2 = [2520,5040,1260,3780]

flag = []
smallest_num=[]
for num in l2:
    for div in l:
        if num % div == 0:
            flag.append(True)
        else:
            flag.append(False)
    if all(flag):
        smallest_num.append(num)
print(smallest_num)
