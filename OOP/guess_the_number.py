import random

class GetRandomNumber:
    def __init__(self):
        self.number = random.randint(0, 100)
        self.numberOfGuesses = 0
        self.guessed = False
        print(self.number)
    

    def acceptUserInput(self):
        userInput = int(input("Please enter a number between 0 to 100: "))
        self.numberOfGuesses += 1
        return userInput
    
    def informUser(self, userInput):
        if userInput < self.number:
            print('Higher Number Please')
        elif userInput == self.number:
            print(f'Guessed Correctly in {self.numberOfGuesses} Attempts') 
        else:
            print('Lower Number Please')

    
    def validateUserInput(self, userInput):
        self.guessed = True if userInput == self.number else False
        self.informUser(userInput)
    

class StartGame(GetRandomNumber):
    def __init__(self):
        super().__init__()
        while not self.guessed:
            self.validateUserInput(self.acceptUserInput())
 
StartGame()