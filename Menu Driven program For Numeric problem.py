#Menu Driven program For Numeric problems

while True:
    print("\n   ░▒▓▆▅▃▂▁NUMERIC OPERATIONS▁▂▃▅▆▓▒░   ")
    print("1.  Time Into Minutes And Hours")
    print("2.  Temperature Conversion From Celsius To Fahrenheit")
    print("3.  Average")
    print("4.  Square And Root Of A Number ")
    print("5.  Area Of Triangle and Perimeter Of Triangle")
    print("6.  Area Of Rectangle And Perimeter Of Rectangle")
    print("7.  Area Of Square And Perimeter Of Square")
    print("8.  Simple interest and Amount Payable")
    print("9.  Conversion Of INR to EUROS")
    print("10. Conversion Of INR to USD")
    print("11. Conversion Of INR to POUNDS") 
    print("12. Factorial Of A Number")
    print("13. EXIT")
    c=int(input("Enter Your Choice(1-12): "))

#Making The Operations Work

#Operation -1 {Time Into Minutes And Hours}

    if c==1:
        print("\nTIME CONVERSION TO MINUTES AND HOURS \n")
        time=int(input("Enter Time in Minutes: "))
        hours=time//60
        minutes= time%60
        print("Hours Are;",hours)
        print("Minutes Are;",minutes)

#Operation -2 {Temperature Conversion From Celsius To Fahrenheit}
    elif c==2:
        print ("\nTEMPERATURE CONVERSION FROM CELSIUS TO FAHRENHEIT \n")
        celsius= float(input('Enter the temperature in celsius : '))
        fahrenheit = (celsius * 9/5)+32
        print ('The Equivalent Of', celsius, 'In Fahrenheit Is ',fahrenheit,'°F')

#Operation -3 {Average}
    elif c==3:
        print ("\nAVERAGE\n")
        r1=int(input("Enter No. OF Observations : "))
        lst=[]
        t=0
        for i in range(0,r1+1):
            obv=int(input("Enter NUMBER : "))
            lst.append(obv)
        for x in lst:
            t += i
        print("\nAverage Of The Observations Is:",t/r1) 

#Operation -4 {Square And Root OF A Number }
    elif c==4:
        print ("\nSQUARE AND SQUAREROOT OF A NUMBER\n")
        numb=float(input("Enter A Number:"))
        sq=numb**2
        root=numb**0.5
        print ("Square Of the Number: ",sq,"\nSquare Root Of The Number :",root)

#Operation -5 {Area of a triangle & perimeter of a triangle}

    elif c==5:
        print ("\nAREA OF A TRIANGLE & PERIMETER OF A TRIANGLE\n")
        base=float(input('\nEnterBase Length:'))
        height=float(input('Height:'))
        area=(base*height)/2
        perimeter=(base + height)*2
        print("Area Of Triangle: ",area,"\nPerimeter Of Triangle is: ",perimeter )

#Operation -6 {Area Of Rectangle And Perimeter Of Rectangle}

    elif c==6:
        print ("\nAREA OF RECTANGLE AND PERIMETER OF RECTANGLE\n")
        l1= float(input("Enter Length Of 1st Side: "))
        l2= float(input("Enter Length Of 2nd Side: "))
        h = float(input("Enter Height Of Rectangle: "))
        arearectangle =(l1*h)+(l2*h)
        perimeterrectangle= (l1+l2)*2
        print("Area Of Rectangle: ",arearectangle,"Perimeter Of Rectangle: ",perimeterrectangle)

#Operation -7 {Area Of Square And Perimeter Of Square}

    elif c==7:
        print ("\nAREA OF SQUARE AND PERIMETER OF SQUARE\n")
        sidesquare= int(input("Enter side length of square"))
        areasquare=sidesquare**2
        perimetersquare=sidesquare*4
        print("Area Of Square: ",areasquare,'\nPerimeter Of Square:',perimetersquare)

#Operation -8 {Simple interest and Amount Payable}

    elif c==8:
        print ('\nSIMPLE INTEREST AND AMOUNT PAYABLE')
        principle=int(input("Enter The Principle Amount: "))
        interest=int(input("Rate Of Interest In %: "))
        time=int(input("Time Period For Simple Interest: "))
        simpleinterest=principle*(interest/(100))*time
        amountpayable=principle+simpleinterest
        print('\nSIMPLE INTEREST: ',simpleinterest,"AMOUNT PAYABLE: ",amountpayable)

#Operation -9 {Conversion of INR to EUROS}

    elif c==9:
        print("\nCONVERSION FROM INR TO EUROS \n")
        amountinr=float(input("Amount in Rupees:"))
        euros=round(amountinr*0.011,2)
        print(amountinr,"IN EUROS:",euros)

#Operation -10 {Conversion of INR to USD}

    elif c==10:
        print("\nCONVERSION FROM INR TO USD \n")
        amountinr1=float(input("Amount in Rupees:"))
        USD=round(amountinr1*0.012,2)
        print(amountinr1,"IN USD:",USD)

#Operation -11 {Conversion of INR to USD}

    elif c==11:
        print("\nCONVERSION FROM INR TO POUNDS \n")
        amountinr2=float(input("Amount in Rupees:"))
        POUNDS=round(amountinr2*0.0096,2)
        print(amountinr2,"IN POUNDS:",POUNDS)

#Operation -12 {Factorial of a Number}
    elif c==12:
        print('FACTORIAL OF NUMBERS')
        num = int(input("ENTER THE NUMBER:"))
        factorial=1
        if num==0:
            print(1)
        else:
            for i in range(1,num+1):
                factorial=factorial * i
            print (f"The Factorial Of {num} is {factorial}")

#Operation -13 {EXIT}
    elif c==13:
        print("THANK YOU")
        print("EXITING")
        break;

#ELSE
    else:
        print("*******Invalid Choice*******")
        print("\n Press Any Key To Continue......................")
        returntomenu=input()

#END OF THE CODE