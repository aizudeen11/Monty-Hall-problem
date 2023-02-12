import random

def prob(n):
    i = 0
    change_win = 0
    change_lose = 0
    while i != n:
        lists = ["goat", "goat", "car"]
        random.shuffle(lists)
        x = random.randint(0,2)
        pick = lists[x]
        lists.remove(pick)
        lists.remove("goat")
        if lists == ["car"]:
            change_win += 1
        else:
            change_lose += 1
        i += 1
    print(f"if player change door, the player has {change_win/n*100}% to win")
    print(f"while player has {change_lose/n*100}% chance to lose")

prob(1000)