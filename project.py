#Final Project for CS50
import random

# Define a class for choosing a number and handle exceptions
class Number:
    def __init__(self, number):
        self.number = number


    def __str__(self):
        return f"You chose {self.number}"
    
    @classmethod
    def get(cls):
        while True:
            try:
                number = int(input("Choose a number between 1 and 10: "))
                if number in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
                    return cls(number)
                else:
                    print("\nPICK A NUMBER BETWEEN 1 AND 10 TO START THE TRICK")
            except ValueError:
                print(f"\nPICK A NUMBER BETWEEN 1 AND 10 TO START THE TRICK")
        

def main():
    #Ask the user for what magic trick they want 
    choice = get_trick()
    
    # Run the trick function according to the choice
    if choice == 1:
        threeTrick()

    elif choice == 2:
        divideTrick()

    else:
        luckyNumber()

#End-with-3 trick implementation
def threeTrick():
    print(f"\nIn this trick, whatever number you type between 1 and 10 would result in the number 3.")

    """Set a number to play with by initiating an object of the class Number"""
    number = Number.get()
    print(f"\n{number}\n")
    number = input("Multiply your number by 2 and type your answer: ")
    number = input("\nMultiply your result by 5 and type your answer: ")
    number = input("\nWe are getting close! Divide your result by the number you originally chose and type the answer: ")
    number = input("\nSubtract 7 from the current result. Press enter!")
    
    '''Beat the drumbs for excitmente!'''
    for i in range(10):
        print("🥁")
    print(f"🥁Your result is 3!🥁")

#Divide by half trick implementation
def divideTrick():
    print(f"\nIn this trick, whatever number you choose between 1 and 10 would result in half a number Mr. Computer will choose.")

    '''Set a number to play with by initiating an object of the class Number '''
    number = Number.get()
    print(f"\n{number}\n")

    number = int(input("Multiply your number by 2 and type your answer: "))
    
    '''Choose a random even number to add to number'''
    randomNumber = random.randrange(2, 11, 2)

    number = int(input(f"\nMr. Computer choses the number {randomNumber}. Add it to your lattest number and type the answer: "))

    number = int(input(f"\nDivide your number by 2. Type your answer: "))

    input(f"\nFinally, subtract your original number and press enter.")
    
    '''Beat the drumbs for excitmente!'''
    for i in range(10):
        print("🥁")

    print(f"🥁Your result is {(round(randomNumber/2))}!🥁")
                  

    
#Lucky Number 13 implementation
def luckyNumber():
    print(f"\nIn this magic trick, whatever number you choose between 1 and 10 would result in the LUCKY number 13!")

    '''Set a number to play with by initiating an object of the class Number '''
    number = Number.get()
    print(f"\n{number}\n")

    number = int(input(f"Multiply your number by 9. Type your answer: "))

    number = int(input(f"\nAdd the first and second digit of your new number (e.g. 13 -> 1 + 3; 9 -> 9 + 0). Type your answer: "))

    input(f"Now add 4 to your lattest number and press enter. Drums rolling!")

    number +=4 
    
    for i in range(10):
        print("🥁")

    print(f"You got the lucky number {number}🥁")

# Get the type of magic trick from the user
def get_trick():
    ''' Get an input and evaluate if the input is an int'''
    while True:
        try:
            type = int(input("What type of magic trick you want to play?\n 1 - Three every time!\n 2 - Half the number\n 3 - Lucky 13\n Type the number: "))
            if type in [1, 2, 3]:
                return type
            else:
                print(f"\nChoose a number between 1 and 3\n")
                
        except ValueError:
            print(f"\nYou must choose an option between 1 and 3\n")
           

if __name__ == "__main__":
    main()

