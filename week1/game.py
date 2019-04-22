import random

number = random.randint(0, 101)

while True:

    answer = input("Input a number: ")
    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Input a corrent number")

    user_answer = int(answer)

    if user_answer > number:
        print("Less")
    elif user_answer < number:
        print("Greater")
    else:
        print("Correct")
        break
