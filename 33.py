N,C,S=map(int,input().split())
p=(S-1)//(N*C)+1
p2=(S-1)%(N*C)+1
p3=(p2-1)//N+1
p4=(p2-1)%N+1
print(f"{p} страница {p3} столбец {p4} строка")