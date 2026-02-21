print('\nAccuracy Finder by Sukhman\nVery Basic Version\nHow To Use:- For Correct Answer - Press Enter\n             For Incorrect Answer - Press Space and then Enter\n             To Quit - Type "DONE" and then Enter')
correct, total = 0,0
while True:
    ans = input()
    if ans.lower() == 'done':
        break
    if ans =='':
        correct += 1
        print(f'{total +1}. Correct')
    else:
        print(f'{total +1}. Incorrect')
    total += 1
print(f"\nQuestions Attempted: {total}\tCorrect: {correct}\tIncorrect: {total-correct}\n\n{round((correct / total)*100, 2)} %") if total > 0 else print('No Attempts Made')
