rows = int(input("Enter the number of rows: "))

k=0
num=1

for i in range(1, rows+1):
    for space in range(1, (rows-i)+1):
        print(end=" ")
   
    while k!=(2*i-2):
        if(num%2!=0):
            print(num,end=" ")
        num+=1
        k+=1
    k=0
    print()
