class Tiles:
    def __init__(self, word):
        self.tiles = ['_ ']*len(word)

    def print(self):
        print(self.tiles)
        return

    def update_tiles(self, char, word):
        for i in range(len(word)):
            if char == word[i]:
                self.tiles[i] = char

    def is_complete(self):
        if '_ ' not in self.tiles:
            return True
        else:
            return False

def print_hangman(errors):

    #Change to single line string variables using \n, adding each component as errors increase
    if errors==0:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")

    if errors==1:
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        print("-")

    if errors==2:
        print("  ")
        print("|")
        print("|")
        print("|")
        print("-")

    if errors==3:
        print("----------- ")
        print("|           ")
        print("|           ")
        print("|           ")
        print("-           ")

    if errors==4:
        print("----------- ")
        print("|         | ")
        print("|           ")
        print("|           ")
        print("-           ")

    if errors==5:
        print("----------- ")
        print("|         | ")
        print("|         O ")
        print("|           ")
        print("-           ")

    if errors==6:
        print("----------- ")
        print("|         | ")
        print("|         O ")
        print("|         | ")
        print("-           ")

    if errors==7:
        print("----------- ")
        print("|         | ")
        print("|         O ")
        print("|        \\| ")
        print("-           ")

    if errors==8:
        print("----------- ")
        print("|         | ")
        print("|         O ")
        print("|        \\|/")
        print("-           ")

    if errors==9:
        print("----------- ")
        print("|         | ")
        print("|         O ")
        print("|        \\|/")
        print("-         ' ")

    if errors==10:
        print("----------- ")
        print("|         | ")
        print("|         O ")
        print("|        \\|/")
        print("-        /' ")

    if errors==11:
        print("----------- ")
        print("|         | ")
        print("|         O ")
        print("|        \\|/")
        print("-        /'\\")

        return True

def guess(word):
    if in_word(word, char):
        print("Guess Correct!")
        return True, char
    else:
        return False, char

def in_word(char, word):
    count = 0
    if char in word:
        count += 1
    if count == 0:
        return False
    else:
        return True


game_over = False
errors = 0

print("Player One enter your word:")
word = input().upper()
hangman = Tiles(word)

while not game_over:
    hangman.print()

    print("Guess a character: ")
    char = input('').upper()

    guess(word)
    print(in_word(char, word))
    if not in_word(char, word):
        errors +=1

    print_hangman(errors)

    print(hangman.tiles)

    hangman.update_tiles(char, word)

    print(hangman.tiles)
    if hangman.is_complete():
        game_over = True
