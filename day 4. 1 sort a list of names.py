n = int(input())
list=[]
for i in range(n):
    a= (input())
    list.append(a)
l1=sorted(list)
l2= sorted(list,reverse=True)
choice = (input("a/d"))
if(choice=="a"):
    print("ascending order:",l1)
else:
    print("descending order:",l2)
