#Alex F's Text Based Adventure Game - School Survival
teacher_points = 50
popularity_points = 50
happiness_points = 50
def yn_question(question, y_response, y_teacher, y_popularity,y_happiness, n_response,n_teacher,n_popularity,n_happiness):
    answer = input(question + " Please print Y for yes or N for no. ")
    if answer == 'Quit' or answer == 'quit' or answer == 'Exit' or answer == 'exit':
        HHHHEEEEELLLLLPPPPPPP
    while answer != Y or != N:
        answer = input('Please print Y for yes or N for no')
    if answer == Y:
        print(y_responce)
        teacher_points += int(y_teacher)
        popularity_points += int(y_popularity)
        happiness_points += int(y_happiness)
    elif answer == N:
        print(n_responce)
        teacher_points += int(n_teacher)
        popularity_points += int(n_popularity)
        happiness_points += int(n_happiness)


name = input('Hi there! My name\'s Alex. What\'s your name?')
answer1 = input('Hi ' + name + '! So, I hear that you want to play my game. Are you sure? It\'s pretty hard. Y or N')
if answer1 == 'Y' or answer1 == 'N':
    answer2 = input('You understand the game already! Just in case you didn\'t get it, sometimes I\'m going to ask you questions, and you might have to respond with yes or no. To save everyone\'s time, I decided that all you would have to do is type 1 letter! Y for yes or N for no. Got it? Y or N. ')
else:
    answer2 = input('Sorry, I forgot to explain. Sometimes I\'m going to ask you questions, and you might have to respond with yes or no. To save everyone\'s time, I decided that all you would have to do is type 1 letter! Y for yes or N for no. Got it? Y or N. ')
while answer2 != 'Y' or answer2 != 'N':
    print('Please answer Y or N. ')


    favourite = input('Great! Now, some of the questions aren\'t going to be Y or N, but I can\'t predict all of the possible responses. So, I\'ve decided to create a number system. I\'m going to assign each answer a numerical value that you can enter. For example, what do you care about the most during school? 1 = Good grades, 2 = Popularity, and 3 = Happiness.')


def print_scene(sceneID):
    if (sceneID == 1):
        print("Some stuff")
    elif sceneID == 2:
        print ("Some other stuff")

def get_next_scene(currentSceneID, choice):
    if (currentSceneID == 1 and choice == 1):
        return 2



# ==========

#loop this:
#print text and questions for scene
#get choice from player
choice  = int(input("Input: "))
#use the choice to figure out the next scene
