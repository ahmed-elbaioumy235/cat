x=0
ope=[]
s=int(input())
for i in range(s):
    op=input()
    ope.append(op)
for s in ope :
        if s.find('+')!=-1:
            x+=1
        elif  s.find('-')!=-1:
            x-=1

print(x)

