import sys

teach_points = 50
pop_points = 50
happy_points = 50

questions = [
    {
        'prompt': 'whaddup?',
        'options': [
            {
                'description': 'hello',
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': 'nerd',
            },
            {
                'description': 'heyyyy',
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': 'nice',
            },
            {
                'description': 'loser',
                'reward': {'teach': 0, 'pop': 0, 'happy': 1},
                'response': 'oy',
            },
        ],
    },
    {
        'prompt': 'whaddup?',
        'options': [
            {
                'description': 'hello',
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': 'nerd',
            },
            {
                'description': 'heyyyy',
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': 'nice',
            },
            {
                'description': 'loser',
                'reward': {'teach': 0, 'pop': 0, 'happy': 1},
                'response': 'oy',
            },
        ],
    },
    {
        'prompt': 'whaddup?',
        'options': [
            {
                'description': 'hello',
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': 'nerd',
            },
            {
                'description': 'heyyyy',
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': 'nice',
            },
            {
                'description': 'loser',
                'reward': {'teach': 0, 'pop': 0, 'happy': 1},
                'response': 'oy',
            },
        ],
    },
]


def ask(question):
    global teach_points, pop_points, happy_points
    print(question['prompt'])
    for ii in range(len(question['options'])):
        option = question['options'][ii]
        print('[' + str(int(ii) + 1) + '] ' + option['description'])
    answer = input('Write the number of your answer: ')
    if answer == 'Quit' or answer == 'quit':
        sys.exit()
    while answer != '1' and answer != '2' and answer != '3':
        answer = input('Please choose a number: ')
    choice = question['options'][int(answer) - 1]
    reward = choice['reward']
    teach_points += reward['teach']
    pop_points += reward['pop']
    happy_points += reward['happy']
    print(choice['response'])


def report():
    global teach_points, pop_points, happy_points
    print('You got ' + str(teach_points) + ' teacher points.')
    print('You got ' + str(pop_points) + ' popularity points.')
    print('You got ' + str(happy_points) + ' happiness points.')


for question in questions:
    ask(question)
report()
