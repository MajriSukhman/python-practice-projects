'''
🔥 Advanced Text Engine Challenge

Write a program that:

1️⃣ Sentence Intelligence

Detects sentences (. ! ?)

Capitalizes first letter of each sentence

Ensures standalone “i” becomes “I”

2️⃣ Word Classification

For every word:

If word length is prime → reverse it

If word length is even but not prime → alternate case (hElLo)

If word length is odd and not prime → convert to snake_case style (if multi-word chunk)

3️⃣ Position Logic

Every 3rd word → convert to uppercase

Every 5th word → convert to lowercase

If both → wrap it in brackets [word]

(Yes. Order matters. Good luck.)

4️⃣ Structural Awareness

Preserve punctuation exactly where it was

Remove extra spaces

Keep emojis untouched

Do not break numbers

5️⃣ Bonus Insanity Mode

Add a feature:

If a word appears more than once, replace its later appearances with a counter
Example:
"hello world hello hello"
→ "hello world hello(2) hello(3)"

6️⃣ Constraints

No using built-in .title() or shortcut formatting tricks

Must work in one function

Should handle edge cases like:

"HELLO...why??"

"i i i i"

" multiple spaces "
'''
def SentenceIntelligence(rawText):
    separators = ['?', '!', '.']

    def splitAndCapitalize(separator, rawText):
        sentences = rawText.split(separator)
        stripped_sentences = [sentence.strip() for sentence in sentences]
        capitalized_sentences = [sentence2.capitalize() for sentence2 in stripped_sentences]
        finalOutput = f'{separator} '.join(capitalized_sentences)
        return finalOutput

    def handleStandalone(rawText):
        words = rawText.split(' ')
        while 'i' in words:
            targetIndex = words.index('i')
            words[targetIndex] = 'I'
        finalOutput = ' '.join(words)
        return finalOutput
    
    format1 = splitAndCapitalize(separators[0], rawText)
    
#TO BE CONTINUED SENTENCEINTELLIGENCE

def isPrime(num):
    if num <= 1:
        return False
    for i in range(2, round(num**1/2)):
        return False if num % 2 == 0 else True

print(isPrime(35))
def WordClassification(rawText):
    words = rawText.split(' ')
    for word in words:
        pass