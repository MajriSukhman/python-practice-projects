import pyttsx3
import time
import random

class PronounceList:
    """
    A basic utility to pronounce the elements of a list with the help of pyttsx3 in python

    USAGE:

    #To Speak A List    
    words = ['Lorem', 'ipsum', 'dolor', 'sit', 'amet']
    tts = PronounceList()
    tts.speak(words)


    #To Change The Rate
    tts.rate = 100 (default is 200)
    
    #To Change The Volume
    tts.volume = 1.5 (defualt is 1.0) 

    #To Change The Voice
    tts.voice = 1 (default is 0) 

    #To Reverse The Output
    tts.speak(words, reverse = True)

    #To Randomize The Output
        tts.speak(words, randomize = True)

    

    """
    def __init__(self):
        self.engine = pyttsx3.init()
    
    def speak(self, target, reverse = False, randomize = False):
        if type(target) != list:
            raise ValueError(f"{target} is not a 'list'")
        if randomize:
            targetClone = target.copy()
            random.shuffle(targetClone)
            sentence = ' '.join(targetClone)
        elif reverse:
            sentence = ' '.join(target[::-1])
        else:
            sentence = ' '.join(target)
        self.engine = pyttsx3.init()
        self.engine.say(sentence)
        self.engine.runAndWait()
        # self.engine.stop()
    
    @property
    def rate(self):
        return self.engine.getProperty('rate')
    
    @property
    def volume(self):
        return self.engine.getProperty('volume')
    
    @property
    def voice(self):
        return self.engine.getProperty('voice')
    
    
    @rate.setter
    def rate(self, targetValue):
        self.engine.setProperty('rate', targetValue)

    @volume.setter
    def volume(self, targetValue):
        self.engine.setProperty('volume', targetValue)

    @voice.setter
    def voice(self, targetValue):
        try:
            targetValue = self.engine.getProperty('voices')[targetValue].id
        except IndexError:
            raise ValueError("Invalid Voice Index - (try 0 or 1)")
        self.engine.setProperty('voice', targetValue)

class CLI:
    def __init__(self):
        self.engine = PronounceList()
        self.reverse = False
        self.randomize = False
        self.commands = {
            '1': self.speak,
            '2': self.changeRate,
            '3': self.toggleReverse,
            '4': self.toggleRandomize,
            '5': self.changeVoice,
            '6': self.quit
        }
        self.running = True
    
    def run(self):
        while self.running:
            self.mainmenu()
            choice = input("Select an option: ").strip()
            action = self.commands.get(choice, self.invalidChoice)
            action()
    
    def speak(self):
        userInput = input('Enter the elements of list separated by comma: ')
        words = userInput.split(',')
        self.engine.speak(words, self.reverse, self.randomize)
    
    def changeRate(self):
        newRate = input('Enter new rate (default: 200): ')
        oldRate = self.engine.rate
        self.engine.rate = newRate
        print(f'Changed rate: {oldRate} -> {newRate}')
    
    def toggleReverse(self):
        self.engine.reverse = not self.engine.reverse
        print(f'Reverse: {self.engine.reverse}')
    
    def toggleRandomize(self):
        self.engine.randomize = not self.engine.randomize
        print(f'Randomize: {self.engine.randomize}')
    
    def changeVoice(self):
        newVoice = input("Enter Voice ID (Default: 0): ")
        self.engine.voice = newVoice
    
    def quit(self):
        self.running = False
    
    def mainmenu(self):
        print('1. Speak\n2. Change Rate\n3. Reverse\n4. Randomize\n5. Change Voice\n6. Quit')
    
    def invalidChoice(self):
        print('Invalid Choice')

# s = PronounceList()
# words = ['Harry', 'Bhai', 'Jatt']
# s.speak(words)

# if __name__ == '__main__':
#     run = CLI()
#     run.run()
