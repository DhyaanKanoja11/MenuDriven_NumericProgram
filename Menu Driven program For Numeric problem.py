# Function to convert time into minutes and hours
def time_conversion():
    print("\nTIME CONVERSION TO MINUTES AND HOURS \n")
    time = int(input("Enter Time in Minutes: "))
    hours = time // 60
    minutes = time % 60
    print("Hours Are:", hours)
    print("Minutes Are:", minutes)

# Function to convert temperature from Celsius to Fahrenheit
def temperature_conversion():
    print("\nTEMPERATURE CONVERSION FROM CELSIUS TO FAHRENHEIT \n")
    celsius = float(input('Enter the temperature in celsius: '))
    fahrenheit = (celsius * 9/5) + 32
    print('The Equivalent Of', celsius, 'In Fahrenheit Is ', fahrenheit, '°F')

# Function to calculate average
def calculate_average():
    print("\nAVERAGE\n")
    num_observations = int(input("Enter No. OF Observations: "))
    observations = [int(input("Enter NUMBER: ")) for _ in range(num_observations)]
    average = sum(observations) / num_observations
    print("\nAverage Of The Observations Is:", average)

# Function to calculate square and square root of a number
def square_and_square_root():
    print("\nSQUARE AND SQUAREROOT OF A NUMBER\n")
    num = float(input("Enter A Number: "))
    square = num ** 2
    root = num ** 0.5
    print("Square Of the Number: ", square, "\nSquare Root Of The Number :", root)

# Function to calculate area and perimeter of a rectangle
def rectangle_operations():
    print("\nAREA OF RECTANGLE AND PERIMETER OF RECTANGLE\n")
    length1 = float(input("Enter Length Of 1st Side: "))
    length2 = float(input("Enter Length Of 2nd Side: "))
    height = float(input("Enter Height Of Rectangle: "))
    area_rectangle = (length1 * height) + (length2 * height)
    perimeter_rectangle = (length1 + length2) * 2
    print("Area Of Rectangle: ", area_rectangle, "\nPerimeter Of Rectangle: ", perimeter_rectangle)

# Function to calculate area and perimeter of a triangle
def triangle_operations():
    while True:
        print('\nNOTE:ENTER THE HEIGHT,LENGTH IN ONLY INTEGERAL FORMAT\n')
        print('\n > Enter 1 For Right angle Triangle\n> Enter 2 For Equilateral Triangle\n> Enter 3 For Isosceles Triangle')
        a = int(input('\nEnter The Code Of Your Choice:  '))

        if a == 1:
            print('Area and Perimeter of Right angle Triangle')
            d = int(input('Enter Base Length: '))
            b = int(input('Enter Height Length'))
            BR = ((0.5 * d * b) * 100) // 1
            B = BR / 100
            print('Area = ', B)
            c = round(((b**2) + (d**2))**0.5, 2)
            print('Perimeter = ', round((d + b + c), 2))
        elif a == 2:
            print('Area and Perimeter Of Equilateral Triangle')
            ez = int(input('Enter The Length Of Side: '))
            AR = (((3**0.5)/4) * (ez**2) * 100) // 1
            Ar = AR / 100
            print('Area =', Ar)
            print('Perimeter = ', (3 * ez))
        elif a == 3:
            print('Area and Perimeter of Isosceles Triangle')
            f = int(input('Enter Length of Base:'))
            g = int(input('Enter Length of Common Side: '))
            h = (((f / 2)**2) * (g**2))
            CR = (((1 / 2)(h)(g)) * 100) // 1
            C = CR / 100
            print('Area = ,', ((1 / 2)(h)(g)))
            print('Perimeter = ', f + g + h)
        else:
            print('Invalid Code Entered')

# Function to calculate area and perimeter of a square
def square_operations():
    print("\nAREA OF SQUARE AND PERIMETER OF SQUARE\n")
    side_square = int(input("Enter side length of square"))
    area_square = side_square**2
    perimeter_square = side_square * 4
    print("Area Of Square: ", area_square, '\nPerimeter Of Square:', perimeter_square)

# Function to calculate simple interest and amount payable
def calculate_simple_interest():
    print('\nSIMPLE INTEREST AND AMOUNT PAYABLE')
    principle = int(input("Enter The Principle Amount: "))
    interest = int(input("Rate Of Interest In %: "))
    time = int(input("Time Period For Simple Interest: "))
    simple_interest = principle * (interest / 100) * time
    amount_payable = principle + simple_interest
    print('\nSIMPLE INTEREST: ', simple_interest, "AMOUNT PAYABLE: ", amount_payable)

# Function to convert INR to Euros
def convert_inr_to_euros():
    print("\nCONVERSION FROM INR TO EUROS \n")
    amount_inr = float(input("Amount in Rupees:"))
    euros = round(amount_inr * 0.011, 2)
    print(amount_inr, "IN EUROS:", euros)

# Function to convert INR to USD
def convert_inr_to_usd():
    print("\nCONVERSION FROM INR TO USD \n")
    amount_inr1 = float(input("Amount in Rupees:"))
    usd = round(amount_inr1 * 0.012, 2)
    print(amount_inr1, "IN USD:", usd)

# Function to convert INR to Pounds
def convert_inr_to_pounds():
    print("\nCONVERSION FROM INR TO POUNDS \n")
    amount_inr2 = float(input("Amount in Rupees:"))
    pounds = round(amount_inr2 * 0.0096, 2)
    print(amount_inr2, "IN POUNDS:", pounds)

# Function to calculate factorial of a number
def calculate_factorial():
    print('FACTORIAL OF NUMBERS')
    num = int(input("ENTER THE NUMBER:"))
    factorial = 1
    if num == 0:
        print(1)
    else:
        for i in range(1, num + 1):
            factorial = factorial * i
        print(f"The Factorial Of {num} is {factorial}")

# Function to find even numbers between a particular range
def find_even_numbers():
    print("FINDING EVEN NUMBER BETWEEN A PARTICULAR RANGE")
    start_range = int(input('Enter First Number of the Range:  '))
    end_range = int(input('Enter Second Number of the Range:  '))
    print('The Even Numbers between', start_range, 'and', end_range, 'are:')
    for x in range(start_range, end_range + 1):
        if x % 2 == 0:
            print(x)

# Function to find odd numbers between a particular range
def find_odd_numbers():
    print("FINDING ODD NUMBER BETWEEN A PARTICULAR RANGE")
    start_range = int(input('Enter First Number of the Range:  '))
    end_range = int(input('Enter Second Number of the Range:  '))
    print('The ODD Numbers between', start_range, 'and', end_range, 'are:')
    for u in range(start_range, end_range + 1):
        if u % 2 != 0:
            print(u)
# Main Menu Function
def main_menu():
    while True:
        print("\n  ░▒░▒░▒░▒ NUMERIC OPERATIONS ░▒░▒░▒░▒  ")
        print("1.  Time Into Minutes And Hours")
        print("2.  Temperature Conversion From Celsius To Fahrenheit")
        print("3.  Average")
        print("4.  Square And Root Of A Number ")
        print("5.  Area Of Rectangle and Perimeter Of Rectangle")
        print("6.  Area Of Triangle And Perimeter Of Triangle")
        print("7.  Area Of Square And Perimeter Of Square")
        print("8.  Simple interest and Amount Payable")
        print("9.  Conversion Of INR to EUROS")
        print("10. Conversion Of INR to USD")
        print("11. Conversion Of INR to POUNDS")
        print("12. Factorial Of A Number")
        print("13. Find The Even Numbers Between A Particular Range")
        print("14. Find The Odd Numbers Between A Particular Range")
        print("15. EXIT")
        choice = int(input("Enter Your Choice (1-15): "))

        # Calling the appropriate function based on the user's choice
        if choice == 1:
            time_conversion()
        elif choice == 2:
            temperature_conversion()
        elif choice == 3:
            calculate_average()
        elif choice == 4:
            square_and_square_root()
        elif choice == 5:
            rectangle_operations()
        elif choice == 6:
            triangle_operations()
        elif choice == 7:
            square_operations()
        elif choice == 8:
            calculate_simple_interest()
        elif choice == 9:
            convert_inr_to_euros()
        elif choice == 10:
            convert_inr_to_usd()
        elif choice == 11:
            convert_inr_to_pounds()
        elif choice == 12:
            calculate_factorial()
        elif choice == 13:
            find_even_numbers()
        elif choice == 14:
            find_odd_numbers()
        elif choice == 15:
            print("THANK YOU")
            print("$$$ EXITING $$$")
            break
        else:
            print("******* Invalid Choice *******")
            print("Press Any Key To Continue......................")
            return_to_menu = input()


# Running the Main Menu
if __name__ == "__main__":
    main_menu()
