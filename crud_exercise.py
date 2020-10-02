##Main menu
def main_menu():
    print('\nWelcome to the Philippine Tourism Quiz!!\n')
    print('What would you like to do? \n')
    print('1 Start the game \n2 Update Question Bank \n3 Quit')
    
    choice = input('Enter your choice: ')
    if choice == '1':
        play_quiz() 
    elif choice == '2':
        update_question()
    elif choice == '3':
        print('Thanks for playing!!\n')
        quit()
    else:
        print('Choice is unavailable. Try again.\n')
    return main_menu()

##Start quiz
def get_tof_questions():
    
    questions = []
    questions.append(['Sampaguita is the National flower of the Philippines.', 'T'])
    questions.append(['There are 15 regions in the Philippines.', 'F'])
    questions.append(['Philippines has a total of 7,107 islands.', 'T'])
    questions.append(['Bacolod City is known for its Masskara Festival.', 'T'])
    questions.append(['Mayon volcano can be found in Sorsogon.', 'F'])
    questions.append(['Siargao is the surfing capital of the Philippines.', 'T'])
    questions.append(['Buko pie is the famous delicacy of Cavite.', 'F'])
    questions.append(['Lucban in Quezon is famous for its Pahiyas Festival.', 'T'])
    questions.append(['Mines View Park is located in Benguet.', 'F'])
    questions.append(['Durian is the famous fruit found in Kidapawan City.', 'F'])
    
    return questions

def player_name():
    name = input('Enter your name:')
    name_list.append(name)
    print('Hey',name.title(),'!\n')
    print("Let's start the quiz!\n")

name_list = []
score_list = [] 

def play_quiz():
    
    #Get true or false questions:
    tof_questions = get_tof_questions() 
    
    #Player Name
    player_name()
        
    score = 0 
    #Show tof questions using a loop
    for q in tof_questions:
        #Present statement
        print('True or False: ' + q[0])

        #Player guess
        guess = input('Enter T of F: ')
        
        #Check if correct
        if guess == q[1]:
            print('Correct!\n')
            
            #Update score
            score = score + 1
        else:
            print('Incorrect.\n')  
            
    #Displaying the final grade
    print("Your FINAL SCORE is " + str(score))
    #Grade
    final_score = int((score/10)*100)
    
    if final_score >= 70:
        print("You passed the quiz! Congratulations!\n")
    else:
        print("Better luck next time.\n")
    #score_list.append(final_score)

    #Displaying the player name & scores
    score_list.append(final_score)
    
    #if len(score_list) == 11:
     #   score_list.pop()
    
    print('The list of players and their scores:')
    for final_score in score_list:
        for name in name_list:
            print('Player Name:',name)
            print('Score:'+str(final_score))



def update_question():
    tof_questions = get_tof_questions() 
    print('What would you prefer?\n')
    print('A Add a question \nR Remove a question\n')
    choice = input('Enter your choice: ')
    
    if choice == 'A':
        add_question(tof_questions)
    elif choice == 'R':
        remove_question(tof_questions)
    else:
        print('Choice is unavailable. Try again.\n')
    return update_question()   

def add_question(quiz_list):
    add_question = input("Enter a new question: ")
    quiz_list.append(add_question)
    for add_question in quiz_list:
        print('Updated Question Bank:' ,quiz_list)
    return main_menu()    
            
def remove_question(quiz_list):
    quiz_list = []
    quiz_list = ["Sampaguita is the National flower of the Philippines.","There are 15 regions in the Philippines.",\
                      "Philippines has a total of 7,107 islands.","Bacolod City is known for its Masskara Festival.",\
                          "Mayon volcano can be found in Sorsogon.","Siargao is the surfing capital of the Philippines.", \
                             "Buko pie is the famous delicacy of Cavite.","Lucban in Quezon is famous for its Pahiyas Festival.",\
                                 "Mines View Park is located in Benguet.","Durian is the famous fruit found in Kidapawan City."]
     
    print(quiz_list)
    item = input('Enter the item you want to remove from the quiz list: ')   
    quiz_list.remove(item)
    print('Updated Question Bank' ,quiz_list)
    return main_menu()

main_menu()
