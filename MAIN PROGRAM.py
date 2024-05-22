import class_10th
import class_11th
import class_12th
import mysql.connector as mys
mycon=mys.connect(host='localhost',username='root',passwd='selva',database='student')
mycursor=mycon.cursor()
print("\t\t\t############################################\t\t\t")
print("\t\t\t\tFORMULA BOOK AND CALCULATOR\t\t\t\t")
print("\t\t\t############################################\t\t\t")
print("\n")
print("\t\t\t\t\tWELCOME\t\t\t\t")
print("\t\t\t\t#GENERAL INSTRUCTIONS#\t\t\t\t")
print("=>ALL THE DETAILS YOU SEARCH FOR SHOULD BE IN CAPITAL LETTERS EXCEPT NUMBERS AND THE SPECIAL CHARACTERS")
print("=>IF NOT YOU WILL FACE ERRORS AND POOR EXPERIENCE")
print("\n")
res=True
while res==True:
    N=input("ENTER YOUR CLASS [10,11,12]:")
    if N=='10':
        print("#YOU HAVE CHOOSEN THE CLASS 10")
        print("THE AVAILABLE SUBJECTS ARE,")
        print("1.PHYSICS")
        print("2.CHEMISTRY")
        print("3.MATHS")
        print("\n")
        S=input("ENTER THE SUBJECT FOR WHAT YOU SEARCH:")
        if S.upper()=="PHYSICS":
            class_10th.phy_main_10()        
        elif S.upper()=='MATHS':
            class_10th.mat_main_10()
        elif S.upper()=="CHEMISTRY":
            print("THERE NO MATHEMATICAL FORMULAS TO CALCULATE OR TO SHOW")
        
    elif N=='11':
        print("#YOU HAVE CHOOSEN THE CLASS 11")
        print("THE AVAILABLE SUBJECTS ARE,")
        print("1.PHYSICS")
        print("2.CHEMISTRY")
        print("3.MATHS")
        print("\n")
        S=input("ENTER THE SUBJECT FOR WHAT YOU SEARCH:")
        if S.lower()=='chemistry':
            class_11th.chem_11()
        elif S.lower()=='maths':
            class_11th.math_11()
        elif S.lower()=='physics':
            class_11th.phy_11()
        

    elif N=='12':
        print("#YOU HAVE CHOOSEN THE CLASS 12")
        print("THE AVAILABLE SUBJECTS ARE,")
        print("1.PHYSICS")
        print("2.CHEMISTRY")
        print("3.MATHS")
        print("\n")
        S=input("ENTER THE SUBJECT FOR WHAT YOU SEARCH:")
        if S.lower()=='chemistry':
            class_12th.chem_12()
        elif S.lower()=='maths':
           class_12th.math_12()
        elif S.lower()=='physics':
           class_12th.phy_12()
    res=input("ENTER 'H' TO GO TO HOME OR 'E' TO END THE PROGRAM ~")
    print("\n")
    if res.upper()=='H':
        res=True
    else:
        res=False
else:
    print("\n")
    print("PROGRAM OVER THANK YOU FOR VISITING MY PROGRAM\n")
    print("SORRY! IF YOU HAVE FACED ANY INCONVIENECE IN OUR PORGRAM, WE WILL TRY TO SORT IT OUT IN THE UPCOMING UPDATES OF OUR PROGRAM.;)")

    
    
      
    
