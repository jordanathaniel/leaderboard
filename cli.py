import argparse
from models import Leaderboard

def main():
    parser = argparse.ArgumentParser(description="Leaderboard CLI")
    sub = parser.add_subparsers(dest="cmd")

    add = sub.add_parser("add", help="Add player")
    add.add_argument("name")

    score = sub.add_parser("score", help="Record score")
    score.add_argument("id", type=int)
    score.add_argument("points", type=int)

    show = sub.add_parser("show", help="Show top players")
    show.add_argument("--n", type=int, default=10)

    args = parser.parse_args()
    lb = Leaderboard()

    if args.cmd == "add":
        p = lb.add_player(args.name)
        print(f"Added player {p.id} {p.name} score {p.score}")
    elif args.cmd == "score":
        p = lb.record_score(args.id, args.points)
        print(f"Updated player {p.id} {p.name} score {p.score}")
    elif args.cmd == "show":
        top = lb.list_top(args.n)
        print("Rank ID Name Score")
        for i, p in enumerate(top, start=1):
            print(f"{i:3d} {p.id:3d} {p.name:12s} {p.score}")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
