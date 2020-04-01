import math
def bsgs(alpha,y,p):
    l=p-1
    #pow(alpha,x)=y
    m=math.ceil(math.sqrt(l))
    arr=[]
    for i in range(0,m):
        arr.append(pow(alpha,i,p))
    c = pow(alpha, m*(p-2), p)
    for j in range(0,m):
        sub=(y*pow(c,j,p))%p
        if(sub in arr):
            return((j*m+arr.index(sub)))
print( bsgs(2,8,11))
