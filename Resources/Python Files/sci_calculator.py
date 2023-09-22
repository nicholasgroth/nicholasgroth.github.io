import math

current_result = float(0)

values = []

#Dummy Variable
i = 0

#Calculator Menu
print("Current Result:", current_result)
print("""
Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average"""
)

while i == 0:

    user_input = int(input("Enter Menu Selection: "))

    #append used to add values to list that way an average can be taken
    if user_input <= 7 and user_input >= 0:
    
        if user_input == 0:
            print("""Thanks for using this calculator. Goodbye!""")
            break

        #Addition
        elif user_input == 1:
            first_operand = float(input("Enter first operand: "))
            second_operand = float(input("Enter second operand: "))
            current_result = first_operand + second_operand
            values.append(current_result)
            print("Current Result:", current_result)
            print("""
Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average"""
)
        
        #Subtraction
        elif user_input == 2:
            first_operand = float(input("Enter first operand: "))
            second_operand = float(input("Enter second operand: "))
            current_result = first_operand - second_operand
            values.append(current_result)
            print("Current Result:", current_result)
            print("""
Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average"""
)

        #Multiplication
        elif user_input == 3:
            first_operand = float(input("Enter first operand: "))
            second_operand = float(input("Enter second operand: "))
            current_result = first_operand * second_operand
            values.append(current_result)
            print("Current Result:", current_result)
            print("""
Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average"""
)

        #Division
        elif user_input == 4:
            first_operand = float(input("Enter first operand: "))
            second_operand = float(input("Enter second operand: "))
            current_result = first_operand / second_operand
            values.append(current_result)
            print("Current Result:", current_result)
            print("""
Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average"""
)

        #Exponents
        elif user_input == 5:
            first_operand = float(input("Enter first operand: "))
            second_operand = float(input("Enter second operand: "))
            current_result = first_operand ** second_operand
            values.append(current_result)
            print("Current Result:", current_result)
            print("""
Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average"""
)

        #Logarithms 
        elif user_input == 6:
            first_operand = float(input("Enter first operand: "))
            second_operand = float(input("Enter second operand: "))
            current_result = math.log(second_operand, first_operand)
            values.append(current_result)
            print("Current Result:", current_result)
            print("""
Calculator Menu
---------------
0. Exit Program
1. Addition
2. Subtraction
3. Multiplication
4. Division
5. Exponentiation
6. Logarithm
7. Display Average"""
)

    #Averaging Results
        elif user_input == 7:
            if len(values) == 0:
                print("Error: No calculations yet to average!")

            else:
                current_result = (sum(values) / len(values))
                print("Sum of calculations:", sum(values))
                print("Number of calculations:", len(values))
                print("Average of calculations:", round(current_result, 2))

    else:
        print("Error: Invalid selection!")
