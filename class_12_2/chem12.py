import math
def ss1():
    s=input("enter which value to calculate(a/r):")
    if s.upper()=='A':
        r=float(input("enter the value of r:"))
        res=2*r
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s.upper()=='R':
        a=float(input("enter the value of a:"))
        res=a/2
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")
def ss2():
    s=input("enter which value to calculate(a/r):")
    if s.upper()=='A':
        r=float(input("enter the value of r:"))
        q=math.sqrt(3)
        res=(4/q)*r
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s.upper()=='R':
        a=float(input("enter the value of a:"))
        q=math.sqrt(3)
        res=(4*a)/q
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")
def ss3():
    s=input("enter which value to calculate(a/r):")
    if s.upper()=='A':
        r=float(input("enter the value of r:"))
        q=math.sqrt(2)
        res=2*q*r
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s.upper()=='R':
        a=float(input("enter the value of a:"))
        q=math.sqrt(2)
        res=a/(2*q)
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")
def ss4():
    z=float(input("enter the value of Z:"))
    m=float(input("enter the value of M:"))
    a=float(input("enter the value of a:"))
    n=float(input("enter the value of N(A):"))
    res=(z*m)/(a**3*n)
    print("THE RESULT OF THE CALCULATION IS",res)
def ss5():
    d=float(input("enter the value of d:"))
    m=float(input("enter the value of M:"))
    r=float(input("enter the value of r:"))
    n=float(input("enter the value of N(A):"))
    res=((d*n)/m)*((4*3.14*r**3)/3)*100
    print("THE RESULT OF THE CALCULATION IS",res)
def s1():
    s=input("enter which value to calculate(x(A)/x(B)):")
    if s=='x(A)':
        na=float(input("enter the value of n(A):"))
        nb=float(input("enter the value of n(B):"))
        res=na/(na+nb)
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s=='x(B)':
        na=float(input("enter the value of n(A):"))
        nb=float(input("enter the value of n(B):"))
        res=nb/(na+nb)
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")
def s2():
    sol=float(input("enter the value of moles of solute:"))
    vol=float(input("enter the value of volume of solution in litres:"))
    res=sol/vol
    print("THE RESULT OF THE CALCULATION IS",res)
def s3():
    sol=float(input("enter the value of moles of solute:"))
    mas=float(input("enter the value of mass of solvent in kilograms:"))
    res=sol/mas
    print("THE RESULT OF THE CALCULATION IS",res)
def s4():
    i=float(input("enter the value of i:"))
    t=float(input("enter the value of T:"))
    r=float(input("enter the value of R:"))
    c=float(input("enter the value of C:"))
    res=i*c*r*t
    print("THE RESULT OF THE CALCULATION IS",res)
def s5():
    mas=float(input("enter the value of normal molar mass:"))
    abmas=float(input("enter the value of abnormal molar mass:"))
    res=mas/abmas
    print("THE RESULT OF THE CALCULATION IS",res)
def s6():
    i=float(input("enter the value of i:"))
    k=float(input("enter the value of K(b):"))
    m=float(input("enter the value of m:"))
    res=i*k*m
    print("THE RESULT OF THE CALCULATION IS",res)
def s7():
    i=float(input("enter the value of i:"))
    k=float(input("enter the value of K(f):"))
    m=float(input("enter the value of m:"))
    res=i*k*m
    print("THE RESULT OF THE CALCULATION IS",res)
def ec1():
    r=float(input("enter the value of R:"))
    l=float(input("enter the value of l:"))
    a=float(input("enter the value of A:"))
    res=(1/r)*(l/a)
    print("THE RESULT OF THE CALCULATION IS",res)
def ec2():
    s=input("enter which value to calculate(A(m)/k):")
    if s=='A(m)':
        k=float(input("enter the value of k:"))
        c=float(input("enter the value of c:"))
        res=(1000*k)/c
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s=='k':
        a=float(input("enter the value of A(m):"))
        c=float(input("enter the value of c:"))
        res=(a*c)/1000
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")
def ec3():
    e=float(input("enter the value of (E^+):"))
    r=float(input("enter the value of R:"))
    t=float(input("enter the value of T:"))
    n=float(input("enter the value of n:"))
    f=float(input("enter the value of F:"))
    m=float(input("enter the value of (M^n+):"))
    v=1/m
    lo=math.log(v)
    res=e-((2.303*r*t)/(n*f))*lo
    print("THE RESULT OF THE CALCULATION IS",res)
def ec4():
    v=float(input("enter the value of v:"))
    n=float(input("enter the value of n:"))
    k=float(input("enter the value of K(c):"))
    lo=math.log(k)
    res=((0.059*v)/n)*lo
    print("THE RESULT OF THE CALCULATION IS",res)
def ck1():
    s=input("enter which value to calculate(k/t):")
    if s=='t':
        k=float(input("enter the value of k:"))
        r1=float(input("enter the value of [R(0)]:"))
        r=float(input("enter the value of [R]:"))
        res=(r1-r)/k
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s=='k':
        t=float(input("enter the value of t:"))
        r1=float(input("enter the value of [R(0)]:"))
        r=float(input("enter the value of [R]:"))
        res=(r1-r)/t
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")
def ck2():
    k=float(input("enter the value of k:"))
    r=float(input("enter the value of [R(0)]:"))
    res=r/(2*k)
    print("THE RESULT OF THE CALCULATION IS",res)
def ck3():
    s=input("enter which value to calculate(k/t):")
    if s=='t':
        k=float(input("enter the value of k:"))
        r1=float(input("enter the value of [R(0)]:"))
        r=float(input("enter the value of [R]:"))
        v=r1/r
        lo=math.log(v)
        res=(2.303/k)*lo
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s=='k':
        t=float(input("enter the value of t:"))
        r1=float(input("enter the value of [R(0)]:"))
        r=float(input("enter the value of [R]:"))
        v=r1/r
        lo=math.log(v)
        res=(2.303/t)*lo
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")
def ck4():
    k=float(input("enter the value of k:"))
    res=0.693/k
    print("THE RESULT OF THE CALCULATION IS",res)
def ck5():
    e=float(input("enter the value of Ea:"))
    r=float(input("enter the value of R:"))
    t=float(input("enter the value of T:"))
    a=float(input("enter the value of A(e):"))
    m=-e*r*t
    res=a**m
    print("THE RESULT OF THE CALCULATION IS",res)
    
    

    
    
    
    
    
    
    

    
    































    
