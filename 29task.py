import math
a,b,c=map(int,input().split())
cos_a=(b**2+c**2-a**2)/(2*b*c)
cos_b=(a**2+c**2-b**2)/(2*a*c)
cos_c=(a**2+b**2-c**2)/(2*a*b)
ua=math.degrees(math.acos(cos_a))
ub=math.degrees(math.acos(cos_b))
uc=math.degrees(math.acos(cos_c))
print(ua,ub,uc)