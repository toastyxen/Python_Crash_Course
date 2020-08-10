print("Give me two numbers and I will divide them.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num.lower() == "q":
        break
    second_num = input("Second number: ")
    if second_num.lower() == "q":
        break
    try:
        answer = int(first_num) / int(second_num)
    except ZeroDivisionError:
        print("Foolish mortal, you cannot divide by zero!")
    else:
        print(answer)