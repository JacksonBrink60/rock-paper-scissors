import random


def get_player_choice():
    """Get the player's choice with input validation."""
    choice = 0
    while choice not in [1, 2, 3]:
        try:
            choice = int(input("1 for Rock, 2 for Paper, 3 for Scissors: "))
            if choice not in [1, 2, 3]:
                print("ERROR: Please enter a valid choice.")
        except ValueError:
            print("ERROR: Please enter a number.")
    return ["Rock", "Paper", "Scissors"][choice - 1]


def get_computer_choice():
    """Generate the computer's choice."""
    choice = random.choice(["Rock", "Paper", "Scissors"])
    print(f"The Computer chooses {choice}")
    return choice


def determine_winner(player_choice, computer_choice):
    """Determine the outcome of the round."""
    if player_choice == computer_choice:
        return "Tie"
    elif (player_choice == "Rock" and computer_choice == "Scissors") or \
         (player_choice == "Scissors" and computer_choice == "Paper") or \
         (player_choice == "Paper" and computer_choice == "Rock"):
        return "Win"
    else:
        return "Lose"


def display_results(results):
    """Display the summary of all rounds played."""
    print("#" * 49 + "\n######### Rock, Paper, Scissors Report ##########\n" + "#" * 49)
    print("-------------------------------------------------")
    print("|Round| User Played | Computer Played | Outcome |")
    print("-------------------------------------------------")
    for round_num, player, computer, outcome in results:
        print(f"| {round_num:^3} | {player:^12}| {
              computer:^14} | {outcome:^7} |")
        print("-------------------------------------------------")


def main():
    results = []
    for i in range(5):
        player_choice = get_player_choice()
        print(f"You chose {player_choice}")
        computer_choice = get_computer_choice()
        outcome = determine_winner(player_choice, computer_choice)
        results.append((i + 1, player_choice, computer_choice, outcome))
    display_results(results)


if __name__ == "__main__":
    main()
