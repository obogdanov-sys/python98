x,y,n=map(int,input().split())
k=(x*100+y)*n
r=k//100
k2=k%100
print(r, "руб.", k2, "коп.")