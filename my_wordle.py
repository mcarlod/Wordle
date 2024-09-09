import random

# function that validates the users guess and returns the guess once it follows the rules
def get_wordle_guess(word_list, attempts):
    number = 0
    guess = ''
    while guess not in word_list or number != 5:
        number = 0
        print('\nPlease enter your guess - attempt', attempts, end='')
        guess = input(': ')
        number = len(guess)
        if number != 5:
            print('\nFive letter words only please.')
        elif guess not in word_list:
            print('\nNot in word list!')
    return guess

# function that reads the file for words
def create_word_list(file):
    infile = open(file, "r")
    line = infile.readline()
    if line != '':
        words = line.split()
        if len(words) > 0:
            word_list = words
        line = infile.readline()
    infile.close()
    return word_list

print('\n\n---------------------------------')
print('--         My Wordle!          --')
print('-- Guess the Wordle in 6 tries --')
print('---------------------------------')

# prompts for input whether use wants to start or not
start = input('\n\nWould you like to play My Wordle [y/n]? ')
while start != 'y' and start != 'n':
    start = input('Would you like to play My Wordle [y/n]? ')
if start == 'n':
    print('\n\nNo worries... another time perhaps... :)')
elif start == 'y':
    
    # prompts to restart
    restart = 'y'
    
    # keeps track of how many tries all in all
    rounds = 1
    attempts = 1
    
    #keeps track and stops the loop if the user gets it
    correct_answer = 'n'
    
    # keeps track of solved and unsolvedwordles
    solved = 0
    unsolved = 0
    
    while restart == 'y':
        
        # variable to read the file
        word_list = create_word_list("word_file.txt")
        
        # variable to display the user's guess
        guess_list =['|','-','-','-','-','-','|']
        
        # chooses a word from word_list
        wordle = random.choice(word_list)
        print('\nWordle is:', wordle)
        
        # printing of starter box
        print('\n-------------')
        index = 0
        while index < len(guess_list):
            print(guess_list[index], end=' ')
            index += 1
        print('')
        
        # keeps track of correct and used letters
        correct_letters = ''
        used_letters = ''
        
        # loop that stops after 6 attempts or if the user has guessed correctly
        while attempts <=6 and correct_answer != 'y':
            
            # prompts user for their guess
            guess = get_wordle_guess(word_list, attempts)
            print('\nYou guessed: ', guess)
            
            # prints the user's guess in box
            print('\n-------------')
            index = 0
            guess_index = 0
            while index < len(guess_list):
                if guess_list[index] != '|':
                    guess_list[index] = guess[guess_index]
                    guess_index += 1
                print(guess_list[index], end=' ')
                index += 1
            print('')
            
            # checks if character is in the same place 
            index = 0
            guess_index = 0
            wordle_index = 0
            correct_list =['|']
            result = ''
            
            while index < len(guess_list):
                # turns wordle into a list
                wordle_list = []
                for letter in wordle:
                    wordle_list.append(letter)
                
                # displays correspong ^ * - characters
                if guess_list[index] != '|':
                    if guess_list[index] == wordle[guess_index]:
                        correct_list.append('^')
                        wordle_list.remove(wordle_list[wordle_index])
                    elif guess_list[index] in wordle and guess_list[index] not in wordle_list:
                        correct_list.append('-')
                        wordle_list.remove(wordle_list[wordle_index])
                    elif guess_list[index] in wordle_list and guess_list[index] in wordle:
                        correct_list.append('*')
                        wordle_list.remove(wordle_list[wordle_index])
                    else:
                        correct_list.append('-') 
                        wordle_list.remove(wordle_list[wordle_index])
                    guess_index += 1  
                index += 1   
            correct_list.append('|')
            
            # displaying the turnout on screen
            for element in correct_list:
                result += element + ' '
            print(result)              
            print('|')
            
            # counts and display correct and wrong spots
            correct = 0
            wrong = 0
            for i in correct_list:
                if i == '^':
                    correct += 1
                elif i == '*':
                    wrong += 1
            print("| Correct spot(^):",correct)
            print("| Wrong spot(*):  ",wrong)
            print('|')
            
            # puts the letters in their corresponding strings
            for letter in guess:
                if letter not in correct_letters and letter in wordle:
                    correct_letters += letter + ' '
                elif letter not in used_letters and letter not in wordle:
                    used_letters += letter + ' '
            print('| Correct letters:', correct_letters)
            print('| Used letters:', used_letters)
            
            # keeps track of total number of attemps
            attempts += 1
            
            #stops if its correct
            if correct == 5:
                correct_answer = 'y'
                solved += 1
                if attempts < 7:
                    print("\n\nSolved in", attempts-1, "tries! Well done!")
                else:
                    print("\n\nPhew! Solved in", attempts-1, "tries! Well done!")
    
        # displays text when the user does not guess right in 6 attempts
        if correct != 5:
            unsolved += 1
            print('\n\nOh no! Better luck next time!')
            print('\nThe wordle was:', wordle)
    
        # prompts to restart
        restart = input('\n\nWould you like to play again [y/n]? ')
        while restart != 'y' and restart != 'n':
            restart = input('Would you like to play again [y/n]? ')
        if restart == 'y':
            rounds += 1
        
        # restart attempts
        attempts = 1
        correct_answer = 'n'
    
    # displays wordle summary to screen with number of wordles solved and unsolved
    print('\n\nMy Wordle Summary')
    print('=================')
    print('You played', rounds, 'games:')
    print('  |--> Number of wordles solved:  ', solved)
    print('  |--> Number of wordles unsolved:', unsolved)       
    print('\n\nThanks for playing!')