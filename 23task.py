s=int(input())
hour=s//3600
min=(s%3600)//60
s2=s%60
print(hour, f"часов",min, f"минут",s2 ,f"секунд")