
subjects = ["Java","Python","Kotlin","Dart","Fluter","Php","C","C++"]

#len() -  checkout this length() 0 to start this length.;
a = len(subjects)
print("Total length" , a)

# apeand() -  use to list item adding and adding to last item..
subjects.append("Programming")
print("appeand :" ,subjects)


# insert()-  if you want to appeand any index so, adding and after the all value arrange to step to step.
subjects.insert(2,"Go")
print("Insert :", subjects)

# remove() - if want to remove write a index char.
subjects.remove("Java")
print("Remove : ",subjects)

#sorting() - this is arrange in char & int.
subjects.sort()
print("Arrange sort : " ,subjects)

# reverse()  - this is to use descending  in print
subjects.reverse();
print("Reverse : ", subjects)

#pop() - behind the length is remove.
subjects.pop();
print("Pop ", subjects)


#copy() - list copy
subjects2 = subjects.copy();
print("Copy ", subjects)




#clear() - all list  are clear.
subjects.clear();
print("Clear : ", subjects)

#index() - return for index.
sub3 = [20,10,2,55,44,2,555,0,0,0,0]
pos = sub3.index(2)
print("Index : ",pos)

#count - how many item arrange in the storage.
num = sub3.count(0)
print("Count number : ",num)






