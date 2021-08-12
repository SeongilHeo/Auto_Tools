### Load Data from .txt files as Dictionary 'D'
day=int(input("Enter the data(ex: 2 -> day2)"))
E=open('./data/%02dE.txt'%(day),'r',encoding='utf-8')
K=open('./data/%02dK.txt'%(day),'r',encoding='utf-8')
D={}
while True:
    a=K.readline().strip()
    if a:
        D[a]=E.readline().strip()
    else:
        break
E.close()
K.close()

### Quiz's Time
L=list(D.keys())
ori=len(L)
i=0
for each_kor in L:
    print("%s\t\tcount %02d"%(each_kor,len(L)-i))
    if i==ori:
        print("----------------------------------")
        print("review",len(L))
    if input().strip()!=D[each_kor]:
        L.append(each_kor)
        print("*******"+each_kor+"->"+D[each_kor]+"*******")
        print("*%s*"%(input().strip()==D[each_kor]))
        print()
    else:
        i+=1