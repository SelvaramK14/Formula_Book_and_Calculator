from class_11_1 import math11
from class_11_1 import phy11
from class_11_1 import chem11

import mysql.connector as mys
mycon=mys.connect(host='localhost',username='root',passwd='selva',database='student')
mycursor=mycon.cursor()

def chem_11():
    d=['STRUCTURE OF ATOM(1)','SOME BASIC CONCEPTS OF CHEMISTRY(2)','THERMODYNAMICS(3)','CHEMICAL BONDING AND MOLECULAR STRUCTURE(4)']
    print('THE AVAILABLE CHAPTERS ARE:')
    for i in d:
        print(i)
    print('#THE FORMULAS CAN BE ACCESSED THROUGH THE NUMBER AT END OF IT#')
    p=int(input('ENTER THE NUMBER OF THE CHAPTER YOU ARE SEARCHING FOR:'))
    if p==1:
        mycursor.execute("select * from chem_11 where unit='structure of atom'")
        print("THE AVAILABLE FORMULA IN THIS CHAPTER IS")
        rec=mycursor.fetchall()
        for i,e,y in rec:
            print(i.upper())
        c=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
        while c.lower()=='y':
            for i,e,y in rec:
                print("the formula is",e)
            chem11.statom()
            c=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
        else:
            print("CALCULATION OVER")
    elif p==2:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from chem_11 where unit='some basic concepts of chemistry'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS density=mass/volume ")
                chem11.bcoc1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS mass of the compound*100/molar mass of the compound")
                chem11.bcoc2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS (mass of solute/mass of solution)*100")
                chem11.bcoc3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS no. of moles in A/no. of moles in the solutions")
                chem11.bcoc4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS no. of moles of solute/volume of solution in litres")
                chem11.bcoc5()
            elif s==6:
                print("THE CHOOSEN FORMULA IS no. of moles of solute/mass of solvent in kg")
                chem11.bcoc6()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')    
        else:
            print('%%%CALCULATION OVER%%%')
    elif p==3:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from chem_11 where unit='thermodynamics'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS delU=q+w ")
                chem11.ther1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS w(rev)=-2.303nRTlog(V(f)/V(i))")
                chem11.ther2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS H=U+pV")
                chem11.ther3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS del(r)G=del(r)H+T.del(r)S")
                chem11.ther4()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print('%%%CALCULATION OVER%%%')
    elif p==4:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from chem_11 where unit='chemical bonding and molecular structure'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("the choosen formula is total no. of valence electron-total no. of lone pair-1/2(no. of bonding electron)")
                chem11.cb1()
            elif s==2:
                print("the choosen formula is (no.of electron in bonding orbital-no.of elctron in antibonding orbital)/2 ")
                chem11.cb2()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print('%%%CALCULATION OVER%%%')



def math_11():
    d=['Trigonometric Functions(1)','Complex Numbers And Quadratic Equations(2)','Sequence And Series(3)','Straight Lines(4)','Introduction To Three Dimensional Geometry(5)']
    for i in d:
        print(i.upper())
    print('#THE FORMULAS CAN BE ACCESSED THROUGH THE NUMBER AT END OF IT#')
    p=int(input('ENTER THE NUMBER OF THE CHAPTER YOU ARE SEARCHING FOR:'))
    if p==1:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from math_11 where unit='trigonometry'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS l=r*(o)")
                math11.tgf1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS radian measure = pi/180*degree measure")
                math11.tgf2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS degree measure = 180/pi*radian measure")
                math11.tgf3()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
    elif p==2:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from math_11 where unit='complex numbers and quadratic equations'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS z1+z2=(a+c)+i(b+d)")
                math11.cnqe1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS z1.z2=(ac-bd)-i(ad+bc)")
                math11.cnqe2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS z*=a^2/(a^2+b^2)+i(-b^2/(a^2+b^2))")
                math11.cnqe3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS z*=a-ib")
                math11.cnqe4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS X=-b+(4ac-b^2)^1/2*i/2a or -b-(4ac-b^2)^1/2*i/2a")
                math11.cnqe5()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
    elif p==3:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from math_11 where unit='sequences and series'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS a(n)=a+(n-1)d")
                math11.ss1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS s(n)=n/2(2a+(n-1)d)")
                math11.ss2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS a(n)=a.r^(n-1)")
                math11.ss3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS (ab)^1/2")
                math11.ss4()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
    elif p==4:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from math_11 where unit='Straight Lines'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS m=y2-y1/x2-x1=y1-y2/x1-x2")
                math11.st1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS tan(o)=m1+m2/(1+m1.m2)")
                math11.st2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS x/a+y/b=1")
                math11.st3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS d=mod((C1-C2)/(A^2+B^2)^1/2)")
                math11.st4()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
    elif p==5:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from math_11 where unit='Introduction To 3 Dimensional Geometry'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS  PQ=((x2-x1)^2+(y2-y1)^2+(z2-z1)^2)^1/2")
                math11.dg1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS  [(mx2+nx1)/m+n , (my2+my1)/m+n , (mz1-mz2)/m+n]")
                math11.dg2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS  [(x1+x2)/2 , (y1+y2)/2, (z1+z2)/2]")
                math11.dg3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS  [(x1+x2+x3/3),(y1+y2+y3/3),(z1+z2+z3/3)]")
                math11.dg4()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
def phy_11():
    d=['VECTORS(1)','KINEMATICS(2)','WORK, ENERGY AND POWER(3)','GRAVITATION(4)','REFLECTION OF LIGHT(5)','HEAT AND TEMPERATURE(6)','SPECIFIC HEAT(7)']
    print('THE AVAILABLE CHAPTERS ARE:')
    for i in d:
        print(i)
    print('#THE FORMULAS CAN BE ACCESSED THROUGH THE NUMBER AT END OF IT#')
    p=int(input('ENTER THE NUMBER OF THE CHAPTER YOU ARE SEARCHING FOR:'))
    if p==1:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_11 where unit='vectors'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS sqrt(a(x)^2+a(y)^2+a(z)^2)")
                phy11.vc1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS a.b=a*b*cos(o)")
                phy11.vc2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS axb=a*b*sin(o)")
                phy11.vc3()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
        
    elif p==2:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_11 where unit='kinematics'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS v(av)=[r(final)-r(initial)]/[t(final)-t(initial)]")
                phy11.k1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS a(av)=[v(final)-v(initial)]/[t(final)-t(initial)]")
                phy11.k2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS v=u+at")
                phy11.k3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS v^2-u^2=2*a*s")
                phy11.k4()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
    elif p==3:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_11 where unit='work, energy, power'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS W=F*S*cos(o)")
                phy11.wep1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS K=1/2*m*v^2")
                phy11.wep2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS P=m*g*h")
                phy11.wep3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS W=del K(K(final)-K(initial))")
                phy11.wep4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS E=U+K")
                phy11.wep5()
            elif s==6:
                print("THE CHOOSEN FORMULA IS P(av)=del W/del t")
                phy11.wep6()
            
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
    elif p==4:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_11 where unit='gravitation'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS F=G*m1*m2/r^2")
                phy11.g1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS U=G*M*m/r")
                phy11.g2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS g=G*M/r")
                phy11.g3()
            
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
    elif p==5:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_11 where unit='reflection of light'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS f=R/2")
                phy11.re1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS 1/v-1/u=1/f")
                phy11.re2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS m=-v/u")
                phy11.re3()
            
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
    elif p==6:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_11 where unit='heat and temperature'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS pV=nRT")
                phy11.ht1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS F/A=Y*(del l/l)")
                phy11.ht2()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
    elif p==7:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from phy_11 where unit='specific heat'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,":",e,"(",r,")")
            r+=1
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS s=Q/m*del T")
                phy11.sh1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS L=Q/m")
                phy11.sh2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS C(p)-C(r)=R")
                phy11.sh3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS U=f/2*R*T")
                phy11.sh4()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
        else:
            print("%%%CALCULATION OVER%%%")
    
        


    
    
    
                
        
   





















    
