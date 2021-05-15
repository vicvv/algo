

'''given the array of distinct integers count the number of 
pairs of int that have diference k'''

mylist = [1,7,5,9,2,12,3] 
k=2
mydict = {mylist[i]:i for i in range(len(mylist))}
mynewarr =[]

for key in mydict:
    if mydict[key]-k in mydict:
        mynewarr.append((mydict[key], mydict[key] - k))

print(mynewarr,len(mynewarr))


