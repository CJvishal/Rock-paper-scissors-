import random

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['stone', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 'stone' and computer_choice == 'scissors') or \
         (player_choice == 'scissors' and computer_choice == 'paper') or \
         (player_choice == 'paper' and computer_choice == 'stone'):
        return "You win!"
    else:
        return "You lose!"

# Main game function
def stone_paper_scissors():
    print("Welcome to Stone, Paper, Scissors!")
    print("Type 'stone', 'paper', or 'scissors' to play.")
    
    # Get player's choice
    player_choice = input("Enter your choice: ").lower()
    
    if player_choice not in ['stone', 'paper', 'scissors']:
        print("Invalid choice. Please select 'stone', 'paper', or 'scissors'.")
        return
    
    # Get computer's choice
    computer_choice = get_computer_choice()
    
    # Display choices
    print(f"Computer chose: {computer_choice}")
    print(f"You chose: {player_choice}")
    
    # Determine and display the winner
    result = determine_winner(player_choice, computer_choice)
    print(result)

# Call the main game function
stone_paper_scissors()
