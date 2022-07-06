#Program 1
def natural(n):
  c=0
  for i in range(n+1):
    c+=i
  print("Addition of numbers is",c)
def fibonacci(n):
  a=0
  b=1
  print(a)
  print(b)
  for i in range(2,n+1):
    d=a+b
    print(d)
    a=b
    b=d
  n=int(input("Enter the number"))
  f=natural(n)
  g=fibonacci(n)
  

  #Program 2
def check_baggage(baggage_weight):
  if baggage_weight>=0 and baggage_weight<=40:
    return True
  else:
    return False

def check_immigration(expiry_year):
  if expiry_year>=2030 or expiry_year<=2050:
    return True 
  else:
    return False

def check_security(noc_status):
  if noc_status=='valid' or'VALID':
    return True
  else:
    return False

def traveller():
  traveller_id=int(input("Enter traveller id"))
  traveller_name=input("Enter traveller name")
    
  x=int(input("Enter baggage weight:"))
  check_baggage(x)
    
  y=int(input("Enter expiry year"))
  check_immigration(y)
    
  z=input('VALID or Invalid')
  check_security(z)
    
  if check_immigration(y) and check_baggage(x) and check_security(z):
    print(traveller_id,traveller_name)
    print('Allow traveller to fly')
  else:
    print(traveller_id,traveller_name)
    print('Detain traveller for re-checking!')
  return traveller_id,traveller_name,check_baggage(x),check_immigration(y),check_security(z)
traveller()
  

#Program 3
def MaxTuple(tup):
  a = max(tup, key=lambda item:item[1])[1]
    
def MinTuple(tup):
  b = min(tup, key=lambda item:item[1])[1]
  
tup=[('V', 62), ('VI', 68), ('VII', 72), ('VIII', 70), ('IX', 74), ('X', 65)]
print("Tuple:",tup)
print("Max value:",MaxTuple(tup))
print("Min value:",MinTuple(tup))
