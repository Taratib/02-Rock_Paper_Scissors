# Main routine more efficent than v2

# Checks for the a number that is more then zero
def check_rounds():
    while True:
        print()
        response = input("How many rounds: ")
    
        round_error = "Please type either <enter> or an integer that is more than 0"
        
        
        if response != "":
            try:
                response = int(response)

                if response < 1:
                    print(round_error)
                    continue
            
            except ValueError:
                print(round_error)
                continue
    
        return response

# Main routine goes here

rounds_played = 0
choose_instruction = "Please choose rock (r), paper (p) or scissorrs (s)"


# Ask user for # of rounds, <enter> for infinite mode
rounds = check_rounds()

end_game = "no"
while end_game == "no":

    # Start of the Game Play Loop

    # Rounds Heading
    print()
    if rounds == "":
        heading = "Continuous Mode: Round {}".format(rounds_played + 1)

    else:
        heading = "Round {} of {}".format(rounds_played + 1, rounds)
    
    print(heading)
    choose = input("{} or 'xxx' to end: ".format(choose_instruction))
    
    # End game if exit code is typed
    if choose == "xxx":
        break
    
    # **** rest of loop / game *****
    print("You chose {}".format(choose))

    rounds_played += 1 

    # end game if requested # of rounds has been played 
    if rounds_played == rounds:
        break


# Put end game content here
print("Thank you for playing")
