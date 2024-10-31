import random


def player():
    rps = 0
    while not rps in [1, 2, 3]:
        rps = int(input("1 for Rock, 2 for Paper, 3 for Scissors: "))
        if not rps in [1, 2, 3]:
            print("ERROR")
    if rps == 1:
        print("You chose Rock")
        return "Rock"
    elif rps == 2:
        print("You chose Paper")
        return "Paper"
    else:
        print("You chose Scissors")
        return "Scissors"


def comp():
    crps = random.randint(1, 3)
    if crps == 1:
        print("The Computer chooses Rock")
        return "Rock"
    elif crps == 2:
        print("The Computer chooses Paper")
        return "Paper"
    else:
        print("The Computer chooses Scissors")
        return "Scissors"


def win(crps, rps):
    if rps == crps:
        return "Tie"
    return "Win" if (rps == 1 and crps == 3) or (rps == 3 and crps == 2) or (rps == 2 and crps == 1) else "Lose"


def main():
    results = []
    for i in range(5):
        rps = player()
        crps = comp()
        result = win(crps, rps)
        results.append((i + 1, rps, crps, result))
    print("#" * 49 + "\n######### Rock, Paper, Scissors Report ##########\n" + "#" * 49)
    print("-------------------------------------------------\n|Round| User Played | Computer Played | Outcome |\n-------------------------------------------------")
    for round_num, rps, crps, result in results:
        print(f"| {round_num:^3} | {rps:^12}|  {
              crps:^14} | {result:^7} |\n-------------------------------------------------")


if __name__ == "__main__":
    main()
