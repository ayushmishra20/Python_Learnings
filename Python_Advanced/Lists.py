# orderd , muteble, allows duplicate ele

mylist = ["Banana", "Cherry", "apple"]
print(mylist)
 
 
newlist = [4,"apple", "apple", False]
for element in newlist:
    print(element)
    
if "apple" in newlist:
    print("Yes")
else:
    print("No")
    
print(len(newlist))
newlist.append("Kela")
newlist.insert(1,"berry")
item = newlist.pop()
print(item)
print(newlist)
newlist.clear()
newlist.reverse()
newlist2 = [1,2,6,3,6,3]
newlist2.sort()
new_sorted = sorted(newlist2)

newlist2 = [0] = 5
print(newlist2)
new_ls = mylist + newlist2
print(new_ls)


#slicing in list

ls1 = [1,2,3,4,5,6,7,8,9,0]

a= ls1[::-1] # reverse the list

lst = ["Banana", "chery", "kela"]
list_copy = lst
list_copy.append("Amrood")
print(lst)
newls2 = lst.copy()
newls3 = lst[:] #this also makes copy

a = [2,4,6,7,8,8]
b = [i*i for i in a]

print(a)
print(b)
