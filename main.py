import random
import time as t

def intro():
    name = input('Welcome to Double Dare, our first contender is: ' ) # Gets the name of the contester
    print(f'You will be asked {len(questions)} questions, answer them as fast as possible.') # Gives instuctions
    t.sleep(4)
    print('Are you ready...') # Starts the countdown
    t.sleep(1)
    print('3...')
    t.sleep(1)
    print('2...')
    t.sleep(1)
    print('1...')
    t.sleep(1)
    print('Go!')
    start_time = t.time() # Starts the stopwatch
    return name, start_time #returns the name and start time



questions = {'What geometric shape is generally used for stop signs?': ['Square', 'Hexagon', 'Octagon', 'Pentagon'],     #the questions with the answer choices as values
    'What is "cynophobia"?': ['Fear of dogs', 'Fear of mice', 'Fear of buttons', 'Fear of cinema'],
    "What's the fastest land animal?": ['Tiger', 'Leopard', 'Cheetah'],
    'How many colors are there in the rainbow?': ['5', '7', '8', '11'],
    'Which country borders 14 nations and crosses 8 time zones?': ['China', 'USA', 'Russia', 'India'],
    'The unicorn is the national animal of which country?': ['Ireland', 'Scotland', 'Belgium', 'Sudan'],
    'What is the hottest planet in the solar system?': ['Uranus', 'Mars', 'Mercury', 'Venus'],
    'What is the nearest planet to the sun?': ['Earth', 'Venus', 'Mercury', 'Pluto'],
    'From which country does Gouda cheese originate?': ['Italy', 'France', 'Netherlands', 'India'],
    'Which email service is owned by Microsoft?': ['Gmail', 'Outlook', 'Hotmail', 'GMX'],
    'Which animal can be seen on the Porsche logo?': ['Dog', 'Horse', 'Jaguar', 'Leopard'],
    'Which country produces the most coffee in the world?': ['Brazil', 'Uruguay', 'China', 'Switzerland'],
    'Which continent is the largest?': ['Europe', 'Asia', 'Africa', 'North America'],
    'What is the capital of Australia?': ['Sydney','Canberra','Melbourne','Perth'],
    'What is the largest mammal on Earth?': ['Blue Whale','Elephant','Giraffe','Hippopotamus'],
    'What is the most popular sport in the world?': ['Basketball','Cricket','Football','Tennis']}

answers = ['Octagon',     #The answers to the questions
    'Fear of dogs',
    'Cheetah',
    '7',
    'Russia',
    'Scotland',
    'Venus',
    'Mercury',
    'Netherlands',
    'Hotmail',
    'Horse',
    'Brazil',
    'Asia',
    'Canberra',
    'Blue Whale',
    'Football']


score = 0    # Starting correct answers counter

name, start_time = intro()

for i, question in enumerate(questions):   # Uses enumerate to go through each answer and remember at what spot it was
    print(question)    # Prints the question

    choices = questions[question]    # gets answer choices for the question
    random.shuffle(choices)    # Randomize the answer choices

    for j, choice in enumerate(choices):     # Prints the choices one by one remembering what value it had
        print(j+1, choice)  

    while True:
        try:
            ans = int(input('Enter the number of your answer (1-4): ')) -1       # asks for the users input as a integer; the -1 is becuase the user input starts at 1 but the enumeration at 0
            if ans >= 0 and ans <= 3:     # makes sure that the number is between 1-4
                break
            else:
                print('Please enter a number between 1-4')
        except ValueError:       # if users input is not an interger it asks again
            print('Please enter a number between 1-4')
           
    if choices[ans] == answers[i]:     # Checks if the users answer is correct
        score += 1      # If correct, increase the score by one
        print('Correct!')
    else:
        print(f'Incorrect, the correct answer is {answers[i]}')      # If not correct, print the correct answer

end_time = t.time() # Stops the stopwatch
elapsed_time = int(end_time) - int(start_time) # Gets the time it took to answer the questions     
print(f'{name}, it took you {elapsed_time} seconds to answer {score}/{len(questions)} correctly.')      # Print the final time and score using the f' function