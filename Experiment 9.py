#Program 1: Input two values from the user where the first line contains N, the number of test cases. The next N lines contain the space-separated values of a and b. Perform integer division and print a/b. Print the error code in the case of ZeroDivisionError or ValueError.

t= int(input("Enter test cases: "))
lst = []

for x in range(0,t):
  n = input("Enter number {0}: ".format(x+1))
  lst.append(n)

for x in lst:
  try:
    l=x.split(' ')
    print(int(l[0]/int(l[1]))
          
  except ZeroDivisionError:
    print("Division with zero not possible")
  except NameError:
    print("Only Integer values are excpected.")
  except:
    print("Some exception occurred")
          
          
#Program 2: Rewrite the code to handle the exceptions raised. Print appropriate error messages wherever applicable.

 try:
   l=[1,2,3,4,5]
   sum=0
   for x in l:
     if isinstance(x,tuple):
        raise Exception("Only Integer expected")
     sum+=x
   print(sum)
   x= int(input("Enter index value:"))
   if(x>4):
      raise Exception("Index out od range.")
   print(l[5])
          
  except Exception as exp:
    print(exp)

          
#Program 3: Rewrite the code to handle the exceptions raised. Print appropriate error messages wherever applicable.
try:
  f= open("D:\\F1.txt","r")
   str1=f.read()
   str2=""
   print(str)
   for ch in str1:
     if ch == '\"':
          str2+= "\\"+ch
     else:
          str2+=ch
   print(str2)
   f.close()
   f=open("D:\F2.txt","w+")
   f.write(str2)
   f.close()
 
 except:
    print("Some error occured")

          
          
