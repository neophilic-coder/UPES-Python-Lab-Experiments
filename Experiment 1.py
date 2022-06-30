#PROGRAM 1

n=float(input("Enter the number"))
if n%2!=0:
  print("WEIRD")
elif(n>=2 and n<=5 and n%2==0):
  print("NOT WEIRD")
elif(n%2==0 and n>=6 and n<=20):
  print("WEIRD)
else:
  print("NOT WEIRD)
  
#PROGRAM 2
n=int(input("Enter number:"))
for i in range(1,n+1):
  print(i*i)
  
#PROGRAM 3
n=int(input("Enter number:"))
for i in range(1,n+1):
  print(i*i,end=" ")
