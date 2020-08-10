print("Give me two numbers and I will add them.")
print("Enter 'q' to quit.")

while True:
    first_num = input("\nFirst number: ")
    if first_num.lower() == "q":
        break
    second_num = input("Second number: ")
    if second_num.lower() == "q":
        break
    try:
        answer = int(first_num) + int(second_num)
    except ValueError:
        print("Foolish mortal, I requested two numbers! You shall pay for this insolence...")
    else:
        print(answer)