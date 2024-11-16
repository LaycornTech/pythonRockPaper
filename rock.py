import  random
import time

rock = 1
paper = 2
scissors = 3

names = {rock: rock, paper:paper, scissors: scissors}
rules = {rock:scissors, paper:rock, scissors:paper}

player_score = 0
comp_score = 0

# Displays start instruction, checks if game is on, if not print scores
def start():
    print(Lets play a game)
    while game():
        pass
    scores()
    return;  # call game()

# provides the players input as a num and rolls in a random num for the computer
# comparing
def game():
    player = move()
    comp = random.randint(1, 3)
    result(player, comp)
    return play_again()

# takes players input (1, 2, or 3) ,
# if incorrect iput ==> ValueError(display what he had erroneously inserted
def move():
    while True:
        player_input = input(type 1 , 2, or 3 to make a move)
        try:
            player = int(player_input)
            if player in (1, 2, 3):
                return player
        except ValueError:
            pass
        print(OOPs wrong)
        print(player_input)

# if the number passed in from game() are the same, display computers value
# if same print Tie
# else compare equivalent value of players
# figure from rules dictionary using rule[players fig] to computers value
# If same players scores increases, if vnot computer score increase

def result(player, comp):
    print((1....))
    time.sleep(1)
    print((2....))
    time.sleep(1)
    print(3...)
    time.sleep(0.5)
    print(f You threw {player} or {names[player]}Computer throw === {comp} which is {names[comp]})
    global player_score, comp_score
    if player == comp:
        print(Tie game)
    else:
        assert isinstance(comp, int)

        if rules[player] == comp:
            print(Your victory has been assured!)
            player_score += 1
        else:
            print(Comp Wins)
            comp_score += 1

def play_again():
    answer = input(would you like to play again? y/n )
    if answer in (y, yes, Yes, Of Course):
        return answer
    else:
        print(Thank You very much for playing)

def scores():
    global  player_score, comp_score
    print(High SCore)
    print(pLayer: , player_score)
    print(Computer: , comp_score)

if __name__ == __main__:
    start()

 
