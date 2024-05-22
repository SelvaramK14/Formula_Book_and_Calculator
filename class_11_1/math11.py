import math
def tgf1():
    
    a=input("enter which value to calculate(l/(o)/r):")
    if a.lower()=='l':
        o=int(input("enter the angle:"))
        r=float(input("enter the radius of the arc:"))
        res=r*o
        print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
    elif a.lower()=='r':
        o=int(input("enter the angle:"))
        l=float(input("enter the length of the arc:"))
        res=l/o
        print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
    elif a.lower()=='(o)':
        l=int(input("enter the length of arc:"))
        r=float(input("enter the radius of the arc:"))
        res=l/r
        print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
def tgf2():
    d=int(input("enter the degree mesure:"))
    res=(3.14/100)*d
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
def tgf3():
    d=int(input("enter the radian mesure:"))
    res=(100/3.14)*d
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
def cnqe1():
    a=float(input("enter the real part of z1:"))
    c=float(input("enter the real part of z2:"))
    b=float(input("enter the imaginary part of z1:"))
    d=float(input("enter the imaginary part of z2:"))
    f=a+c
    v=c+d
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",f,"+ i(",v,")")
def cnqe2():
    a=float(input("enter the real part of z1:"))
    c=float(input("enter the real part of z2:"))
    b=float(input("enter the imaginary part of z1:"))
    d=float(input("enter the imaginary part of z2:"))
    f=(a*c)-(b*d)
    v=(a*d)+(b*c)
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",f,"- i(",v,")")
def cnqe3():
    a=float(input("enter the real part of z1:"))
    b=float(input("enter the imaginary part of z1:"))
    f=a**2/(a**2+b**2)
    v=-b**2/(a**2+b**2)
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",f,"+ i(",v,")")
def cnqe4():
    a=float(input("enter the real part of z1:"))
    b=float(input("enter the imaginary part of z1:"))
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",a,"- i(",b,")")
def cnqe5():
    a=float(input("enter the value of a:"))
    c=float(input("enter the value of c:"))
    b=float(input("enter the value of b:"))
    f=4*a*c-b**2
    x1=(-b + math.sqrt(f))/2*a
    x2=(-b - math.sqrt(f))/2*a
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",x1,"i","or",x1,"i")
def ss1():
    a=float(input("enter the value of first term(a):"))
    n=float(input("enter the value of n:"))
    d=float(input("enter the value of common difference(d):"))
    res=a+(n-1)*d
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
def ss2():
    a=float(input("enter the value of first term(a):"))
    n=float(input("enter the value of n:"))
    d=float(input("enter the value of common difference(d):"))
    res=(n/2)*(2*a+(n-1)*d)
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
def ss3():
    a=float(input("enter the value of first term(a):"))
    n=float(input("enter the value of n:"))
    r=float(input("enter the value of r:"))
    res=a*(r**(n-1))
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
def ss4():
    a=float(input("enter the value of a:"))
    b=float(input("enter the value of b:"))
    res=(a*b)**1/2
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
def st1():
    x1=float(input("enter the value of x1:"))
    x2=float(input("enter the value of x2:"))
    y1=float(input("enter the value of y1:"))
    y2=float(input("enter the value of y2:"))
    res=(y2-y1)/(x2-x1)
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
def st2():
    m1=float(input("enter the value of m1:"))
    m2=float(input("enter the value of m2:"))
    res=(m1+m2)/(1+(m1*m2))
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
def st3():
    a=float(input("enter the value of a:"))
    b=float(input("enter the value of b:"))
    c=a*b
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",b,"x +",a,"y =",c)
def st4():
    C2=float(input("enter the value of C2:"))
    C1=float(input("enter the value of C1:"))
    B=float(input("enter the value of A:"))
    A=float(input("enter the value of B:"))
    a=math.sqrt(A**2+B**2)
    s=(C1-C2)/a
    if s<0:
        s= -(C1-C2)/a
    else:
        s=(C1-C2)/a
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",s)
def dg1():
    x1=float(input("enter the value of x1:"))
    x2=float(input("enter the value of x2:"))
    y1=float(input("enter the value of y1:"))
    y2=float(input("enter the value of y2:"))
    z1=float(input("enter the value of z1:"))
    z2=float(input("enter the value of z2:"))
    res=((x2-x1)**2+(y2-y1)**2+(z2-z1)**2)**1/2
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS",res)
def dg2():
    x1=float(input("enter the value of x1:"))
    x2=float(input("enter the value of x2:"))
    y1=float(input("enter the value of y1:"))
    y2=float(input("enter the value of y2:"))
    z1=float(input("enter the value of z1:"))
    z2=float(input("enter the value of z2:"))
    m=float(input("enter the value of m:"))
    n=float(input("enter the value of n:"))
    res=(m*x2)+(n*x1)/(m+n) 
    res1=(m*y2)+(n*y1)/(m+n) 
    res2=(m*z1)-(n*z2)/(m+n)
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS","[",res,",",res1,",",res2,"]")
def dg3():
    x1=float(input("enter the value of x1:"))
    x2=float(input("enter the value of x2:"))
    y1=float(input("enter the value of y1:"))
    y2=float(input("enter the value of y2:"))
    z1=float(input("enter the value of z1:"))
    z2=float(input("enter the value of z2:"))
    res=(x1+x2)/2 
    res1=(y1+y2)/2 
    res2=(z1+z2)/2
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS","[",res,",",res1,",",res2,"]")
def dg4():
    x1=float(input("enter the value of x1:"))
    x2=float(input("enter the value of x2:"))
    y1=float(input("enter the value of y1:"))
    y2=float(input("enter the value of y2:"))
    z1=float(input("enter the value of z1:"))
    z2=float(input("enter the value of z2:"))
    x3=float(input("enter the value of x3:"))
    y3=float(input("enter the value of y3:"))
    z3=float(input("enter the value of z3:"))
    res=(x1+x2+x3)/2 
    res1=(y1+y2+z3)/2 
    res2=(z1+z2+z3)/2
    print("THE CALCULATED VALUE FOR THE GIVEN DATA IS","[",res,",",res1,",",res2,"]")
    
    
    
         

    
        
    





    
    
    
    
    











    
    

    
    
