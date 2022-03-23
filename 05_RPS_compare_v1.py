# RPS Component 3 - Compare user choice and computer choice
rps_list = ["rock", "paper", "scissors"]
comp_index = 0
for item in rps_list:
    user_index = 0
    for item in rps_list:
        user_choice = rps_list[user_index]
        comp_choice = rps_list[comp_index]
        user_index += 1

        # Compare options....
        print()
        if user_choice == "rock" and comp_choice == "rock":
            results = "It's a Tie"
        elif user_choice == "paper" and comp_choice == "paper":
            results = "It's a Tie"
        elif user_choice == "scissors" and comp_choice == "scissors":
            results = "It's a Tie"
        elif user_choice == "rock" and comp_choice == "scissors":
            results = "You Won!"
        elif user_choice == "paper" and comp_choice == "rock":
            results = "You Won!"
        elif user_choice == "scissors" and comp_choice == "paper":
            results = "You Won!"
        elif user_choice == "scissors" and comp_choice == "rock":
            results = "You lost (better luck next time)"
        elif user_choice == "rock" and comp_choice == "paper":
            results = "You lost (better luck next time)"
        elif user_choice == "paper" and comp_choice == "scissors":
            results = "You lost (better luck next time)"
        
        print("You chose {}, the computer chose {}. \nResult: {}".format(user_choice, comp_choice, results))

    comp_index += 1
    print()
    if user_choice == "rock" and comp_choice == "rock":
            results = "It's a Tie"
    elif user_choice == "paper" and comp_choice == "paper":
        results = "It's a Tie"
    elif user_choice == "scissors" and comp_choice == "scissors":
        results = "It's a Tie"
    elif user_choice == "rock" and comp_choice == "scissors":
        results = "You Won!"
    elif user_choice == "paper" and comp_choice == "rock":
        results = "You Won!"
    elif user_choice == "scissors" and comp_choice == "paper":
        results = "You Won!"
    elif user_choice == "scissors" and comp_choice == "rock":
        results = "You lost (better luck next time)"
    elif user_choice == "rock" and comp_choice == "paper":
        results = "You lost (better luck next time)"
    elif user_choice == "paper" and comp_choice == "scissors":
        results = "You lost (better luck next time)"
    
            
    