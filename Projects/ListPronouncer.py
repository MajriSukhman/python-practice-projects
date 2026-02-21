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
        self.settings = {
            'rate': 200,
            'volume': 1,
            'voice': 0
        }
    
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
        engine = pyttsx3.init()
        engine.setProperty('rate',self.settings['rate'])
        engine.setProperty('volume',self.settings['volume'])
        voices = engine.getProperty('voices')
        engine.setProperty('voice',voices[self.settings['voice']].id)
        engine.say(sentence)
        engine.runAndWait()
        # self.engine.stop()
    
    @property
    def rate(self):
        return self.settings['rate']
    
    @property
    def volume(self):
        return self.settings['volume']
    
    @property
    def voice(self):
        return self.settings['voice']
    
    
    @rate.setter
    def rate(self, targetValue):
        self.settings['rate'] = targetValue

    @volume.setter
    def volume(self, targetValue):
        self.settings['volume'] = targetValue

    @voice.setter
    def voice(self, targetValue):
        self.settings['voice'] = targetValue

class CLI:
    def __init__(self):
        self.engine = PronounceList()
        self.reverse = False
        self.randomize = False
        self.commands = {
            '1': self.speak,
            '2': self.changeRate,
            '3': self.changeVolume,
            '4': self.toggleReverse,
            '5': self.toggleRandomize,
            '6': self.changeVoice,
            '7': self.quit
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
        newRate = int(input('Enter new rate (default: 200): '))
        oldRate = self.engine.settings['rate']
        self.engine.settings['rate'] = newRate
        print(f'Changed rate: {oldRate} -> {newRate}')
    
    def changeVolume(self):
        newVol = float(input('Enter new volume (default: 1.0): '))
        oldVol = self.engine.settings['volume']
        self.engine.settings['volume'] = newVol
        print(f'Changed volume: {oldVol} -> {newVol}')
    
    def toggleReverse(self):
        self.reverse = not self.reverse
        print(f'Reverse: {self.reverse}')
    
    def toggleRandomize(self):
        self.randomize = not self.randomize
        print(f'Randomize: {self.randomize}')
    
    def changeVoice(self):
        newVoice = int(input("Enter Voice ID (Default: 0): "))
        oldVoice = self.engine.settings['voice']
        self.engine.settings['voice'] = newVoice
        print(f'Changed Voice from {oldVoice} -> {newVoice}')
    
    def quit(self):
        self.running = False
    
    def mainmenu(self):
        print('1. Speak\n2. Change Rate\n3. Change Volume\n4. Reverse\n5. Randomize\n6. Change Voice\n7. Quit')
    
    def invalidChoice(self):
        print('Invalid Choice')

# s = PronounceList()
# words = ['Harry', 'Bhai', 'Jatt']
# s.speak(words)
# input()
# s.speak(words)

if __name__ == '__main__':
    run = CLI()
    run.run()
