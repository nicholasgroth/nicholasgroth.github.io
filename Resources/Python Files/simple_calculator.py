answer = 0

#User Operand Input
first_op = float(input("Enter first operand: "))
second_op = float(input("Enter second operand: "))

#Calculator Menu
print("Calculator Menu")
print("---------------")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

#User Operation Selection
user_select = int(input("Which operation do you want to perform? "))

if user_select == 1:
    answer = first_op + second_op

elif user_select == 2:
    answer = first_op - second_op

elif user_select == 3:
    answer = first_op * second_op

elif user_select == 4:
    answer = first_op / second_op

#Result printing
else:
    print("Error: Invalid selection! Terminating program.")

if user_select >= 1 and user_select <= 4:
    print("The result of the operation is", str(answer) + ".", "Goodbye!")