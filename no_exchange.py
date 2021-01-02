import random as rd 
c=d=0
for i in range(10000):
    a,b=rd.randrange(0,3,1),[0,0,0]
    b[rd.randrange(0,3,1)]=1
    if b[a]==1:
        c+=1
    else:
        d+=1
print(c/(c+d)*100,"%")
