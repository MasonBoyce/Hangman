import random
#Give a Single Player or Multiplayer Option
#if Single Player Take Text from a predetermined List
#If Multiplayer recieve text from 1 Player
# Create a Dictionary with letter and all of its indices
#Display Letters of the word with "_"
#Take input from Guessing Player
# If guess is incorrect remove a live (max 5)
# If guess is correct replace "_" with correct letter
#Repeat until live == 0 or no more letters to guess


Hangman_Words = ["abruptly", "absurd","abyss","affix","askew","avenue","awkward","axiom","azure","bagpipes","bandwagon","banjo","bayou","beekeeper","bikini","blitz","blizzard","boggle","bookworm","boxcar","buckaroo","buffalo","buffoon","haiku","haphazard","hyphen","icebox","injury","ivory","ivy",
"jackpot","jawbreaker","jaywalk","jazziest","jazzy","jelly","jigsaw","jinx","jiujitsu","jockey","jogging","joking","quips","quiz","quizzes","quorum","razzmatazz","rhubarb","rhythm","scratch","shiv","snazzy","sphinx","spritz","squawk"]
#def ModeisSinglePlayer():
  #  mode = input("Type 'S' for Sinlge Player and 'M' for Multiplayer")
    #while mode != "S" and mode != "M" and mode != "s" and mode != "m":
    #    mode = input("Type 'S' for Sinlge Player and 'M' for Multiplayer")
    #if mode == "S" or mode == 's':

     #   return True
    #elif mode == 'M' or mode == 'm':
     #   return False

def WordSelection():
    #if ModeisSinglePlayer() == True:
      #  print("in word select true")
    #SinglePlayer
    #Takex from List of words
    #pick random number and whatever that number is pick that word in list
        num_words = len(Hangman_Words)
        random_num = random.randint(0, num_words)
        return (Hangman_Words[random_num])
   # else:
    #MultiPlayer
    #Take an Input from Player 
        #Word = input("Write One Word for your opponent to Guess (NO Numbers or Special Characters)")
        #return Word

def Letter_Placement(Word):
    #Create Empty Dictionary
    #For each word loop through every letter
    #For each Letterr Add to Dictionary the letter as the Key and the Index as the Value
    #Set the default as key, list of values
    # Return Dictionary
    Dict = {}
    for index, letter in enumerate(Word):
        Dict.setdefault(letter,[]).append(index)
    return Dict
    

def SetupBoard(Word):
    board = ""
    for i in (Word): 
        board += "_ "
    return board

def Guessing(Dict,letter_guessed):
    #Return True if letter guessed correctly
    if letter_guessed in Dict:
        return True
    elif letter_guessed not in Dict:
        return False

def UpdateBoard(Dict,board,letter):
    #take in the string board and the letter correctly guessed
    # Find the vlaues of the letter
    # Take each of those values and replace the current ind
    index_values = Dict.get(letter)
    for i in index_values:
        i *=2 
        NewBoard = board[:i] + letter +board[i+1:]
        board = NewBoard
    return NewBoard

def GameUpdate(board,lives):
    print("You have {} lives left".format(lives))
    print (board)


def IsGameOver(board,lives):
    def IsBoardComplete(board):
        for i in board:
            if i == "_":
                return False
        return True

    if lives == 0 or IsBoardComplete(board):
        return True
    else:
        return False
    
    
def main():
    WordToGuess = WordSelection()
    Dict = Letter_Placement(WordToGuess)
    lives = 7
    board = SetupBoard(WordToGuess)
    GameUpdate(board,lives)
     
    while IsGameOver(board,lives) == False:
        letter_guessed = input("Pick a Letter\n")
        while len(letter_guessed) != 1:
            letter_guessed = input("Pick a Letter\n")
        if Guessing(Dict,letter_guessed):
            board = UpdateBoard(Dict,board,letter_guessed)
        else:
            lives -= 1
        GameUpdate(board,lives)
    if lives == 0:
        print("You lost the Correct Word was {}".format (WordToGuess))
    else:
        print("You Won with {} Lives Left" .format(lives))
     


    

main()




