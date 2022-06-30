#Working with Data Structures in Python 

#PROGRAM 1
a=dict()
for i in range(1,6):
  a[i]=input(" ")
  print(a)
  
a={"amit":[34,90,61],"ajay":[17,59,62]}
sum=0
for i in range(0,3):
  sum=sum+a["amit"][i]
print(sum/3)


#PROGRAM 2
a=[]
n = int(input("Enter number:"))
for i in range(1,n+1):
  x = int(input("Enter score:"))
  a.append(x)
a.sort()
print("Runner up is:",a[n-2])


#PROGRAM 3
lst=[]
n=int(input("Enter the number:"))
for i in range(1,n+1):
  b = int(input("Enter score:"))
  lst.append(b)
t=set(lst)
print("Distinct numbers are:",t)
