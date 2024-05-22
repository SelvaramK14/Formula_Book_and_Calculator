import math
def vc1():
    a=float(input("enter the value of a(x):"))
    b=float(input("enter the value of a(y):"))
    c=float(input("enter the value of a(z):"))
    res=(a**2+b**2+c**2)**1/2
    print("THE CALCULATED VALUE IS",res)
def vc2():
    o=int(input("enter the value of (o)(theta):"))
    a=float(input("enter the value of a:"))
    b=float(input("enter the value of b:"))
    x=math.cos(o)
    res=a*b*x
    print("THE CALCULATED VALUE IS",res)
def vc3():
    o=int(input("enter the value of (o)(theta):"))
    a=float(input("enter the value of a:"))
    b=float(input("enter the value of b:"))
    x=math.sin(o)
    res=a*b*x
    print("THE CALCULATED VALUE IS",res)
def k1():
    a=float(input("enter the value of r(final):"))
    b=float(input("enter the value of r(initial):"))
    c=float(input("enter the value of t(final):"))
    d=float(input("enter the value of t(initial):"))
    res=(a-b)/(c-d)
    print("THE CALCULATED VALUE IS",res)

def k2():
    a=float(input("enter the value of v(final):"))
    b=float(input("enter the value of v(initial):"))
    c=float(input("enter the value of t(final):"))
    d=float(input("enter the value of t(initial):"))
    res=(a-b)/(c-d)
    print("THE CALCULATED VALUE IS",res)
def k3():
    r=True
    while r==True:
        x=input("enter which value you need to calculate:")
        if x=='v':
            u=float(input("enter the value of u:"))
            a=float(input("enter the value of a:"))
            t=float(input("enter the value of t:"))
            res=u+(a*t)
            print("THE CALCULATED VALUE IS",res)
        elif x=='u':
            v=float(input("enter the value of v:"))
            a=float(input("enter the value of a:"))
            t=float(input("enter the value of t:"))
            res=v-(a*t)
            print("THE CALCULATED VALUE IS",res)
        elif x=='a':
            v=float(input("enter the value of v:"))
            u=float(input("enter the value of u:"))
            t=float(input("enter the value of t:"))
            res=(v-u)/t
            print("THE CALCULATED VALUE IS",res)
        elif x=='t':
            v=float(input("enter the value of v:"))
            u=float(input("enter the value of u:"))
            a=float(input("enter the value of a:"))
            res=(v-u)/a
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def k4():
    r=True
    while r==True:
        x=input("enter which value you need to calculate:")
        if x=='v':
            u=float(input("enter the value of u:"))
            a=float(input("enter the value of a:"))
            s=float(input("enter the value of s:"))
            res=((2*a*s)-u**2)**1/2
            print("THE CALCULATED VALUE IS",res)
        elif x=='u':
            v=float(input("enter the value of v:"))
            a=float(input("enter the value of a:"))
            s=float(input("enter the value of s:"))
            res=((2*a*s)-v**2)**1/2
            print("THE CALCULATED VALUE IS",res)
        elif x=='a':
            v=float(input("enter the value of v:"))
            u=float(input("enter the value of u:"))
            s=float(input("enter the value of s:"))
            res=(v**2-u**2)/(2*s)
            print("THE CALCULATED VALUE IS",res)
        elif x=='s':
            v=float(input("enter the value of v:"))
            u=float(input("enter the value of u:"))
            a=float(input("enter the value of a:"))
            res=(v**2-u**2)/(2*a)
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def wep1():
    o=int(input("enter the value of (o)(theta):"))
    a=float(input("enter the value of F:"))
    b=float(input("enter the value of S:"))
    x=math.cos(o)
    res=a*b*x
    print("THE CALCULATED VALUE IS",res)
def wep2():
    a=float(input("enter the value of m:"))
    b=float(input("enter the value of v:"))
    res=1/2*(a*b**2)
    print("THE CALCULATED VALUE IS",res)
def wep3():
    x=float(input("enter the value of m:"))
    a=float(input("enter the value of g:"))
    b=float(input("enter the value of h:"))
    res=a*b*x
    print("THE CALCULATED VALUE IS",res)
def wep4():
    a=float(input("enter the value of K(final):"))
    b=float(input("enter the value of K(initial:"))
    res=a-b
    print("THE CALCULATED VALUE IS",res)
def wep5():
    r=True
    while r==True:
        x=input("enter which value you need to calculate:")
        if x.upper()=='E':
            U=float(input("enter the value of U:"))
            K=float(input("enter the value of K:"))
            res=U+K
            print("THE CALCULATED VALUE IS",res)
        elif x.upper()=='U':
            E=float(input("enter the value of E:"))
            K=float(input("enter the value of K:"))
            res=E-K
            print("THE CALCULATED VALUE IS",res)
        elif x.upper()=='K':
            E=float(input("enter the value of E:"))
            U=float(input("enter the value of U:"))
            res=E-U
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def wep6():
    a=float(input("enter the value of W(final):"))
    b=float(input("enter the value of W(initial):"))
    c=float(input("enter the value of t(final):"))
    d=float(input("enter the value of t(initial):"))
    res=(a-b)/(c-d)
    print("THE CALCULATED VALUE IS",res)
def g1():
    r=True
    while r==True:
        x=input("enter which value you need to calculate:")
        if x.lower()=='g':
            m1=float(input("enter the value of m1:"))
            m2=float(input("enter the value of m2:"))
            r=float(input("enter the value of r:"))
            f=float(input("enter the value of F:"))
            res=(f*r**2)/(m1*m2)
            print("THE CALCULATED VALUE IS",res)
        elif x.upper()=='F':
            m1=float(input("enter the value of m1:"))
            m2=float(input("enter the value of m2:"))
            r=float(input("enter the value of r:"))
            g=float(input("enter the value of G:"))
            res=(g*m1*m2)/r**2
            print("THE CALCULATED VALUE IS",res)   
        elif x=='r':
            m1=float(input("enter the value of m1:"))
            m2=float(input("enter the value of m2:"))
            f=float(input("enter the value of F:"))
            g=float(input("enter the value of G:"))
            res=((g*m1*m2)/f)**1/2
            print("THE CALCULATED VALUE IS",res)
        elif x=='m1':
            r=float(input("enter the value of r:"))
            m2=float(input("enter the value of m2:"))
            f=float(input("enter the value of F:"))
            g=float(input("enter the value of G:"))
            res=(f*r**2)/(g*m2)
            print("THE CALCULATED VALUE IS",res)
        elif x=='m2':
            r=float(input("enter the value of r:"))
            m1=float(input("enter the value of m1:"))
            f=float(input("enter the value of F:"))
            g=float(input("enter the value of G:"))
            res=(f*r**2)/(g*m1)
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def g2():
    r=True
    while r==True:
        x=input("enter which value you need to calculate:")
        if x.lower()=='u':
            g=float(input("enter the value of G:"))
            M=float(input("enter the value of M:"))
            m=float(input("enter the value of m:"))
            r=float(input("enter the value of r:"))
            res=(g*M*m)/r
            print("THE CALCULATED VALUE IS",res)
        elif x.upper()=='G':
            u=float(input("enter the value of U:"))
            M=float(input("enter the value of M:"))
            m=float(input("enter the value of m:"))
            r=float(input("enter the value of r:"))
            res=(u*r)/(M*m)
            print("THE CALCULATED VALUE IS",res)   
        elif x=='M':
            g=float(input("enter the value of G:"))
            u=float(input("enter the value of U:"))
            m=float(input("enter the value of m:"))
            r=float(input("enter the value of r:"))
            res=(u*r)/(g*m)
            print("THE CALCULATED VALUE IS",res)
        elif x=='m':
            g=float(input("enter the value of G:"))
            u=float(input("enter the value of U:"))
            M=float(input("enter the value of M:"))
            r=float(input("enter the value of r:"))
            res=(u*r)/(g*M)
            print("THE CALCULATED VALUE IS",res)
        elif x=='r':
            g=float(input("enter the value of G:"))
            M=float(input("enter the value of M:"))
            m=float(input("enter the value of m:"))
            U=float(input("enter the value of U:"))
            res=(g*M*m)/U
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def g3():
    r=True
    while r==True:
        x=input("enter which value you need to calculate:")
        if x.lower()=='g':
            g=float(input("enter the value of G:"))
            M=float(input("enter the value of M:"))
            r=float(input("enter the value of r:"))
            res=(g*M)/r
            print("THE CALCULATED VALUE IS",res)
        elif x.upper()=='G':
            g=float(input("enter the value of g:"))
            M=float(input("enter the value of M:"))
            r=float(input("enter the value of r:"))
            res=(g*r)/M
            print("THE CALCULATED VALUE IS",res)   
        elif x=='M':
            G=float(input("enter the value of G:"))
            g=float(input("enter the value of g:"))
            r=float(input("enter the value of r:"))
            res=(g*r)/G
            print("THE CALCULATED VALUE IS",res)
        elif x=='r':
            G=float(input("enter the value of G:"))
            g=float(input("enter the value of g:"))
            M=float(input("enter the value of M:"))
            res=(G*M)/g
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def re1():
    r=True
    while r==True:
        x=input("enter which value you need to calculate:")
        if x.lower()=='f':
            r=float(input("enter the value of R:"))
            res=r/2
            print("THE CALCULATED VALUE IS",res)
        elif x.upper()=='R':
            f=float(input("enter the value of F:"))
            res=2*f
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def re2():
    r=True
    while r==True:
        x=input("enter which value you need to calculate:")
        if x.lower()=='v':
            u=float(input("enter the value of u:"))
            f=float(input("enter the value of f:"))
            res=(u*f)/(u+f)
            print("THE CALCULATED VALUE IS",res)
        elif x.lower()=='f':
            u=float(input("enter the value of u:"))
            v=float(input("enter the value of v:"))
            res=(u*v)/(u-v)
            print("THE CALCULATED VALUE IS",res)
        elif x.lower()=='u':
            f=float(input("enter the value of f:"))
            v=float(input("enter the value of v:"))
            res=(f*v)/(f-v)
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def re3():
    r=True
    while r==True:
        x=input("enter which value you need to calculate:")
        if x.lower()=='v':
            u=float(input("enter the value of u:"))
            m=float(input("enter the value of m:"))
            res=-(m*u)
            print("THE CALCULATED VALUE IS",res)
        elif x.lower()=='m':
            u=float(input("enter the value of u:"))
            v=float(input("enter the value of v:"))
            res=-(v*u)
            print("THE CALCULATED VALUE IS",res)
        elif x.lower()=='u':
            m=float(input("enter the value of m:"))
            v=float(input("enter the value of v:"))
            res=-(v/m)
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def ht1():
    r=True
    while r==True:
        x=input("enter which value you need to calculate(p/V):")
        if x.lower()=='p':
            n=float(input("enter the value of n:"))
            r=float(input("enter the value of R:"))
            t=float(input("enter the value of T:"))
            v=float(input("enter the value of V:"))
            res=(n*r*t)/v
            print("THE CALCULATED VALUE IS",res)
        elif x.lower()=='m':
            n=float(input("enter the value of n:"))
            r=float(input("enter the value of R:"))
            t=float(input("enter the value of T:"))
            p=float(input("enter the value of p:"))
            res=(n*r*t)/p
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def ht2():
    r=True
    while r==True:
        x=input("enter which value you need to calculate(F/A):")
        if x.lower()=='f':
            y=float(input("enter the value of Y:"))
            a=float(input("enter the value of A:"))
            ln=float(input("enter the value of DEL l:"))
            l=float(input("enter the value of l:"))
            res=y*a*(ln/l)
            print("THE CALCULATED VALUE IS",res)
        elif x.lower()=='a':
            y=float(input("enter the value of Y:"))
            f=float(input("enter the value of F:"))
            ln=float(input("enter the value of DEL l:"))
            l=float(input("enter the value of l:"))
            res=f/(y*(ln/l))
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
    
def sh1():
    #s=Q/m*del 
    q=float(input("enter the value of Q:"))
    m=float(input("enter the value of m:"))
    t=float(input("enter the value of DEL T:"))
    res=(q/m)*t
    print("THE CALCULATED VALUE IS",res)
def sh2():
    r=True
    while r==True:
        x=input("enter which value you need to calculate:")
        if x.lower()=='l':
            q=float(input("enter the value of Q:"))
            m=float(input("enter the value of m:"))
            res=q/m
            print("THE CALCULATED VALUE IS",res)
        elif x.lower()=='q':
            l=float(input("enter the value of L:"))
            m=float(input("enter the value of m:"))
            res=l*m
            print("THE CALCULATED VALUE IS",res)
        elif x.lower()=='m':
            l=float(input("enter the value of L:"))
            q=float(input("enter the value of Q:"))
            res=q/l
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def sh3():
    r=True
    while r==True:
        x=input("enter which value you need to calculate(C(p)/C(r)/R):")
        if x=='C(p)':
            c1=float(input("enter the value of C(r):"))
            r=float(input("enter the value of R:"))
            res=r+c1
            print("THE CALCULATED VALUE IS",res)
        elif x=='C(r)':
            c2=float(input("enter the value of C(p):"))
            r=float(input("enter the value of R:"))
            res=c2-r
            print("THE CALCULATED VALUE IS",res)
        elif x.lower()=='r':
            c1=float(input("enter the value of C(p):"))
            c2=float(input("enter the value of C(r):"))
            res=c2-c1
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
def sh4():
    r=True
    while r==True:
        x=input("enter which value you need to calculate:")
        if x.lower()=='u':
            f=float(input("enter the value of f:"))
            r=float(input("enter the value of R:"))
            t=float(input("enter the value of T:"))
            res=(f/2)*r*t
            print("THE CALCULATED VALUE IS",res)
        elif x.lower()=='f':
            u=float(input("enter the value of U:"))
            r=float(input("enter the value of R:"))
            t=float(input("enter the value of T:"))
            res=(u*2)/(r*t)
            print("THE CALCULATED VALUE IS",res)   
        elif x.lower()=='r':
            f=float(input("enter the value of f:"))
            u=float(input("enter the value of U:"))
            t=float(input("enter the value of T:"))
            res=(u*2)/(f*t)
            print("THE CALCULATED VALUE IS",res)
        elif x.lower()=='t':
            f=float(input("enter the value of f:"))
            r=float(input("enter the value of R:"))
            u=float(input("enter the value of U:"))
            res=(u*2)/(f*r)
            print("THE CALCULATED VALUE IS",res)
        else:
            print("enter within the range")
        
        x=input("Do you want calculate more(Y/N):")
        if x.lower()=='y':
            r=True
        else:
            r=False
    
    
    
    




























    
        




















    
    
