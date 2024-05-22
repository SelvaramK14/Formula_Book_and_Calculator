import math
def statom():
    h=float(input("enter the value of h:"))
    x=float(input("enter the value of delta x:"))
    m=float(input("enter the value of m:"))
    res=h/(4*3.14*x*m)
    print("THE RESULT OF THE CALCULATION IS",res)
def bcoc1():
    mass=float(input("enter the mass:"))
    volume=float(input("enter the volume:"))
    res=mass/volume
    print("THE RESULT OF THE CALCULATION IS",res)
def bcoc2():
    mass=float(input("enter the mass of the compund:"))
    mmass=float(input("enter the molar mass of compound:"))
    res=(mass*100)/mmass
    print("THE RESULT OF THE CALCULATION IS",res)
def bcoc3():
    mass=float(input("enter the mass of the solute:"))
    mmass=float(input("enter the molar mass of solution:"))
    res=(mass/mmass)*100
    print("THE RESULT OF THE CALCULATION IS",res)
def bcoc4():
    mass=float(input("enter the no. of moles in A:"))
    mmass=float(input("enter the no. of moles in the solution:"))
    res=mass/mmass
    print("THE RESULT OF THE CALCULATION IS",res)
def bcoc5():
    mass=float(input("enter the no. of moles of solute:"))
    mmass=float(input("enter the volume of solution in litres:"))
    res=mass/mmass
    print("THE RESULT OF THE CALCULATION IS",res)
def bcoc6():
    mass=float(input("enter the no. of moles of solute:"))
    mmass=float(input("enter the volume of solvent in kg:"))
    res=mass/mmass
    print("THE RESULT OF THE CALCULATION IS",res)
def ther1():
    a=input("enter which value to calculate(U/q/w):")
    if a.upper()=='U':
        q=float(input("enter the value of q:"))
        w=float(input("enter the value of w:"))
        res=q+w
        print("THE RESULT OF THE CALCULATION IS",res)
    elif a.upper()=='Q':
        u=float(input("enter the value of delta U:"))
        w=float(input("enter the value of w:"))
        res=u-w
        print("THE RESULT OF THE CALCULATION IS",res)
    elif a.upper()=='W':
        u=float(input("enter the value of delta U:"))
        q=float(input("enter the value of q:"))
        res=u-q
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")
def ther2():
    a=input("enter which value to calculate(n/w/T):")
    if a.upper()=='N':
        w=float(input("enter the value of w(rev):"))
        t=float(input("enter the value of T:"))
        v1=float(input("enter the value of V(i):"))
        v2=float(input("enter the value of V(j):"))
        q=v2/v1
        s=math.log(q,math.e)
        res=w/(2.303*1.987*t*s)
        print("THE RESULT OF THE CALCULATION IS",res)
    elif a.upper()=='W':
        n=float(input("enter the value of n:"))
        t=float(input("enter the value of T:"))
        v1=float(input("enter the value of V(i):"))
        v2=float(input("enter the value of V(j):"))
        q=v2/v1
        s=math.log(q,math.e)
        res=2.303*1.987*t*s*n
        print("THE RESULT OF THE CALCULATION IS",res)
    elif a.upper()=='T':
        n=float(input("enter the value of n:"))
        w=float(input("enter the value of w(rev):"))
        v1=float(input("enter the value of V(i):"))
        v2=float(input("enter the value of V(j):"))
        q=v2/v1
        s=math.log(q,math.e)
        res=w/2.303*1.987*s*n
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")

def ther3():
    a=input("enter which value to calculate(U/V/H/p):")
    if a.upper()=='H':
        u=float(input("enter the value of U:"))
        p=float(input("enter the value of P:"))
        v=float(input("enter the value of V:"))
        res=u+p*v
        print("THE RESULT OF THE CALCULATION IS",res)
    elif a.upper()=='U':
        h=float(input("enter the value of H:"))
        v=float(input("enter the value of V:"))
        p=float(input("enter the value of p:"))
        res=h-p*v
        print("THE RESULT OF THE CALCULATION IS",res)
    elif a.upper()=='V':
        h=float(input("enter the value of H:"))
        u=float(input("enter the value of U:"))
        p=float(input("enter the value of p:"))
        res=(h-u)/p
        print("THE RESULT OF THE CALCULATION IS",res)
        
    elif a.upper()=='P':
        h=float(input("enter the value of H:"))
        u=float(input("enter the value of U:"))
        v=float(input("enter the value of V:"))
        res=(h-u)/v
        print("THE RESULT OF THE CALCULATION IS",res)
        
    else:
        print("enter within range")
def ther4():
    a=input("enter which value to calculate(G/H/T/S):")
    if a.upper()=='H':
        g=float(input("enter the value of del(r)G:"))
        s=float(input("enter the value of del(r)S:"))
        t=float(input("enter the value of T:"))
        res=g-(t*s)
        print("THE RESULT OF THE CALCULATION IS",res)
    elif a.upper()=='G':
        h=float(input("enter the value of del(r)H:"))
        s=float(input("enter the value of del(r)S:"))
        t=float(input("enter the value of T:"))
        res=h+(t*s)
        print("THE RESULT OF THE CALCULATION IS",res)
    elif a.upper()=='T':
        h=float(input("enter the value of del(r)H:"))
        s=float(input("enter the value of del(r)S:"))
        g=float(input("enter the value of del(r)G:"))
        res=(g-h)/s
        print("THE RESULT OF THE CALCULATION IS",res)
    elif a.upper()=='S':
        h=float(input("enter the value of del(r)H:"))
        t=float(input("enter the value of T:"))
        g=float(input("enter the value of del(r)G:"))
        res=(g-h)/t
        print("THE RESULT OF THE CALCULATION IS",res)
    else:
        print("enter within range")
def cb1():
    a=float(input("enter the no. of valence elctrons:"))
    b=float(input("enter the no. of lone pair elctrons:"))
    c=float(input("enter the no. of bonding pair electrons:"))
    res=a-b-((1/2)*c)
    print("THE RESULT OF THE CALCULATION IS",res)
def cb2():
    a=float(input("enter the no.of electron in bonding orbital:"))
    b=float(input("enter the no.of elctron in antibonding orbital):"))
    res=(a-b)/2
    print("THE RESULT OF THE CALCULATION IS",res)

    















    


    
