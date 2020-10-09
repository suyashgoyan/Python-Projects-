low = 1 
high = 1000
print("Please think of a number between {} and {}".format(low,high))
input("Press ENTER to start ")

guesses = 1

while low != high:                                     # We used True because the computer don't the exact answer
    guess = low + (high - low) // 2                 #Binary Search Formula

    high_low = input("My guess is {}. Should I guess higher or lower?"
                    " Press 'h' for higher and 'l' for lower or if my guess is correct press 'c' "
                     .format(guess)).casefold()                         #.casefold() is used when we don't want the program to be case sensitive

    if high_low == "h":
        low = guess + 1                        # Guess higher. The low end of the range becomes 1 greater than the guess 
    elif high_low == "l":    
         high = guess -1                    # Guess lower. The higher end of the range becomes 1 less than the guess
    elif high_low == "c":
        print("I got it in {} guesses.".format(guesses))
        break
    else:
        print("Please enter h,l or c")

    guesses += 1
else:
    print("You thought of the number {}".format(low))
    print("I guessed the number in {} guesses.".format(guesses))
