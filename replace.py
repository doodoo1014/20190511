b = input("염기서열(A, T, C, G) 입력 : ")
c = ""
length = len(b) - 1
i=0
while(length >= i):
    if(b[i]=='A'):
        c+='T'
    elif(b[i]=='T'):
        c+='A'
    elif(b[i]=='C'):
        c+='G'
    elif(b[i]=='G'):
        c+='C'
    i+=1

print(c)
