import time

# Load Data from .txt files as Dictionary 'D'

day=int(input("Enter the data(ex: 2 -> day2): "))
E=open('data/%02dE.txt'%(day),'r',encoding='utf-8')
K=open('data/%02dK.txt'%(day),'r',encoding='utf-8')
D={}
while True:
    a=K.readline().strip()
    if a:
        D[a]=E.readline().strip()
    else:
        break
E.close()
K.close()

# Quiz's Time

L=list(D.keys())
ori=len(L)
s=0
i=0
while L:
    i+=1
    each_kor=L.pop(0)
    print("%s\t\tcount %02d"%(each_kor,len(L)+1))
    if input().strip()!=D[each_kor]:
        L.append(each_kor)
        print("*******"+each_kor+"->"+D[each_kor]+"*******")
        print("*%s*"%(input().strip()==D[each_kor]))
    if s==0 and i==ori:
        print("----------------------------------")
        print("review",len(L))
        s=1
    print()
print("Day%02d completed"%day)
time.sleep(1)
	