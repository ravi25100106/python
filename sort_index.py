n = int(input('Enter number of names:'))
names={}
L=[]
for i in  range(n):
    ip=input("enter the names:")
    L.append([i+1,ip])
for i in range(len(L)):
    names[L[i][0]]=[]
    names[L[i][0]].append(L[i][1])
name = list(names.values())
pos = int(input('Enter position'))-1
name.sort(key=lambda x:x[pos])
print(name)
