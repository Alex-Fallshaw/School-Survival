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

