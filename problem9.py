x=0
ope=[]
s=int(input())
for i in range(s):
    op=input()
    ope.append(op)
for s in ope :
        if s == '++x' or s =='x++':
            x+=1
        elif s=='--x' or s=='x--':
            x-=1

print(x)

