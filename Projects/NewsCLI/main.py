import requests
from ListPronouncer import PronounceList

API_KEY = 'YOUR_API_KEY_HERE' #Replace this with your API KEY from newsapi.org

class News:
    API = API_KEY
    url = "https://newsapi.org/v2/top-headlines"
    category = 'Technology'
    country = 'us'

    def fetch(self, returnList=False):
        params = {
        'country': self.country,
        'category': self.category,
        'apiKey': self.API}

        try:
            response = requests.get(self.url, params=params, timeout=5)
            response.raise_for_status()
        except requests.RequestException:
            return f"Some Error Occured"
        newsList = []

        data = response.json()
        for i, article in enumerate(data['articles']):
            newsList.append(f"{i+1}. {article['title']}")
        if not newsList:
            return 'No Articles Found'
        if not returnList:
            return '\n'.join(newsList)
        else:
            return newsList

class CLI:
    def __init__(self):
        self.newsEngine = News()
        self.actions = {
        '1': self.printNews,
        '2': self.speak,
        '3': self.changeCategory,
        '4': self.changeCountry,
        '5': self.quit
        }
        self.running = True

    def run(self):
        while self.running:
            self.mainmenu()
            choice = input("Select A Choice: ")
            action = self.actions.get(choice, self.invalid)
            action()

    def mainmenu(self):
        print('1. Print\n2. Speak\n3. Category\n4. Country\n5. Quit')

    def invalid(self):
        print('Invalid Option')
    
    def printNews(self):
        print(self.newsEngine.fetch())
        input('Press any key...')

    def speak(self, returnList = True):
        speaker = PronounceList()
        news = self.newsEngine.fetch(returnList=True)
        if isinstance(news, list):
            speaker.speak(news)
        else:
            print(news)
            speaker.speak([news])
        input("Press any key...")

    def changeCategory(self):
        userInput = input("Change category: ")
        oldCategory = self.newsEngine.category
        self.newsEngine.category = userInput
        print(f'Changed category from {oldCategory} -> {self.newsEngine.category}')

    def changeCountry(self):
        userInput = input('Change country: ')
        oldCountry = self.newsEngine.country
        self.newsEngine.country = userInput
        print(f'Changed country from {oldCountry} -> {self.newsEngine.country}')
    
    def quit(self):
        self.running = False

if __name__ == '__main__':
    cli = CLI()
    cli.run()