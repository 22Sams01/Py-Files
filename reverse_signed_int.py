# Reverse a number 
# i/p is signed 32 bit int eg: -123 o/p 321- if val outside range of signed 32 bit int return 0
x=int(input())
a=str(x)
print(">>",a) 
if x<0:
    a='-'+a[::-1][:-1]
    y=int(a)
    print("!!!!1",y)
else:
    a=a[::-1]
    y=int(a)
    print("@@@@@@@",y)
neg_limit= -0x80000000
pos_limit= 0x7fffffff

if(y<0):
        val=y&neg_limit
        print("OOOOOOOOO",val)
        if(val==neg_limit):
            print(y) 
        else:
                print("0")
elif(y==0):
    print(y)
else:
    val = y&pos_limit
    print("PPPP",val)
    if(val==y):
        print(y)
    else:
        print("0")
