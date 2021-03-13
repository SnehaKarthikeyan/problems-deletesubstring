Coding:

s=str(input())
s1=str(input())
l=list(s)
k=list(s1)
for i in s:
  if i in s1:
      l.remove(i)
delimiter=''
s2=delimiter.join(l)
print(s2)
