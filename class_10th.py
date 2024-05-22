from tenth_class import physics
from tenth_class import maths
import mysql.connector as mys
mycon=mys.connect(host='localhost',username='root',passwd='selva',database='student')
mycursor=mycon.cursor()
def phy_main_10():
    d=['REFLECTION  AND REFRACTION OF LIGHT(1)','ELECTRICITY(2)']
    print('THE AVAILABLE CHAPTERS ARE:')
    for i in d:
        print(i)
    print('#THE FORMULAS CAN BE ACCESSED THROUGH THE NUMBER AT END OF IT#')
    p=int(input('ENTER THE NUMBER OF THE CHAPTER YOU ARE SEARCHING FOR:'))
    res=True
    while res==True:
        if p==1:
            mycursor.execute("select * from tenth_physics where unit='reflection'")
            rec=mycursor.fetchall()
            print('THE AVAILABLE CONCEPT ARE:')
            r=1
            for i,x,y in rec:
                print(i.upper(),"-",x,"(",r,")")
                r+=1
            a=int(input('ENTER THE NUMBER OF THE FORMULA YOU ARE SEARCHING FOR:'))
            if a==1:
                print('THE MIRROR FOMULA IS: 1/u+1/v=1/f')
                c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
                if c.lower()=='y':
                    physics.mirrorfor()
                else:
                    print('CALCULATION OVER')
                    res=False
            elif a==2:
                print('THE MAGNIFICATION(MIRROR) FORMULA IS: m=height of the image(h1)/height of the object(h2)')
                c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
                if c.lower()=='y':
                    physics.mag()
                else:
                    print('CALCULATION OVER')
                    res=False
            elif a==3:
                print('THE REFRACTIVE INDEX FORMULA IS: n=speed of light in medium2/speed of light in medium1')
                c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
                if c.lower()=='y':
                    physics.refindex()
                else:
                    print('CALCULATION OVER')
                    res=False
            elif a==4:
                print('THE ABSOLUTE REFRACTIVE INDEX FORMULA IS: n=speed of light in air/speed of light in medium')
                c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
                if c.lower()=='y':
                    physics.abrefindex()
                else:
                    print('CALCULATION OVER')
                    res=False
            elif a==5:
                print('THE LENS FOMULA IS: 1/u-1/v=1/f')
                c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
                if c.lower()=='y':
                    physics.lensfor()
                else:
                    print('CALCULATION OVER')
                    res=False
            elif a==6:
                print("THE MAGNIFICATION(LENS) FORMULA IS: m=height of the image(h')/height of the object(h)")
                c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
                if c.lower()=='y':
                    physics.lenmag()
                else:
                    print('CALCULATION OVER')
                    res=False
            elif a==7:
                print('THE POWER OF LENS FORMULA IS: P=1/f')
                c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
                if c.lower()=='y':
                    physics.powoflens()
                else:
                    print('CALCULATION OVER')
                    res=False
            res=False
        elif p==2:
            mycursor.execute("select * from tenth_physics where unit='human eye'")
            rec=mycursor.fetchall()
            print('THE AVAILABLE CONCEPT ARE:')
            r=1
            for i,x,y in rec:
                print(i.upper(),"-",x,"(",r,")")
                r+=1
            a=int(input('ENTER THE NUMBER OF THE FORMULA YOU ARE SEARCHING FOR:'))
            if a==1:
                print('THE HEAT PRODUCED IN THE ELECTRIC CIRCUIT IS: H=I^2RT')
                c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
                if c.lower()=='y':
                    physics.heat()
                else:
                    print('CALCULATION OVER')
                    res=False
            elif a==2:
                print('THE ELECTRIC RESISTANCE FORMULA IS: R=px(l/A)')
                print('here the "p" is electrical resistivity')
                c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
                if c.lower()=='y':
                    physics.resistance()
                else:
                    print('CALCULATION OVER')
                    res=False
            elif a==3:
                print('THE ELECTRIC POWER FORMULA IS: P=W/t')
                c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
                if c.lower()=='y':
                    physics.electricpow()
                else:
                    print('CALCULATION OVER')
                    res=False
            res=False
        else:
            print("enter within range")
            break
def mat_main_10():
    print('THE AVAILABLE CONCEPTS ARE:')
    d=['real numbers(1)','polynomials(2)','quadratic equation(3)','arithmetic progression(4)','coordinate geometry(5)','statistics(6)','circles(7)','mensuration(8)','probability(9)']
    for i in d:
        print(i)
    print('#THE FORMULAS CAN BE ACCESSED THROUGH THE NUMBER AT END OF IT#')
    print("HERE THE NOTATION MEANS:")
    print("^-means 'to the power'")
    print("*-means 'multiplication symbol'")
    print("NOTE:here the right hand side values are calculated")
    a=int(input('ENTER THE NUMBER OF THE CONCEPT YOU ARE SEARCHING FOR:'))
    if a==1:
        mycursor.execute("select * from tenth_maths where unit='real numbers'")
        print("THE AVAILABLE FORMULA IN THIS CHAPTER IS")
        rec=mycursor.fetchall()
        for i,e,y in rec:
            print(i.upper())
        c=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
        while c.lower()=='y':
            for i,e,y in rec:
                print("the formula is",e)
            maths.realnum()
            c=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
        else:
            print("CALCULATION OVER")
            
    elif a==2:
        print('THE FORMULAS IN THIS CONCEPTS ARE:')
        mycursor.execute("select * from tenth_maths where unit='polynomial'")
        rec=mycursor.fetchall()
        for i,e,w in rec:
            print(e)
        en=input('DO YOU WANT TO CLACULATE THE FORMULA(Y/N):')
        while en.lower()=='y':
            s=int(input("enter your choice:"))
            if s==1:
                print("THE CHOOSEN FORMULA IS (a + b)^2 = a^2 + b^2 + 2ab ")
                maths.linereqn1()
            elif s==2:
                print("THE CHOOSEN FORMULA IS (a – b)^2  = a^2 + b^2 – 2ab")
                maths.linereqn2()
            elif s==3:
                print("THE CHOOSEN FORMULA IS a^2 – b^2 = (a + b) (a – b)")
                maths.linereqn3()
            elif s==4:
                print("THE CHOOSEN FORMULA IS (a + b)^3  = a^3 + b^3 + 3ab")
                maths.linereqn4()
            elif s==5:
                print("THE CHOOSEN FORMULA IS a^3 + b^3 = (a + b) (a^2 – ab + b2)")
                maths.linereqn5()
            elif s==6:
                print("THE CHOOSEN FORMULA IS a^3 + b^3 + c^3 – 3abc  = (a + b + c)(a^2 + b^2 + c^2 – ab – bc – ca)")
                maths.linereqn6()
            en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')    
        else:
            print('%%%CALCULATION OVER%%%')
    elif a==3:
        print('THE CHOOSEN FORMULA IS')
        mycursor.execute("select * from tenth_maths where unit='quadratic equation'")
        rec=mycursor.fetchall()
        for i,e,w in rec:
            print(i,":",e)
        c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
        while c.lower()=='y':
            maths.quardratic()
            c=input('DO YOU WANT TO CALCULATE MORE(Y/N):')
        else:
            print('%%%CALCULATION OVER%%%')
    elif a==4:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from tenth_maths where unit='arithmetic progression'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,"(",r,")")
            r+=1
        s=int(input("ENTER YOUR CHOICE:"))
        if s==1:
            mycursor.execute("select * from tenth_maths where formula_name='nth Term of an Arithmetic Progression'")
            c=mycursor.fetchall()
            for i,e,w in c:
                print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.ap1()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        elif s==2:
            mycursor.execute("select * from tenth_maths where formula_name='Sum of First n Terms of an Arithmetic Progression'")
            c=mycursor.fetchall()
            for i,e,w in c:
                print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.ap2()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        else:
            print("ENTER WITHIN RANGE")
    elif a==5:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from tenth_maths where unit='Coordinate Gemetry'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,"(",r,")")
            r+=1
        s=int(input("ENTER YOUR CHOICE:"))
        if s==1:
            mycursor.execute("select * from tenth_maths where formula_name='Distance Formulae'")
            c=mycursor.fetchall()
            for i,e,w in c:
                print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.cg1()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        elif s==2:
            mycursor.execute("select * from tenth_maths where formula_name='Section Formula'")
            c=mycursor.fetchall()
            for i,e,w in c:
                print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.cg2()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        elif s==3:
            mycursor.execute("select * from tenth_maths where formula_name='mid point formula'")
            c=mycursor.fetchall()
            for i,e,w in c:
                print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.cg3()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        elif s==4:
            mycursor.execute("select * from tenth_maths where formula_name='area of triangle'")
            c=mycursor.fetchall()
            for i,e,w in c:
                    print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.cg4()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        else:
            print("ENTER WITHIN RANGE")
    elif a==6:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from tenth_maths where unit='statistics'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,"(",r,")")
            r+=1
        s=int(input("ENTER YOUR CHOICE:"))
        if s==1:
            mycursor.execute("select * from tenth_maths where formula_name='Median'")
            c=mycursor.fetchall()
            for i,e,w in c:
                print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.st1()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        elif s==2:
            mycursor.execute("select * from tenth_maths where formula_name='Mode'")
            c=mycursor.fetchall()
            for i,e,w in c:
                print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.st2()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        else:
            print("ENTER WITHIN RANGE")
                
    elif a==7:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        mycursor.execute("select * from tenth_maths where unit='circles'")
        rec=mycursor.fetchall()
        r=1
        for i,e,w in rec:
            print(i,"=",e,"(",r,")")
            r+=1
        s=int(input("ENTER YOUR CHOICE:"))
        if s==1:
            mycursor.execute("select * from tenth_maths where formula_name='area of circle'")
            c=mycursor.fetchall()
            for i,e,w in c:
                print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.cl1()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        elif s==2:
            mycursor.execute("select * from tenth_maths where formula_name='circumference of circle'")
            c=mycursor.fetchall()
            for i,e,w in c:
                print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.cl2()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        elif s==3:
            mycursor.execute("select * from tenth_maths where formula_name='area of the sector of angle(o)'")
            c=mycursor.fetchall()
            for i,e,w in c:
                print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.cl3()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        elif s==4:
            mycursor.execute("select * from tenth_maths where formula_name='length of an arc of a sector of angle(o)'")
            c=mycursor.fetchall()
            for i,e,w in c:
                print(e)
            en=input("DO YOU WANT TO CALCULATE THE FORMULA(Y/N):")
            while en.lower()=='y':
                maths.cl4()
                en=input("DO YOU WANT TO CALCULATE MORE(Y/N):")
            else:
                print("%%%CALCULATION OVER%%%")
        else:
            print("ENTER WITHIN RANGE")
               
    elif a==8:
        print("THE AVAILABLE FORMULAS IN THIS CHAPTER IS")
        f=['volume formulas(1)','curved surface area formulas(2)','total surface area formulas(3)']
        for i in f:
            print(i)
        e=int(input("enter your choice:"))
        if e==1:
            mycursor.execute("select * from tenth_maths where formula_name like 'volume%'")
            c=mycursor.fetchall()
            r=1
            for i,e,w in c:
                print(i,":",e,"(",r,")")
                r+=1
            en=input('DO YOU WANT TO CLACULATE THE FORMULAS(Y/N):')
            while en.lower()=='y':
                s=int(input("enter your choice:"))
                if s==1:
                    print("THE CHOOSEN FORMULA IS l*b*h")
                    maths.volume1()
                elif s==2:
                    print("THE CHOOSEN FORMULA IS a^3")
                    maths.volume2()
                elif s==3:
                    print("THE CHOOSEN FORMULA IS pi*r^2*h")
                    maths.volume3()
                elif s==4:
                    print("THE CHOOSEN FORMULA IS 1/3*pi*r^2*h")
                    maths.volume4()
                elif s==5:
                    print("THE CHOOSEN FORMULA IS 4/3*pi*r^3")
                    maths.volume5()
                elif s==6:
                    print("THE CHOOSEN FORMULA IS 2/3*pi*r^2")
                    maths.volume6()
                en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
            else:
                print('%%%CALCULATION OVER%%%')
        elif e==2:
            mycursor.execute("select * from tenth_maths where formula_name like 'curved%'")
            c=mycursor.fetchall()
            r=1
            for i,e,w in c:
                print(i,":",e,"(",r,")")
                r+=1
            en=input('DO YOU WANT TO CLACULATE THE FORMULAS(Y/N):')
            while en.lower()=='y':
                s=int(input("enter your choice:"))
                if s==1:
                    print("THE CHOOSEN FORMULA IS 2h(l+b)")
                    maths.surfarea1()
                elif s==2:
                    print("THE CHOOSEN FORMULA IS 4a^2")
                    maths.surfarea2()
                elif s==3:
                    print("THE CHOOSEN FORMULA IS 2*pi*r*h")
                    maths.surfarea3()
                elif s==4:
                    print("THE CHOOSEN FORMULA IS pi*r*l")
                    maths.surfarea4()
                elif s==5:
                    print("THE CHOOSEN FORMULA IS 4*pi*r^2")
                    maths.surfarea5()
                elif s==6:
                    print("THE CHOOSEN FORMULA IS 2*pi*r^2")
                    maths.surfarea6()
                en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
            else:
                print('%%%CALCULATION OVER%%%')
        elif e==3:
            mycursor.execute("select * from tenth_maths where formula_name like 'surface%'")
            c=mycursor.fetchall()
            r=1
            for i,e,w in c:
                print(i,":",e,"(",r,")")
                r+=1
            en=input('DO YOU WANT TO CLACULATE THE FORMULAS(Y/N):')
            while en.lower()=='y':
                s=int(input("enter your choice:"))
                if s==1:
                    print("THE CHOOSEN FORMULA IS 2(lh+bh+lb)")
                    maths.area1()
                elif s==2:
                    print("THE CHOOSEN FORMULA IS 6a^2")
                    maths.area2()
                elif s==3:
                    print("THE CHOOSEN FORMULA IS 2*pi*r(h+r)")
                    maths.area3()
                elif s==4:
                    print("THE CHOOSEN FORMULA IS pi*r(l+r")
                    maths.area4()
                elif s==5:
                    print("THE CHOOSEN FORMULA IS 4*pi*r^2")
                    maths.area5()
                elif s==6:
                    print("THE CHOOSEN FORMULA IS 3*pi*r^2")
                    maths.area6()
                en=input('DO YOU WANT TO CLACULATE MORE(Y/N):')
            else:
                print('%%%CALCULATION OVER%%%')
                
    elif a==9:
        mycursor.execute("select * from tenth_maths where unit='probability'")
        rec=mycursor.fetchall()
        for i,e,w in rec:
            print(i,":",e)
        c=input('DO YOU WANT TO CALCULATE THE VALUES(Y/N):')
        while c.lower()=='y':
            maths.probability()
            c=input('DO YOU WANT TO CALCULATE MORE(Y/N):')
                
        else:
            print('%%%CALCULATION OVER%%%')

