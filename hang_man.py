
import random
import time
gameOver = False
ez = False
h1 = """
------
|   |
|
|
|
------
"""
h2 = """
------
|   |
|   O
|
|
------
"""
h3 = """
------
|   |
|   O
|   |
|
------
"""
h4  = """
------
|   |
|   O
|   |-
|
------
"""
h5  =  """
------
|   |
|   O
|  -|-
|
------
"""
h6 = """
------
|   |
|   O
|  -|-
|  /
------
"""
h7 = """
------
|   |
|   O
|  -|-
|  / \\
------
"""

h8 = """
------
|   |
|   O
| /-|-
|  / \\
------
"""
h9 = """
------
|   |
|   O
| /-|-\\
|  / \\
------
"""
h10 = """
------
|   |
|   O
| /-|-\\
| -/ \\-
------
"""
lives = 10
t = 0
def hang_man_die():

    if lives == 1:
        print(h10)
    if lives == 2:
        print(h9)
    if lives == 3:
        print(h8)
    if lives == 4:
        print(h7)
    if lives == 5:
        print(h6)
        print("you are have way")
    if lives == 6:
        print(h5)
    if lives == 7:
        print(h4)
    if lives == 8:
        print(h3)
    if lives == 9:
        print(h2)
    if lives == 10:
        print(h1)
        gameOver = True
def get_the_word():

    with open("C:\\Users\\evanj\\Desktop\\Hangman\\word_list.txt") as f:
        contents = f.readlines()
        hangWord = contents[y]
        hangWord = hangWord.strip()
        hangWord = contents[y]


print ("this is a hang man game")
print ("you will have to guess the letters")
print ("good luck")
print("type 1 FOR HARD MODE type anything thing else for ez mode")



y = random.randint(0,58108)
import time                 

with open("C:\\Users\\evanj\\Desktop\\Hangman\\word_list.txt") as f:
    contents = f.readlines()



print("The Length of the Word is", str(len(contents[y])))
hangWord = contents[y]
hangWord = hangWord.strip()

allLettersFound = False
numberOfMisses = 0
foundLetters = [0] * len(hangWord)
z = str(input())
if z == "1":
    lives = 5
    print("hard mode selected")
else:
    print("ez mode selected")
    ezMode = True 
    if len(hangWord)>5:
        print("hi")
        print("The Length of the Word is", str(len(contents[y])))




while(not allLettersFound and not gameOver):
    time.sleep(1)
    t+=1

    print("Input a letter and we will tell you if it is in the word other wise you Hang") 
    guess = str(input())
    if len(guess)!=1:
        print("Please Enter Only One Letter!")
        pass
    else:
        if hangWord.__contains__(guess):
            print("You got one!")
            i = 0
            while(i != len(hangWord)):
                if hangWord[i] == guess:
                    foundLetters[i]= guess
                i+=1

            
            # looking to see if all the letters have been found (non-zero) in the foundLetters array
            i = 0
            while(i != len(foundLetters)):
                if(foundLetters[i] == 0):
                    break
                else:
                    i+=1

            # determine if all the  letters are found by looking at i from the  
            # previous use, if i is == to the number of found letters then we 
            # must have found them all
            if(i == len(foundLetters)):
                allLettersFound = True
                print(hangWord)
                print("YOU WIN!")

            # print out found letters so far
            i=0
            while(i != len(foundLetters)):
                  print(foundLetters[i])
                  i += 1
        else:
            numberOfMisses += 1
            print("you missed!")
            lives-=1
            #print your hangman
            hang_man_die()
    if lives == 1:
        print(f"the word was {hangWord}")
        time.sleep(1)
    else:
        pass
    print(f"its been {t} seconds")

