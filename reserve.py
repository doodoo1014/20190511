#첫 번째 방법

a=input("염기서열(A, T, C, G) : ")
b="".join(reversed(a))
print(b)

# 두 번째 방법

c=input("염기서열(A, T, C, G) : ")
d=""
length=len(c)-1
while(length>-1):
    d+=c[length]
    length-=1
print(d)
