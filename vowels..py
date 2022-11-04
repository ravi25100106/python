"""to display whether the given word contains all the vowels or not"""

"""importing permutations module from itertools package."""
from itertools import permutations
"""taking input from the user."""
t=input("Enter any word:") 

"""assigning the vowels to evaluate the given word."""
c="AEIOU"

"""removing the duplicate elements in the given word."""
t=list(t)
t=set(t)
t=list(t)
t="".join(t)

"""converting the whole word into uppercase."""
t=t.upper()

n=len(t)     #assigning the lenght of the sorted word form.

l=[]            #creating empty list.

"""forming every 5 letter combination possible from the sorted word and adding them to the list."""
for ele in permutations(t,5):
    l.append("".join(ele))
    
    """creating a count variable to increment if the combination of all the vowels is present."""
count=0

"""checking if combination containing all vowels is present or not and print the appropriate message."""
for ele in l:
    if ele == c:
        count=1
if count!=1:
    print("one or more vowels are not present!!!")
else:
    print("all vowels are present!!!")