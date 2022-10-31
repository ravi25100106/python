from itertools import permutations
t=input("Enter any word:")
c="OIEUA"
t=list(t)
t=set(t)
t=list(t)
t="".join(t)
t=t.upper()
n=len(t)
l=[]
for ele in permutations(t,5):
    l.append("".join(ele))
count=0
for ele in l:
    if ele == c:
        count=1
if count!=1:
    print("one or more vowels are not present!!!")
else:
    print("all vowels are present!!!")