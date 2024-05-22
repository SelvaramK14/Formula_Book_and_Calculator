import math
def ecf1():
    n=float(input("enter the value of n:"))
    res1= n*1.6*10**-19
    res2=-(n*1.6*10**-19)
    print('THE CLACULATED VALUE IS',res1,'or',res2)
def ecf2():
    s=input("enter which value to calculate(F/q1/q2/r):")
    if s=='F':
        q1=float(input("enter the value of q1:"))
        q2=float(input("enter the value of q2:"))
        r=float(input("enter the value of r:"))
        res=(9*10**9)*((q1*q2)/r**2)
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s=='r':
        q1=float(input("enter the value of q1:"))
        q2=float(input("enter the value of q2:"))
        f=float(input("enter the value of F:"))
        res=((9*10**9)*((q1*q2)/f))**1/2
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s=='q1':
        r=float(input("enter the value of r:"))
        q2=float(input("enter the value of q2:"))
        f=float(input("enter the value of F:"))
        res=(f*r**2)/((9*10**9)*q2)
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s=='q2':
        r=float(input("enter the value of r:"))
        q1=float(input("enter the value of q1:"))
        f=float(input("enter the value of F:"))
        res=(f*r**2)/((9*10**9)*q1)
        print("THE RESULT OF THE CALCULATION IS",res)   
    else:
        print("enter within range")
def ecf3():
    q=float(input("enter the value of q:"))
    r=float(input("enter the value of r:"))
    res=(9*10**9)*(q/r**2)
    print("THE RESULT OF THE CALCULATION IS",res)
def ecf4():
    q=float(input("enter the value of q:"))
    l=float(input("enter the value of l:"))
    res=q*2*l
    print("THE RESULT OF THE CALCULATION IS",res)
def ecf5():
    p=float(input("enter the value of p:"))
    e=float(input("enter the value of E:"))
    o=float(input("enter the value of (o)(theta):"))
    ang=math.sin(o)
    res=p*e*ang
    print("THE RESULT OF THE CALCULATION IS",res)
def ecf6():
    p=float(input("enter the value of p:"))
    e=float(input("enter the value of E:"))
    res=-p*e
    print("THE RESULT OF THE CALCULATION IS",res)
def ecf7():
    q=float(input("enter the value of q:"))
    res=(8.85*10**-12)*q
    print("THE RESULT OF THE CALCULATION IS",res)
def epc1():
    q=float(input("enter the value of q:"))
    r=float(input("enter the value of r:"))
    res=(9*10**9)*(q/r)
    print("THE RESULT OF THE CALCULATION IS",res)
def epc2():
    s=input("enter which value to calculate(C/Q/V):")
    if s=='C':
        q=float(input("enter the value of Q:"))
        v=float(input("enter the value of V:"))
        res=q/v
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s=='Q':
        c=float(input("enter the value of C:"))
        v=float(input("enter the value of V:"))
        res=c*v
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s=='V':
        c=float(input("enter the value of C:"))
        q=float(input("enter the value of Q:"))
        res=q/c
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")
def epc3():
    a=float(input("enter the value of A:"))
    d=float(input("enter the value of d:"))
    e=float(input("enter the value of e(o)(epsilon not):"))
    res=(e*a)/d
    print("THE RESULT OF THE CALCULATION IS",res)
def epc4():
    c=float(input("enter the value of C:"))
    q=float(input("enter the value of q:"))
    res=q/(2*c)
    print("THE RESULT OF THE CALCULATION IS",res)
def epc5():
    c=float(input("enter the value of E:"))
    e=float(input("enter the value of e(o)(epsilon not):"))
    res=(1/2)*e*c**2
    print("THE RESULT OF THE CALCULATION IS",res)
def ce1():
    c=float(input("enter the value of t:"))
    q=float(input("enter the value of q:"))
    res=q/c
    print("THE RESULT OF THE CALCULATION IS",res)
def ce2():
    c=float(input("enter the value of A:"))
    q=float(input("enter the value of I:"))
    res=q/c
    print("THE RESULT OF THE CALCULATION IS",res)
def ce3():
    s=input("enter which value to calculate(I/V/R):")
    if s=='I':
        q=float(input("enter the value of V:"))
        v=float(input("enter the value of R:"))
        res=q/v
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s=='V':
        c=float(input("enter the value of I:"))
        v=float(input("enter the value of R:"))
        res=c*v
        print("THE RESULT OF THE CALCULATION IS",res)
    elif s=='R':
        c=float(input("enter the value of V:"))
        q=float(input("enter the value of I:"))
        res=q/c
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")
def ce4():
    e1=float(input("enter the value of e:"))
    t=float(input("enter the value of t(torque):"))
    m=float(input("enter the value of m:"))
    e2=float(input("enter the value of E:"))
    res=((e1*e2)/m)*t
    print("THE RESULT OF THE CALCULATION IS",res)
def ce5():
    l=float(input("enter the value of l:"))
    r=float(input("enter the value of R:"))
    res=r*((100-l)/l)
    print("THE RESULT OF THE CALCULATION IS",res)
def emi1():
    n=float(input("enter the value of N:"))
    f=float(input("enter the value of d{O}(b)(flux):"))
    t=float(input("enter the value of dt:"))
    res=-(n*f)/t
    print("THE RESULT OF THE CALCULATION IS",res)
def emi2():
    n=float(input("enter the value of N:"))
    f=float(input("enter the value of d{O}(b)(flux):"))
    t=float(input("enter the value of dt:"))
    r=float(input("enter the value of r:"))
    res=-(n/r)*(f/t)
    print("THE RESULT OF THE CALCULATION IS",res)
def emi3():
    b=float(input("enter the value of B:"))
    l=float(input("enter the value of l:"))
    v=float(input("enter the value of v:"))
    res=-b*l*v
    print("THE RESULT OF THE CALCULATION IS",res)
def emi4():
    b=float(input("enter the value of B:"))
    l=float(input("enter the value of l:"))
    v=float(input("enter the value of v:"))
    r=float(input("enter the value of R:"))
    res=(b**2*l**2*v**2)/r
    print("THE RESULT OF THE CALCULATION IS",res)
def emi5():
    m=float(input("enter the value of m(o):"))
    n1=float(input("enter the value of N1:"))
    n2=float(input("enter the value of N2:"))
    a=float(input("enter the value of A:"))
    i=float(input("enter the value of I:"))
    res=(m*n1*n2*a)/i
    print("THE RESULT OF THE CALCULATION IS",res)
def emi6():
    m=float(input("enter the value of m(o):"))
    n=float(input("enter the value of N:"))
    a=float(input("enter the value of A:"))
    i=float(input("enter the value of I:"))
    res=(m*n**2*a)/i
    print("THE RESULT OF THE CALCULATION IS",res)
def ac1():
    v=float(input("enter the value of v:"))
    c=float(input("enter the value of C:"))
    res=1/(2*3.14*v*c)
    print("THE RESULT OF THE CALCULATION IS",res)
def ac2():
    v=float(input("enter the value of v:"))
    c=float(input("enter the value of L:"))
    res=(2*3.14*v*c)
    print("THE RESULT OF THE CALCULATION IS",res)
def ac3():
    l=float(input("enter the value of X(L):"))
    c=float(input("enter the value of X(C):"))
    r=float(input("enter the value of R:"))
    res=(r**2+(l-c))**0.5
    print("THE RESULT OF THE CALCULATION IS",res)
def ac4():
    l=float(input("enter the value of L:"))
    c=float(input("enter the value of C:"))
    res=1/(2*3.14*(l*c)**1/2)
    print("THE RESULT OF THE CALCULATION IS",res)
def ac5():
    l=float(input("enter the value of L:"))
    c=float(input("enter the value of C:"))
    r=float(input("enter the value of R:"))
    res=1/(r*(l/c)**0.5)
    print("THE RESULT OF THE CALCULATION IS",res)

    
    
    
    
    
    

    
    
    
    
    
    

















    





















    
    
