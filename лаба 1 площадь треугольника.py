a = float(input())
b = float(input())
c = float(input())

if a +b>c and a +c > b and b+c>a:
    P = (a+b+c)/2
    PL = (P*(P-a)*(P-b)*(P-c))**0.5
    print(PL)
else:
    print("нет такого")