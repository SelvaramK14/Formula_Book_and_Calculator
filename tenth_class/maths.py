def realnum():
    en=input("WHICH VALUE U NEED TO FIND:")
    if en.lower()=='a':
        b=float(input("enter the value of b:"))
        q=float(input("enter the value of q:"))
        r=float(input("enter the value of r:"))
        res=(b*q)+r
        print("the result will be",res)
    elif en.lower()=='b':
        a=float(input("enter the value of a:"))
        q=float(input("enter the value of q:"))
        r=float(input("enter the value of r:"))
        res=(a-r)/q
        print("the result will be",res)
    elif en.lower()=='b':
        a=float(input("enter the value of a:"))
        b=float(input("enter the value of b:"))
        r=float(input("enter the value of r:"))
        res=(a-r)/b
        print("the result will be",res)
    elif en.lower()=='b':
        a=float(input("enter the value of a:"))
        q=float(input("enter the value of q:"))
        b=float(input("enter the value of b:"))
        res=a/(b*q)
        print("the result will be",res)
    else:
        print("enter within range")
                                               
def linereqn1():
    a=float(input("enter the value of a:"))
    b=float(input("enter the value of b:"))
    res=a**2+b**2+2*a*b
    print("THE CALCULATED VALUE IS",res)
def linereqn2():
    a=float(input("enter the value of a:"))
    b=float(input("enter the value of b:"))
    res=a**2+b**2-2*a*b
    print("THE CALCULATED VALUE IS",res)
def linereqn3():
    a=float(input("enter the value of a:"))
    b=float(input("enter the value of b:"))
    res=a**2-b**2
    print("THE CALCULATED VALUE IS",res)
def linereqn4():
    a=float(input("enter the value of a:"))
    b=float(input("enter the value of b:"))
    res=a**3+b**3+3*a*b
    print("THE CALCULATED VALUE IS",res)
def linereqn5():
    a=float(input("enter the value of a:"))
    b=float(input("enter the value of b:"))
    res=(a+b)*(a**2-a*b+b**2)
    print("THE CALCULATED VALUE IS",res)
def linereqn6():
    a=float(input("enter the value of a:"))
    b=float(input("enter the value of b:"))
    c=float(input("enter the value of c:"))
    res=(a+b+c)*(a**2+b**2+c**2-(a*b)-(b*c)-(c*a))
    print("THE CALCULATED VALUE IS",res)
def quardratic():
    a=float(input("enter the value of a:"))
    b=float(input("enter the value of b:"))
    c=float(input("enter the value of c:"))
    d=(b**2-4*a*c)**1/2
    res=-b+d
    res1=-b-d
    print("THE CALCULATED VALUE IS",res,'or',res1)
def volume1():
    l=float(input('enter the length of cubiod:'))
    b=float(input('enter the breadth of cubiod:'))
    h=float(input('enter the height of cubiod:'))
    res=l*b*h
    print("THE CALCULATED VALUE IS",res)
def volume2():
    l=float(input('enter the side of cube:'))
    res=l**3
    print("THE CALCULATED VALUE IS",res)
def volume3():
    r=float(input('enter the radius of cylinder:'))
    h=float(input('enter the height of cylinder:'))
    res=3.14*r**2*h
    print("THE CALCULATED VALUE IS",res)
def volume4():
    r=float(input('enter the radius of cone:'))
    h=float(input('enter the height of cone:'))
    res=(1/3)*3.14*r**2*h
    print("THE CALCULATED VALUE IS",res)
def volume5():
    r=float(input('enter the radius of sphere:'))
    res=(4/3)*3.14*r**3
    print("THE CALCULATED VALUE IS",res)
def volume6():
    r=float(input('enter the radius of hemisphere:'))
    res=(2/3)*3.14*r**2
    print("THE CALCULATED VALUE IS",res)
def surfarea1():
    l=float(input('enter the length of cubiod:'))
    b=float(input('enter the breadth of cubiod:'))
    h=float(input('enter the height of cubiod:'))
    res=2*h*(l+b)
    print("THE CALCULATED VALUE IS",res)
def surfarea2():
    l=float(input('enter the side of cube:'))
    res=4*l**2
    print("THE CALCULATED VALUE IS",res)
def surfarea3():
    r=float(input('enter the radius of cylinder:'))
    h=float(input('enter the height of cylinder:'))
    res=2*3.14*r*h
    print("THE CALCULATED VALUE IS",res)
def surfarea4():
    r=float(input('enter the radius of cone:'))
    h=float(input('enter the slant height of cone:'))
    res=3.14*r*h
    print("THE CALCULATED VALUE IS",res)
def surfarea5():
    r=float(input('enter the radius of sphere:'))
    res=4*3.14*r**2
    print("THE CALCULATED VALUE IS",res)
def surfarea6():
    r=float(input('enter the radius of hemisphere:'))
    res=2*3.14*r**2
    print("THE CALCULATED VALUE IS",res)
def area1():
    l=float(input('enter the length of cubiod:'))
    b=float(input('enter the breadth of cubiod:'))
    h=float(input('enter the height of cubiod:'))
    res=2*(l*b+b*h+h*l)
    print("THE CALCULATED VALUE IS",res)
def area2():
    l=float(input('enter the side of cube:'))
    res=6*l**2
    print("THE CALCULATED VALUE IS",res)
def area3():
    r=float(input('enter the radius of cylinder:'))
    h=float(input('enter the height of cylinder:'))
    res=2*3.14*r*(h+r)
    print("THE CALCULATED VALUE IS",res)
def area4():
    r=float(input('enter the radius of cone:'))
    l=float(input('enter the slant height of cone:'))
    res=3.14*r*(l+r)
    print("THE CALCULATED VALUE IS",res)
def area5():
    r=float(input('enter the radius of sphere:'))
    res=4*3.14*r**2
    print("THE CALCULATED VALUE IS",res)
def area6():
    r=float(input('enter the radius of hemisphere:'))
    res=3*3.14*r**2
    print("THE CALCULATED VALUE IS",res)
def probability():
    a=float(input('enter the value of favourable outcomes:'))
    b=float(input('enter the value of total outcomes:'))
    res=a/b
    print("THE CALCULATED VALUE IS",res)
def ap1():
    a=float(input("enter the value of first term(a):"))
    d=float(input("enter the value of common difference(d):"))
    n=float(input("enter the value of number of terms(n):"))
    res=a+(n-1)*d
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS", res)
def ap2():
    a=float(input("enter the value of first term(a):"))
    d=float(input("enter the value of common difference(d):"))
    n=float(input("enter the value of number of terms(n):"))
    res=n/2*(2*a+(n-1)*d)
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS", res)
def cg1():
    x1=float(input("enter the value of x1:"))
    x2=float(input("enter the value of x2:"))
    y1=float(input("enter the value of y1:"))
    y2=float(input("enter the value of y2:"))
    res=((x2-x1)+(y2-y1))**1/2
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS", res)
def cg2():
    x1=float(input("enter the value of x1:"))
    x2=float(input("enter the value of x2:"))
    y1=float(input("enter the value of y1:"))
    y2=float(input("enter the value of y2:"))
    m=float(input("enter the value of m:"))
    n=float(input("enter the value of n:"))
    res=(((m*x2)+(n*x1))/(m+n))
    res1=(((m*y2)+(n*y1))/(m+n))
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS", "[",res,",",res1,"]")
def cg3():
    x1=float(input("enter the value of x1:"))
    x2=float(input("enter the value of x2:"))
    y1=float(input("enter the value of y1:"))
    y2=float(input("enter the value of y2:"))
    res=(x1+x2)/2
    res1=(y1+y2)/2
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS", "[",res,",",res1,"]")
def cg4():
    x1=float(input("enter the value of x1:"))
    x2=float(input("enter the value of x2:"))
    x3=float(input("enter the value of x3:"))
    y1=float(input("enter the value of y1:"))
    y2=float(input("enter the value of y2:"))
    y3=float(input("enter the value of y3:"))
    res=1/2*(x1*(y2-y3)+x2*(y3-y1)+x3*(y1-y2))
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS",res)
def st1():
    n=float(input("enter the value of n:"))
    cf=float(input("enter the value of cf:"))
    f=float(input("enter the value of f:"))
    h=float(input("enter the value of h:"))
    l=float(input("enter the value of l:"))
    res=l+(((n/2)-cf)/f)*h
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS",res)
def st2():
    f0=float(input("enter the value of f0:"))
    f1=float(input("enter the value of f1:"))
    f2=float(input("enter the value of f2:"))
    h=float(input("enter the value of h:"))
    l=float(input("enter the value of l:"))
    res=l+((f2-f0)/((2*f1)-f0-f2))*h
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS",res)
def cl1():
    r=float(input("enter the value of radius of the circle"))
    res=3.14*r**2
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS",res)
def cl2():
    r=float(input("enter the value of radius of the circle"))
    res=2*3.14*r
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS",res)
def cl3():
    o=int(input("enter the angle of the sector:"))
    r=float(input("enter the value of radius of the circle"))
    res=(o/360)*3.14*r**2
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS",res)
def cl4():
    o=int(input("enter the angle of the sector:"))
    r=float(input("enter the value of radius of the circle"))
    res=(o/360)*2*3.14*r
    print("THE CALCULATED VALUE FOR ABOVE INPUTS IS",res) 

    


    

    













    
               
            
            
