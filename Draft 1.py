import sys

teach_points = 50
pop_points = 50
happy_points = 50

questions = [
    {
        'prompt': 'Hi there! Are you ready to start school survival?',
        'options': [
            {
                'description': 'I studied!',
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': 'Um, okay weirdo',
            },
            {
                'description': "My friends say it's good.",
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': 'Good friends!',
            },
            {
                'description': 'What is this game?',
                'reward': {'teach': 0, 'pop': 0, 'happy': 1},
                'response': 'Let me explain',
            },
        ],
    },
    {
        'prompt': 'This is a game where you have to survive a day of school.',
        'options': [
            {
                'description': "I'm pretty good at that already",
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': 'No need to be arrogant.',
            },
            {
                'description': "I'm only good at the lunches.",
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': "We'll have that too",
            },
            {
                'description': '(sarcastically) What a treat.',
                'reward': {'teach': 0, 'pop': 0, 'happy': 1},
                'response': "It's fun, I swear.",
            },
        ],
    },
    {
        'prompt': 'You will be graded on the things how much your teachers like you, popularity and happiness.',
        'options': [
            {
                'description': "I'm a teacher's pet supreme.",
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': 'I could tell.',
            },
            {
                'description': 'I have more friends then you have brain cells.',
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': 'Jeez, just telling you the rules.',
            },
            {
                'description': "I'll be happy, at least",
                'reward': {'teach': 0, 'pop': 0, 'happy': 1},
                'response': 'Good on you',
            },
        ],
    },
    {
        'prompt': 'Your timetable for today is as follows: Drama, English, Mathematics, '
                  'Lunch, Physical Education, History. You can access this at anytime by '
                  'typing "timetable"',
        'options': [
            {
                'description': "Woah! Where's my science?",
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': 'We could only fit 5 periods, just chill,',
            },
            {
                'description': 'What about recess?',
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': 'Tough luck.',
            },
            {
                'description': "I mean, it's not the worst I've gotten.",
                'reward': {'teach': 0, 'pop': 0, 'happy': 1},
                'response': "That's the spirit!",
            },
        ],
    },
    {
        'prompt': 'Now, onto your first class!',
        'options': [
            {
                'description': "I'm eager to learn!",
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': '(under breath) nerd',
            },
            {
                'description': "Already? Can't we have recess?",
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': "You're funny, aren't you?",
            },
            {
                'description': 'Onwards and upwards.',
                'reward': {'teach': 0, 'pop': 0, 'happy': 1},
                'response': 'Or downwards and sidewards, but...',
            },
        ],
    },
    {
        'prompt': "You realise you're a little early to drama class.",
        'options': [
            {
                'description': 'I revise my lines.',
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': 'The teacher walks in and sees you. She gives you an approving nod',
            },
            {
                'description': 'I talk to the other kids',
                'reward': {'teach': 0, 'pop': 2, 'happy': -1},
                'response': 'It\'s boring, but you know they like you a little more.',
            },
            {
                'description': 'I pull out my phone.',
                'reward': {'teach': -1, 'pop': 1, 'happy': 1},
                'response': 'The teacher walks in early and pulls it out of your hand before you say a word.',
            },
        ],
    },
    {
        'prompt': 'You walk in and take your seat. Your teacher goes around the circle asking everyone if they learned their lines.',
        'options': [
            {
                'description': 'Of course!',
                'reward': {'teach': 1, 'pop': -1, 'happy': 1},
                'response': 'She\'s suspicious, but believes you. The popular kids snicker.',
            },
            {
                'description': 'I was playing video games',
                'reward': {'teach': -1, 'pop': 2, 'happy': 0},
                'response': 'You\'ve gotten yourself a Friday detention, but the popular kids look like they aprove.',
            },
            {
                'description': 'I did, but I haven\'t learned it as well as I would like to have.',
                'reward': {'teach': 1, 'pop': -1, 'happy': 1},
                'response': 'The teacher looks begrudgingly happy that you told the truth, and so are you.',
            },
        ],
    },
    {
        'prompt': 'The Drama class passes relatively incident-free. What do you say to the teacher while leaving?',
        'options': [
            {
                'description': 'That was a really fun lesson!',
                'reward': {'teach': 2, 'pop': -1, 'happy': 0},
                'response': 'The teacher looks please, but the popular kids giggle.',
            },
            {
                'description': 'Pull a trick on the teacher',
                'reward': {'teach': -2, 'pop': 3, 'happy': 0},
                'response': 'You tell the teacher her shoelace is untied then flick her head up. You just earned yourself a Sunday detention. The popular kids make a huge commotion. They\'re obviously impressed.',
            },
            {
                'description': 'Make a lame joke.',
                'reward': {'teach': 0, 'pop': -1, 'happy': 2},
                'response': 'You ask her what 2 weeks are and she says a fortnight. You giggle and glance to the popular kids, but they shake their heads. You though it was funny.',
            },
        ],
    },
    {
        'prompt': 'Your next class is English. You\'ve actually read the book, but your '
                  'teacher is really scary. You know you can contribute, but do you?',
        'options': [
            {
                'description': "Of course I'll contribute, the teacher will warm up to me",
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': "I don't know why, but your plan barely works; by the end of the lesson your teacher likes you more",
            },
            {
                'description': "I'll probably just talk to my friends",
                'reward': {'teach': -1, 'pop': 2, 'happy': 0},
                'response': "For some reason the popular kids invite you to their table. You sit down and talk to them for most of the lesson. The teacher catches you once or twice, but you mostly fly under the radar.",
            },
            {
                'description': "I'll probably just get some of my other homework done",
                'reward': {'teach': 1, 'pop': -1, 'happy': 1},
                'response': "It looks like you're working hard, so your teacher is happy. One of the popular kids passes you a note that says 'Nerd!', but you concentrate on the fact that you'll have some extra time when you get home",
            },
        ],
    },
    {
        'prompt': "Near the end of the lesson, your teacher calls on you. She asks what you thought about the character relationships.",
        'options': [
            {
                'description': "I thought they might have been established a bit too slowly",
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': "She nods approvingly before letting you off the hook.",
            },
            {
                'description': "They were kind of stupid.",
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': "Your teacher asks you to elaborate and you have nothing else to say. Everyone laughs quietly, but they're not really laughing AT you. More WITH you..",
            },
            {
                'description': "They were a bit unrealistic.",
                'reward': {'teach': 0, 'pop': 0, 'happy': 1},
                'response': "Three people instantly put their hands up to argue, but the teacher still values your contribution.",
            },
        ],
    },
    {
        'prompt': "Your next class is Maths. When you walk in, you see that there are three tables: one with the nerds who know what they're doing, one with the popular kids, and one with your friends. Who do you sit with?",
        'options': [
            {
                'description': "I'll sit with the 'nerds', but I don't like that word anyway",
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': "Throughout the less you're attentive",
            },
            {
                'description': "I'll sit with the popular kids",
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': "You mostly spend the lesson making jokes. You doubt that you've learned much, but they like you more.",
            },
            {
                'description': "I'll sit with my friends, obviously",
                'reward': {'teach': 0, 'pop': 0, 'happy': 1},
                'response': "You learn a little, but mostly talk to your friends.",
            },
        ],
    },
    {
        'prompt': "You get your homework and decide to do some now so you don't have to do it at home. The first question is if 3x = 6, what is x?",
        'options': [
            {
                'description': "3",
                'reward': {'teach': 0, 'pop': 0, 'happy': 0},
                'response': "Wrong!",
            },
            {
                'description': "18",
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': "Wrong",
            },
            {
                'description': "2",
                'reward': {'teach': 0, 'pop': 0, 'happy': 0},
                'response': "Right!",
            },
        ],
    },
    {
        'prompt': "What number represents the gradient in y = mx + c?",
        'options': [
            {
                'description': "y",
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': "Wrong!",
            },
            {
                'description': "m",
                'reward': {'teach': 0, 'pop': 1, 'happy': 0},
                'response': "Right!",
            },
            {
                'description': "c",
                'reward': {'teach': 0, 'pop': 0, 'happy': 0},
                'response': "Wrong!",
            },
        ],
    },
    {
        'prompt': "What is 1 + 1 + 1 + 1 + 1 + 1 x 0 + 1?",
        'options': [
            {
                'description': "6",
                'reward': {'teach': 1, 'pop': 0, 'happy': 0},
                'response': "Right!",
            },
            {
                'description': "1",
                'reward': {'teach': 0, 'pop': 0, 'happy': 0},
                'response': "Wrong!",
            },
            {
                'description': "7",
                'reward': {'teach': 0, 'pop': 0, 'happy': 0},
                'response': "Wrong!",
            },
        ],
    },
    {
        'prompt': "All you have for the rest of the day is free periods. How do you spend your time?",
        'options': [
            {
                'description': "I'll finish off any assignments",
                'reward': {'teach': 5, 'pop': 0, 'happy': 0},
                'response': "`You get them all done by the end of the day and spend the rest of your time perfecting them to what you think is an A+ standard. you feel very confident about them.",
            },
            {
                'description': "I'll just leave and grab some food.",
                'reward': {'teach': 0, 'pop': 5, 'happy': 0},
                'response': "You got some friends to come with and no-one noticed you. It was pretty boring though.",
            },
            {
                'description': "I'll go to the library, find a corner and play on my phone.",
                'reward': {'teach': 0, 'pop': 0, 'happy': 5},
                'response': "You had a surprising amount of fun.",
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
    answer = input('Type the number of your answer: ')
    if answer == 'quit':
        sys.exit()
    if answer == 'timetable':
        print('Drama')
        print('English')
        print('Mathematics')
        print('Lunch')
        print('Physical Education')
        print('History')
        answer = input('Please type the number of your answer: ')
    while answer != '1' and answer != '2' and answer != '3':
        answer = input('Please type the number of your answer: ')
    choice = question['options'][int(answer) - 1]
    reward = choice['reward']
    teach_points += reward['teach']
    pop_points += reward['pop']
    happy_points += reward['happy']
    print(choice['response'])


def report():
    global teach_points, pop_points, happy_points
    favourite = input("Now that the day is over, we need to assess how you did. First of all, what do you think is most important in school?")
        "[1] Grades"
        "[2] Popularity"
        "[3] Happiness"
    while favourite != 1 and favourite != 2 and favourite != 3:
        favourite 
    while least_favourite != 1 and least_favourite != 2 and least_favourite != 3 and least_favourite
    least_favourite = input("And what do you think is the least important?")
    print('You got ' + str(teach_points) + ' teacher points.')
    print('You got ' + str(pop_points) + ' popularity points.')
    print('You got ' + str(happy_points) + ' happiness points.')


for question in questions:
    ask(question)
report()
