#To understand the concepts of string in python

#PROGRAM 1
str=input("Enter string:")
str1=input("Enter substring:")
print(str.count(str1))


#PROGRAM 2
name=input("Enter name:")
lst=name.split(' ')
a=" "
for x in range(len(lst)-1):
  s=lst[x]
  a+=s[0].upper()+'.')
a+=lst[-1].title()
print(a)


#PROGRAM 3
def count_letters(text):
  result = {}
  text=text.lower()
  for letters in text:
    if letter.isalpha() and letter not in result:
      result[letter] = text.lower().count(letter)
    return result
print(count_letters("Casecaseidasese"))
