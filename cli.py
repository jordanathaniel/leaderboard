from models import Leaderboard

lb = Leaderboard()

while True:
    print("\n1. Add Player\n2. Update Score\n3. View Leaderboard\n4. Exit")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter player name: ")
        lb.add_player(name)

    elif choice == "2":
        name = input("Enter player name: ")
        points = int(input("Add points: "))
        lb.update_score(name, points)

    elif choice == "3":
        print("\nLeaderboard:")
        for name, score in lb.get_scores().items():
            print(f"{name}: {score}")

    elif choice == "4":
        break

    else:
        print("Invalid choice")
