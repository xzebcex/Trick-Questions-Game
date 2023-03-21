import random
import sys

# QUESTIONS is a list of dictionaries, each dictionary represents a
# trick question and its answer. The dictionary has the keys 'question'
# (which holds the text of the question), 'answer' (which holds the text
# of the answer), and 'accept' (which holds a list of strings that, if
# the player's answer contains any of, they've answered correctly).
# (!) Try coming up with your own trick questions to add here:

QUESTIONS = [{'Question': "What is the capital of Australia?",
              'Answer': "The capital of Australia is Canberra.",
              'Accept': ["canberra"]},
             {'Question': "Who is the founder of Microsoft?",
              'Answer': "The founder of Microsoft is Bill Gates.",
              'Accept': ["Bill Gates"]},
             {'Question': "What is the highest mountain in the world?",
              'Answer': "The highest mountain in the world is Mount Everest.",
              'Accept': "Mount Everest"},
             {'Question': "How many planets are in our solar system?",
              'Answer': "There are eight planets in our solar system.",
              'Accept': ["eight", "8", "eight planets",]},
             {'Question': "What is the smallest country in the world?",
             'Answer': "The smallest country in the world is Vatican City.",
              'Accept': ["vatican city"]},
             {'Question': "Who painted the Mona Lisa?",
              'Answer': "The Mona Lisa was painted by Leonardo da Vinci.",
              'Accept': ['Leonardo da Vinci', "leonardo da vinci"]},
             {'Question': "What is the largest organ in the human body?",
              'Answer': "The largest organ in the human body is the skin.",
              'Accept': ["skin", "Skin"]},
             {'Question': "How many time zones are there in the world?",
              'Answer': "There are 24 time zones in the world.",
              'Accept': ["24", "twenty-four"]},
             {'Question': "What is the chemical symbol for gold?",
              'Answer': "The chemical symbol for gold is Au."},
             {'Question': "What is the only continent that lies in all four hemispheres?",
              'Answer': "The continent that lies in all four hemispheres is Africa."}]


CORRECT_TEXT = ['Correct!', 'That is right.', "You're right.",
                'You got it.', 'Righto!']
INCORRECT_TEXT = ['Incorrect!', "Nope, that isn't it.", 'Nope.',
                  'Not quite.', 'You missed it.']

print('''
Can you figure out the answers to these trick questions?
(Enter QUIT to quit at any time.)
''')

input('Press Enter to begin...')

random.shuffle(QUESTIONS)
score = 0

for question_number, qa in enumerate(QUESTIONS):  # Main program loop.
    print('\n' * 40)  # "Clear" the screen.
    print('Question:', question_number + 1)
    print('Score:', score, '/', len(QUESTIONS))
    print('QUESTION:', qa['Question'])
    response = input(' ANSWER: ').lower()

    if response == 'quit':
        print('Thanks for playing!')
        sys.exit()

    correct = False
    for acceptance_word in qa['Accept']:
        if acceptance_word in response:
            correct = True

    if correct:
        text = random.choice(CORRECT_TEXT)
        print(text, qa['Answer'])
        score += 1

    else:
        text = random.choice(INCORRECT_TEXT)
        print(text, 'The answer is:', qa['Answer'])
        response = input('Press Enter for the next question...').lower()

    if response == 'quit':
        print('Thanks for playing!')
        sys.exit()

print("That's all the questions. Thanks for playing!")
