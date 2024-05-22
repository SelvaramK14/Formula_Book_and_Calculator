def mirrorfor():
    c='y'
    while c.lower()=='y':
        h=input('ENTER WHICH VALUE YOU NEED CALCULATE(u/v/f):')
        if h.lower()=='u':
            v=float(input('ENTER THE IMAGE DISTANCE:'))
            f=float(input('ENTER THE FOCAL LENGTH:'))
            res=(v*f)/(v-f)
            print('THE OBJECT DISTANCE(u) IS',res)
        elif h.lower()=='v':
            v=float(input('ENTER THE OBJECT DISTANCE:'))
            f=float(input('ENTER THE FOCAL LENGTH:'))
            res=(v*f)/(v-f)
            print('THE IMAGE DISTANCE(v) IS',res)
        elif h.lower()=='f':
            v=float(input('ENTER THE IMAGE DISTANCE:'))
            u=float(input('ENTER THE OBJECT LENGTH:'))
            res=(u*v)/(v+u)
            print('THE OBJECT DISTANCE(u) IS',res)
        else:
            print('ENTER WITHIN THE OPTIONS')
        c=input('DO YOU WANT TO CALCULATE THE MORE(Y/N):')
   

def mag():
    c='y'
    while c.lower()=='y':
        H1=float(input('ENTER THE HEIGHT OF THE IMAGE:'))
        H2=float(input('ENTER THE HEIGHT OF THE OBJECT:'))
        res=H1/H2
        print('THE MAGNIFICATION IS',res)
        c=input('DO YOU WANT TO CALCULATE THE MORE(Y/N):')
    
def refindex():
    c='y'
    while c.lower()=='y':
        v1=float(input('ENTER THE SPEED OF LIGHT IN MEDIUM 1:'))
        v2=float(input('ENTER THE SPEED OF LIGHT IN MEDIUM 2:'))
        res=v2/v1
        print('THE REFRACTIVE INDEX IS',res)
        c=input('DO YOU WANT TO CALCULATE THE MORE(Y/N):')
    
def abrefindex():
    c='y'
    while c.lower()=='y':
        v1=float(input('ENTER THE SPEED OF LIGHT IN AIR:'))
        v2=float(input('ENTER THE SPEED OF LIGHT IN MEDIUM:'))
        res=v1/v2
        print('THE  ABSOLUTE REFRACTIVE INDEX IS',res)
        c=input('DO YOU WANT TO CALCULATE MORE(Y/N):')
    
def lensfor():
    c='y'
    h=input('ENTER WHICH VALUE YOU NEED CALCULATE(u/v/f):')
    while c.lower()=='y':
        if h.lower()=='u':
            v=float(input('ENTER THE IMAGE DISTANCE:'))
            f=float(input('ENTER THE FOCAL LENGTH:'))
            res=v*f/v+f
            print('THE OBJECT DISTANCE(u) IS',res)
        elif h.lower()=='v':
            v=float(input('ENTER THE OBJECT DISTANCE:'))
            f=float(input('ENTER THE FOCAL LENGTH:'))
            res=v*f/v+f
            print('THE IMAGE DISTANCE(v) IS',res)
        elif h.lower()=='f':
            v=float(input('ENTER THE IMAGE DISTANCE:'))
            u=float(input('ENTER THE OBJECT LENGTH:'))
            res=u*v/v-u
            print('THE OBJECT DISTANCE(u) IS',res)
        else:
            print('ENTER WITHIN THE OPTIONS')
        c=input('DO YOU WANT TO CALCULATE THE MORE(Y/N):')
   
def lenmag():
    c='y'
    while c.lower()=='y':
        H1=float(input('ENTER THE HEIGHT OF THE IMAGE:'))
        H2=float(input('ENTER THE HEIGHT OF THE OBJECT:'))
        res=H1/H2
        print('THE MAGNIFICATION IS',res)
        c=input('DO YOU WANT TO CALCULATE THE MORE(Y/N):')
   
def powoflens():
    c='y'
    while c.lower()=='y':
        H1=float(input('ENTER THE FOCAL LENGTH:'))
        res=1/H1
        print('THE POWER OF LENS IS',res)
        c=input('DO YOU WANT TO CALCULATE THE MORE(Y/N):')
    
def heat():
    c='y'
    while c.lower()=='y':
        I=float(input('ENTER THE AMOUNT OF CURRENT:'))
        R=float(input('ENTER THE RESISTANCE OF THE RESISTOR:'))
        T=float(input('ENTER THE TIME THAT THE CURRENT FLOWS:'))
        J=I**2*R*T
        print('THE HEAT PRODUCES IS',J)
        c=input('DO YOU WANT TO CALCULATE THE MORE(Y/N):')
    
def resistance():
    c='y'
    while c.lower()=='y':
        p=float(input('ENTER THE RESISTIVITY VALUE:'))
        l=float(input('ENTER THE LENGTH OF THE CONDUCTOR:'))
        A=float(input('ENTER THE AREA OF CROSS SECTION:'))
        res=p*(l/A)
        print('THE ELECTRIC RESISTANCE IS',res)
        c=input('DO YOU WANT TO CALCULATE THE MORE(Y/N):')
    
def electricpow():
    c='y'
    while c.lower()=='y':
        p=float(input('ENTER THE WORKDONE:'))
        t=float(input('ENTER THE TIME TAKEN:'))
        res=p/t
        print('THE ELECTRIC POWER IS',res)
        c=input('DO YOU WANT TO CALCULATE THE MORE(Y/N):')
    
    
    
    

    

    
    

    
            
