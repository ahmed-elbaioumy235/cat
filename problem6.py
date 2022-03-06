from itertools import count


n=int(input())
problems=[]
count=0
for i in range(n):
    pro=input()
    problems.append(pro)
for p in problems:
    if p.count('1')>=2:
        count+=1
print(count)
