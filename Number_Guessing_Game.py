import random

answer = random.randint(1,10)
print(answer)
choose_number = print("Choose a number between 1 to 10")


while answer != choose_number:
    choose_number = int(input(" "))
    if answer == choose_number:
        print("Wow! You got it first time.")
        break

    else:
        if answer > choose_number:
            print(" Choose a higher number")
        else:
            print("Choose a lower number")

        choose_number = int(input("Enter any number: "))

    if answer == choose_number:
        print("Well done ! You have guessed correctly.")
        break
    else:
        print("Sorry you lose.")
        break
            
