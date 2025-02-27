#Dylan King
#Hangman game

import random
EE= 'e'

#********************************************************
#This function will check to see if the guess matches a word
#word is a string
#guess is a string
#words is an array
#returns an integer
#********************************************************
def wordCheck (guess, words):
    wordsLength = len(words)
    
    for counter in range (wordsLength):
        if guess == words[counter]:
            return counter
    return -1




#********************************************************
#This function will generate a word based off a random integer
#returns an array
#********************************************************
def wordGen ():
    
    word = ["friend", "red ball", "air", "mace", "block", "program", "food", "skeleton", "car", "goose", "love", "ant", "can", "sand", "dad joke", "cow", "valentines", "dungeon", "alien", "felt", "jack", "place", "column", "muscle car", "life", "reindeer", "morning", "santa", "alive", "star", "floor", "world", "boat", "forever", "far", "tower", "sports car", "bell", "bottle", "friends and rebels", "staircase", "minecraft", "fell", "laughter", "projector", "rafter", "headphones", "submarine", "computer", "wonder", " chair", "desk", "pencil", "book", "game", "mouse", "animal"]
    
    length = len(word)
    word = word[random.randrange(length)]

    if EE != 'e':
        word = "EEEEEEEEE"

    return word



#*******************************************************
#This function will generate a random sentence for fun
#fun is a string
#returns a string
#*******************************************************
def easterEgg ():
    
    funnySentence = ["are you intentionally doing this", "what's going on", "maybe try something new", "hey, maybe try pressing the button next to the you keep repeating", "Hello, can you hear me..."]
    length = len(funnySentence)
    integer = random.randrange (length)
    
    return funnySentence[integer]



#*******************************************************
#this function checks if all numbers in arrays match
#list1 is an array
#list2 is an array
#returns a boolean
#*******************************************************
def arrayCheck (list1, list2, length):
    check = True
    counter = 0
    
    while check == True and counter < length :
        if list1[counter] != list2[counter]:
            check = False
        counter = counter + 1

    return check




#********************************************************
#MAIN program
#********************************************************
def main ():
    word = wordGen ()       #Initializing variables
    check = False
    wordLength = len(word)
    found = []
    guessed = []
    guesses = 0
    funCounter = 0
    used = False
    position = 0
    position1 = [0]
    words = []
    number = 1
    
    for counter in range (wordLength):
        if word[counter] == " ":
            words.append (word[position: counter])
            position = counter + 1
            position1.append (counter)
            number = number + 1
            
    words.append (word[position: counter + 1])


    for counter in range (wordLength): #Creating the initial blanks
        if word[counter] == ' ':
            found.append (' ')
        else:
            found.append ("_")

    while check == False and guesses < 10:
        
        print ("You have", 10 - guesses, "guesses left")
        
        for counter in range (wordLength):     #Printing blanks
            print (found[counter], end = " ")
        print ()
        
        

        guess = input("Enter a letter: ")
        
        length = len(guessed)
        error = False
        
        for counter in range (length):
            if guess == guessed[counter]:
                error = True
        
        while error == True or EE != 'e':      #Checking for already guessed letters
            print ()
            print ("You have already guessed this letter please try again")     
            fun = guess
            
            
            if funCounter == 2 or EE != 'e':     #A fun easter egg
                print ()
                print ("You've entered that 3 times now. Is your keyboard running?")
                print ()
                guess = input("Enter a letter: ")
                
                if guess == "y":     #Answering player if they responded
                    print ("then you better go catch it!")
                    print ()
                    
                    if used == False:
                        guesses = guesses - 3
                        used = True
                    guess = input("Enter a letter: ")
                    
                elif guess == "n":
                    print ("Dang sorry to hear that you should get a new one")
                    print ()
                    
                    if used == False:
                        guesses = guesses - 1
                        
                    guess = input("Enter a letter: ")

                elif EE != 'e':
                    print ("did you remove the E")
                    
                elif guess == fun: #adding stupid comments until player changes their guess
                    print ("Jeez something must be really wrong")
                    print ()
                    guess = input("Enter a letter: ")
                    
                    while guess == fun:
                        funnySentence = easterEgg ()
                        print (funnySentence)
                        print ()
                        
                        if funnySentence == "Hello, can you hear me...":
                            print ()
                            print ("I don't think he can hear me")
                            print ()
                            
                        guess = input("Enter a letter: ")
                        
            else:
                guess = input("Enter a letter: ")
                
            if fun == guess:  #counts how many times the same response was given
                funCounter = funCounter + 1
            else:
                funCounter = 0
                
            fun = guess
            
            length = len(guessed)

            error = False
            for counter in range (length): #checks to see if player already guessed the input
                if guess == guessed[counter]:
                    error = True
                    
        length = len(guess)
        
        check = wordCheck (guess, words)

        guessed.append (guess)
        print ()
        print ()
        
        foundCheck = False
        
        if EE!= 'e':
            for counter in range (50):
                print("E")
            again = False
            length = len(word)
            for counter in range(length):
                found[counter] = word[counter]


        if check != -1 and number == 1:
            for counter in range (position1[check], length + position1[check]):
                found[counter] = word[counter]
                foundCheck = True
        
        elif check != -1 and number > 1:
            for counter in range (position1[check], 1 + length + position1[check]):
                found[counter] = word[counter]
                foundCheck = True
        
        else:
            for counter in range (wordLength): #Replacing blanks in found array
                if guess == word[counter]:
                    found[counter] = word[counter]
                    foundCheck = True
                
        if foundCheck == False:
            guesses = guesses + 1
        
        length = len(guessed)
        print ("Letters used:", end = " ")    #Printing used letters
        for counter in range (length):
            print (guessed[counter], end = ", ")
        print ()
        print ()
        

        
        check = arrayCheck (word, found, wordLength) #Checking if both arrays match
        
        if check == True:
            print ("congratulations you found the word")
            
    print ()
    print ()
    
    for counter in range (wordLength):     #Printing blanks
        print (word[counter], end = " ")
    print ()
    print ()
    
    if guesses >= 10:
        print ("You ran out of guesses. Better luck next time")
        
main ()

playAgain = True

while playAgain == True:     #looping the game
    print ()
    print ()
    print ("would you like to play again:")
    again = input("")

    yes = ["yes", "y", "Y", "Yes", "again", "go", "Go", ""]

    length1 = len(yes)
    playAgain = False

    for counter in range (length1):
        if again == yes[counter] and EE== 'e':
            print ()
            print ()
            print ()
            print ()
            print ()
            playAgain = True
            main ()

print ()
print ()
print ()
print ()
print ()
print ("Thanks for playing")