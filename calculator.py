# input
operation_type = input()  # addition, subtraction, multiplying, dividing
number_1 = float(input())
number_2 = float(input())

# logic
result = ""

if operation_type == "addition":
    result = number_1 + number_2
    print(result)

elif operation_type == "subtraction":
    result = number_1 - number_2
    print(result)

elif operation_type == "multiplying":
    result = number_1 * number_2
    print(result)

else:
    result = number_1 / number_2
    print(result)
