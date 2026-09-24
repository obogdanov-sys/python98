A,C,Y,T,I=map(int,input().split())
a=(C/(A)-0.3)*5
b=(Y/(A)-3)*0.25
c=(T/A)*20
d=2.375-(25*I/(A))
R=(a+b+c+d)/(6)*100
print(R)