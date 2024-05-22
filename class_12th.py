from class_12_2 import chem12
from class_12_2 import phy12
import mysql.connector as mys
mycon=mys.connect(host='localhost',username='root',passwd='selva',database='student')
mycursor=mycon.cursor()


def chem_12():
    d=['SOLID STATE(1)','SOLUTIONS(2)','ELECTRO CHEMISTRY(3)','CHEMICAL KINETICS(4)']
    print('THE AVAILABLE CHAPTERS ARE:')
    for i in d:
        print(i)
    print('#THE FORMULAS CAN BE ACCESSED THROUGH THE NUMBER AT END OF IT#')
    print("\n")
    p=int(input('ENTER THE NUMBER OF THE CHAPTER YOU ARE SEARCHING FOR:'))
    if p==1:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from chem_12 where unit='solid state'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS a=2r")
                chem12.ss1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS a=4/sqrt(3)*r")
                chem12.ss2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS a=2*sqrt(2)*r")
                chem12.ss3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS d=(Z*M)/(a^3*N(A))")
                chem12.ss4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS (d*N(A)/M)*(4*PI*r^3/3)*100")
                chem12.ss5()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')    
        else:
            print('%%%CALCULATION OVER%%%')
    elif p==2:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from chem_12 where unit='solutions'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS x(A)=n(A)/n(A)+n(B) and x(B)=n(B)/n(A)+n(B)")
                chem12.s1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS M=moles of solute/volume of solution in litres")
                chem12.s2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS m=moles of solute/mass of solvent in kilograms")
                chem12.s3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS pi=i*C*R*T ")
                chem12.s4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS i=normal molar mass/abnormal molar mass")
                chem12.s5()
            elif s==6:
                print("THE CHOOSEN FORMULA IS del T(b)=i*K(b)*m")
                chem12.s6()
            elif s==7:
                print("THE CHOOSEN FORMULA IS del T(f)=i*K(f)*m")
                chem12.s7()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')    
        else:
            print('%%%CALCULATION OVER%%%')
    elif p==3:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from chem_12 where unit='electro chemistry'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS K=(1/R)*(l/A)")
                chem12.ec1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS A(m)=1000*k/c")
                chem12.ec2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS E=(E^+)-(2.303*R*T)/(n*F)*log(1/(M^n+))")
                chem12.ec3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS E(o)cell=(0.059*v/n)*log K(c)")
                chem12.ec4()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')    
        else:
            print('%%%CALCULATION OVER%%%')
    elif p==4:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from chem_12 where unit='chemical kinetics'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS k=[R(0)]-[R]/t")
                chem12.ck1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS t(1/2)=[R(0)]/2*k")
                chem12.ck2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS k=(2.303/t)*log([R]o/[R])")
                chem12.ck3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS t(1/2)=0.693/k")
                chem12.ck4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS k=A(e)^(-Ea*R*T)")
                chem12.ck5()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')    
        else:
            print('%%%CALCULATION OVER%%%')
def math_12():
    d=['INVERSE TRIGONOMETRIC FUNCTIONS(1)','CONTINUITY(2)','DIFFERENTIABILITY(3)']
    print('THE AVAILABLE CHAPTERS ARE:')
    for i in d:
        print(i)
    print("\n")
    print("Here '(o)' means theta")
    print("Here '^' means to 'to the power'(exponent)")
    print("\n")
    print("!!!SORRY FOR THE INCONVENIENCE, THE FOLLOWING FORMULA FROM ABOVE MENTIONED CHAPTERS CANNOT BE CALCULATED!!!")
    print("\n")
    p=int(input('ENTER THE NUMBER OF THE CHAPTER YOU ARE SEARCHING FOR:'))
    if p==1:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from math_12 where unit='Inverse trigonometric functions'")
        rec=mycursor.fetchall()
        for i,e in rec:
            print(i)
    elif p==2:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from math_12 where unit='Continuity'")
        rec=mycursor.fetchall()
        for i,e in rec:
            print(i)
    elif p==3:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from math_12 where unit='Differentiability'")
        rec=mycursor.fetchall()
        for i,e in rec:
            print(i)
    else:
        print("CHOOSE WITHIN THE GIVEN OPTIONS")

def phy_12():
    d=['ELECTRIC CHARGES AND FIELDS(1)','ELECTROSTAIC POTENTIAL AND CAPACITANCE(2)','CURRENT ELECTRICITY(3)','ELECTRO MAGNETIC INDUCTION(4)','ALTERNATING CURRENT(5)']
    print('THE AVAILABLE CHAPTERS ARE:')
    for i in d:
        print(i)
    print('#THE FORMULAS CAN BE ACCESSED THROUGH THE NUMBER AT END OF IT#')
    print("\n")
    print("HERE,")
    print("'{O}' MEANS FLUX")
    print("'e(o)' MEANS EPSILON NOT")
    print("'t' MEANS TORQUE")
    print("'(o)' MEANS THETA")
    print("\n")
    p=int(input('ENTER THE NUMBER OF THE CHAPTER YOU ARE SEARCHING FOR:'))
    if p==1:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_12 where unit='Electric charges and fields'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS q=+ne or -ne")
                phy12.ecf1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS F=k*(q1*q2)/r^2")
                phy12.ecf2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS E=1/(4*pi*e(o))*(q/r^2)")
                phy12.ecf3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS p=q*2*l")
                phy12.ecf4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS t=p*E*sin (o)")
                phy12.ecf5()
            elif s==6:
                print("THE CHOOSEN FORMULA IS W= -p*E")
                phy12.ecf6()
            elif s==7:
                print("THE CHOOSEN FORMULA IS Flux=(1/e(o))*q")
                phy12.ecf7()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')    
        else:
            print('%%%CALCULATION OVER%%%')
    elif p==2:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_12 where unit='Electrostaic potential and capacitance'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS V=1/(4*pi*e(o))*(q/r)")
                phy12.epc1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS C=Q/V")
                phy12.epc2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS C=e(o)*A/d")
                phy12.epc3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS U=q^2/2*C")
                phy12.epc4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS U=1/2*e(o)*E^2")
                phy12.epc5()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')    
        else:
            print('%%%CALCULATION OVER%%%')
    elif p==3:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_12 where unit='Current electricity'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS I= q/t")
                phy12.ce1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS J= I/A")
                phy12.ce2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS V=I*R")
                phy12.ce3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS V(d)= (e*E/m)*t")
                phy12.ce4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS S=R*((100-l)/l)")
                phy12.ce5()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')    
        else:
            print('%%%CALCULATION OVER%%%')
    elif p==4:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_12 where unit='Electro magnetic induction'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS e= -Nd{O}(b)/dt")
                phy12.emi1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS I=-(N/r)*(d{O}(b))/dt")
                phy12.emi2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS e= -Blv")
                phy12.emi3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS P= B^2*l^2*v^2/R")
                phy12.emi4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS M=m(o)*N1*N2*A/I")
                phy12.emi5()
            elif s==6:
                print("THE CHOOSEN FORMULA IS L=m(o)*N**2*A/I")
                phy12.emi6()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')    
        else:
            print('%%%CALCULATION OVER%%%')
    elif p==5:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_12 where unit='Alternating current'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS X(C)=1/(2*pi*v*C)")
                phy12.ac1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS X(L)= 2*pi*v*L")
                phy12.ac2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS Z=(R^2+(X(L)-X(C))^1/2")
                phy12.ac3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS v(r)= 1/(2*pi*(L*C)^1/2)")
                phy12.ac4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS Q-fact=1/R(L/C)^1/2")
                phy12.ac5()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')    
        else:
            print('%%%CALCULATION OVER%%%')
        
        
            
                
        
    
            


























        

    
    
    
                                

