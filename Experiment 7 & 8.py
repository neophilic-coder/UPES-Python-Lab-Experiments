#File Handling in Python

#Program 1
f = open("D:\\F1.txt","r+")
str = f.read()
s = " "
for x in str:
  if x == '\"':
    s = s+'\\'+x
   else:
    s = s+x
print(s)
f.close()
f = open("D:\\F2.txt","w")
f.write(s)
f.close()

#Program 2
f1 = open("D:Rhyme.txt","r+")
lst = f1.read().split()
f1.close()
d={}
for i in lst:
  i = i.lower()
  if i in d:
    d[i] = d[i]+1
  else:
    d[i] = 1
f2 = open("D:\\Words.txt","w+")
for i in d:
  f2.write(i+' ')
  print(i,end=' \t')
  print(d[i])
f2.close()


#Program 3
f = open("D:\\City.txt","r+")
l = f.read().split("\n")
lst = []
for x in l:
  lst.append(x.split(' '))
print("\nCity Details:" , end = "\t")
for x in lst:
  print(x,end="\t")
print("\nCity with population over 10 lakh:",end="\t")
for x in lst:
  if float(x[1])>10.0:
    print(x[0])
print("\nSum of area of all cities:",end="\t")
sum = 0.0
for x in lst:
  sum+=float(x[2])
print(sum)
f.close()
