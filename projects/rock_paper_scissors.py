#!/usr/bin/python

import random

def get_hand(hand):
    # 0=Rock, 1=Paper, 2=Scissors0
    hand = int(hand)
    if hand == 0:
        hand_str = "Rock"
    elif hand == 1:
        hand_str = "Paper"
    elif hand == 2:
        hand_str = "Scissors"
    return hand_str
        
def determine_winner(uplay, cplay):
    uplay = int(uplay)
    cplay = int(cplay)
    if uplay == 0 and cplay == 1:
        winner = "computer"
    elif uplay == 0 and cplay == 2:
        winner = "user"
    elif uplay == 1 and cplay == 0:
        winner = "user"
    elif uplay == 1 and cplay == 2:
        winner = "computer"
    elif uplay == 2 and cplay == 0:
        winner = "computer"
    elif uplay == 2 and cplay == 1:
        winner = "user"
    elif uplay == cplay:
        winner = "tie"
    return winner

user_play = 0
comp_play = 0 
loop_count = 0

while user_play == comp_play:
    if loop_count > 0:
        print("This round is a tie.. please try again! ")
        input("Press enter to continue..")
    user_play = input("Please enter 0 for Rock, 1 for Paper or 2 for Scissors:  ")
    comp_play = random.randrange(3)
    user_play = int(user_play)
    loop_count += 1
    print(loop_count)
    print(f"{user_play},{comp_play}")

user_play_str = get_hand(user_play)
comp_play_str = get_hand(comp_play)

print(f"Users entry: {user_play_str}")
print(f"Computers entry: {comp_play_str}")

if determine_winner(user_play, comp_play) == "user":
    print(f"You won!!!")
elif determine_winner(user_play, comp_play) == "computer":
    print(f"Sorry the computer beat you this time...")






#while user_play == comp_play:
#    print(f"Your play {user_play_str}")
#    print(f"The Computers play: {comp_play_str}")
#    print("This round is a tie... please try again.")
#    user_play = input("Please enter 0 for Rock, 1 for Paper or 2 for Scissors:  ")
#    comp_play = random.randrange(3)
#    get_hand(hand)
    
    


