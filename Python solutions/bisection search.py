print("Please think of a number between 0 to 100")

low=0
high=100
medium=(low+high)//2
state= True

while state :
    print("Is your Secret Num " +  str(medium))
    guess = input("Enter 'h' to indicate the guess is too high, Enter 'l' to indicate the guess is too low, Enter 'c' to indicate the guess is correct. ")
    if guess == 'c':
        print("Game Over. Your Secret Num was:"+ str(medium))
        state = False
    elif guess == 'h':
        high = medium
        medium = (high+low)//2
    elif guess == 'l':
        low = medium
        medium = (high+low)//2
    else:
        print("Sorry,i didn't understand your input.")
