f1=open("sample.txt","w")

while True:

    data=input("enter python features:")
    f1.write(data+"\n")
    n=int(input("enter 1 to store again and 2 to terminate"))
    if n==1:
        continue
    else:
        break
f1.close()  
print("data is written")  