"""i=11
while(i<10):
    print(i)
    i+=1



while True:
    print(i)

    if(i<10):
        print(i)
        
    else:
        break"""

ls=[12,45,67,"HI","HELLO",23,5,67,8]
ls1=[]
print(ls1.__class__)

ls1.append("green")
ls1.append("yellow")

ls1.append(ls)
ls1.append("blue")
print(ls1)

ls1.insert(1,"grape")
ls1.insert(2,ls)
print(ls1)

ls1.remove("blue")
print(ls1)

#ls1.remove(45)

for i in ls1:
    if type(i)==type(ls1):
        print("List")
    try:
        i.remove(45)
        print(ls1)
    except:
        print("Not Present")
else:
    try:
        ls1.remove("green")
        print(ls1)
    except:
        break

