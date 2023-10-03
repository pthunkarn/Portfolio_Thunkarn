import random
choices = ["rock", "scissors", "paper"]

def rsp():
    bot_score = 0
    user_score = 0
    while True:
        guess = input("Rock, Scissors or Paper!? but if you wanna quit then type 'quit': ")
        bot_rsp = random.choice(choices)
        print(f"bot select: {bot_rsp}")
        if guess == bot_rsp:
            print("It's a draw!")
        elif guess == "rock" and bot_rsp == "scissors":
            print("You win!")
            user_score = user_score +1
        elif guess == "rock" and bot_rsp == "paper":
            print("You lose!")
            bot_score = bot_score +1
        elif guess == "scissors" and bot_rsp == "rock":
            print("You lose!")
            bot_score = bot_score +1
        elif guess == "scissors" and bot_rsp == "paper":
            print("You lose!")
            user_score = user_score +1
        elif guess == "paper" and bot_rsp == "rock":
            print("You win!")
            user_score = user_score +1
        elif guess =="paper" and bot_rsp == "scissors":
            print("You lose!")
            bot_score = bot_score+1
        if guess == "quit":
            print(f"bot score = {bot_score}")
            print(f"user score = {user_score}")
            if user_score > bot_score: print("You WIN!")
            else: print("You lose! Try again next time :(")
            print("see you next time!")
            break
        else:
            print("next turn!")

rsp()
