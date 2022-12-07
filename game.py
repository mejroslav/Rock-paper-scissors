import random
import time

# color sequences
reset = '\033[0m'
bold = '\033[01m'
blue = '\033[34m'
red = '\033[31m'
green = '\033[32m'
orange = '\033[33m'

slovnik_znaku = {
    "kámen": "kámen",
    "nůžky": "nůžky",
    "papír": "papír",
    "rock": "kámen",
    "scissors": "nůžky",
    "paper": "papír"
}

slovnik_hodnot = {
    "undefined": 0,
    "kámen": 1,
    "nůžky": 2,
    "papír": 3
}

class Znak:
    def __init__(self):
        self.type = ""
        self.num = 0
        self.score = 0

    def update(self, name):
        self.type = slovnik_znaku[name] if name in slovnik_znaku else "undefined"
        self.num = slovnik_hodnot[self.type]

    def __str__(self) -> str:
        return(f"Objekt třídy Znak typu {self.type}.")
    
    def __eq__(self,other):
        return self.type == other.type

    def __lt__(self,other):
        return True if (self.num == 3 and other.num == 2) or (self.num == 2 and other.num == 1) or (self.num == 1 and other.num == 3) else False

def game_result(player: Znak, opponent: Znak):
    if player < opponent:
        print("Prohra!")
        opponent.score += 1
    elif player == opponent:
        print("Remíza!")
        player.score += 0.5
        opponent.score += 0.5
    elif opponent < player:
        print("Výhra")
        player.score += 1
    else:
        print("Zadal jsi neplatný znak. Povolené znaky: kámen(rock), nůžky(scissors), papír(paper)")

def print_intro():
    print(blue + """
 ___  ___  _  ___  ___  ___  ___  ___         ___  ___  ___  ___  ___         ___  ___  ___  _ __
/ __]|  _]| |/ __]/ __]| . || . \/ __]  ___  | . \| . || . \| __]| . \  ___  | . \| . ||  _]| / /
\__ \| [__| |\__ \\__ \| | ||   /\__ \ |___| |  _/|   ||  _/| _] |   / |___| |   /| | || [__|  \ 
[___/`___/|_|[___/[___/`___'|_\_\[___/       |_|  |_|_||_|  |___]|_\_\       |_\_\`___'`___/|_\_\
                                                                                                 
    """ + reset)
    print("Vítej u klasické hry KÁMEN-NŮŽKY-PAPÍR.")
    print("Povolené znaky: kámen(rock), nůžky(scissors), papír(paper)")


def main():
    print_intro()
    player = Znak()
    opponent = Znak()

    while True:
        p_znak = input("Zadej znak: ").lower()
        player.update(p_znak)
        op_znak = random.choice(("kámen", "nůžky", "papír"))
        opponent.update(op_znak)

        print(f"Počítač zahrál {opponent.type}.")
        game_result(player, opponent)
        print(f"Skóre: hráč: {player.score}, počítač: {opponent.score}")

        while True:
            again = input("Chceš hrát znovu? [a/n] ")
            if again == "a":
                break
            elif again == "n":
                print(f"Finální skóre: hráč: {player.score}, počítač: {opponent.score}")
                exit()

if __name__ == "__main__":
    main()