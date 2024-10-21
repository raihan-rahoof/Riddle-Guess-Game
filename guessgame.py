import random
import time
from abc import ABC, abstractmethod


class Riddle:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


class RiddleRepository:
    def __init__(self):
        self.riddles = [
            Riddle(
                "I speak without a mouth and hear without ears. I have no body, but I come alive with wind. What am I?",
                "echo",
            ),
            Riddle(
                "What has keys, but no locks; space, but no room; you can enter, but not go in?",
                "keyboard",
            ),
            Riddle(
                "The more you take, the more you leave behind. What am I?", "footsteps"
            ),
            Riddle(
                "What comes once in a minute, twice in a moment, but never in a thousand years?",
                "m",
            ),
            Riddle(
                "I have cities, but no houses. I have mountains, but no trees. I have water, but no fish. What am I?",
                "map",
            ),
        ]

    def get_random_riddle(self):
        return random.choice(self.riddles)


class Weapon:
    def __init__(self, name):
        self.name = name


class WeaponRepository:
    def __init__(self):
        self.weapons = [
            Weapon("Sword"),
            Weapon("Bow"),
            Weapon("Axe"),
            Weapon("Spear"),
            Weapon("Dagger"),
        ]

    def get_random_weapons(self, count):
        return random.sample(self.weapons, count)


class Key:
    def __init__(self, name):
        self.name = name


class KeyRepository:
    def __init__(self):
        self.keys = [Key("Golden Key"), Key("Silver Key"), Key("Bronze Key")]

    def get_random_keys(self, count):
        return random.sample(self.keys, count)


class Level(ABC):
    @abstractmethod
    def play(self):
        pass


class LevelOne(Level):
    def __init__(self, riddle_repo, weapon_repo, key_repo):
        self.riddle_repo = riddle_repo
        self.weapon_repo = weapon_repo
        self.key_repo = key_repo
        self.lives = 3

    def play(self):
        print("\nWelcome to Level 1!")
        print(f"You have {self.lives} lives.")

        while self.lives > 0:
            if self.answer_riddle() and self.pick_weapon() and self.open_door():
                print("Congratulations! You've completed Level 1!")
                return True
            self.lives -= 1
            print(f"You lost a life. Remaining lives: {self.lives}")

        print("Game Over. You've run out of lives.")
        return False

    def answer_riddle(self):
        riddle = self.riddle_repo.get_random_riddle()
        print("\nSolve this riddle:")
        print(riddle.question)

        for _ in range(3):  # Give the player 3 attempts
            answer = input("Your answer: ").lower().strip()
            if answer == riddle.answer:
                print("Correct! You've solved the riddle.")
                return True
            print("Incorrect. Try again.")

        print(f"Sorry, you couldn't solve the riddle. The answer was: {riddle.answer}")
        return False

    def pick_weapon(self):
        weapons = self.weapon_repo.get_random_weapons(3)
        print("\nChoose a weapon:")
        for i, weapon in enumerate(weapons, 1):
            print(f"{i}. {weapon.name}")

        while True:
            try:
                choice = int(input("Enter the number of your chosen weapon: "))
                if 1 <= choice <= 3:
                    print(f"You've chosen the {weapons[choice-1].name}.")
                    return True
                print("Invalid choice. Please choose a number between 1 and 3.")
            except ValueError:
                print("Please enter a valid number.")

    def open_door(self):
        keys = self.key_repo.get_random_keys(3)
        correct_key = random.choice(keys)

        print("\nChoose a key to open the door:")
        for i, key in enumerate(keys, 1):
            print(f"{i}. {key.name}")

        while True:
            try:
                choice = int(input("Enter the number of your chosen key: "))
                if 1 <= choice <= 3:
                    if keys[choice - 1] == correct_key:
                        print("The door opens! You've chosen the correct key.")
                        return True
                    print("Wrong key. The door remains locked.")
                    return False
                print("Invalid choice. Please choose a number between 1 and 3.")
            except ValueError:
                print("Please enter a valid number.")


class LevelTwo(Level):
    def __init__(self, riddle_repo):
        self.riddle_repo = riddle_repo
        self.lives = 0

    def play(self):
        print("\nWelcome to Level 2!")

        while self.lives < 3:
            self.add_life()
            print(f"Current lives: {self.lives}")

            if not self.fight_villain():
                continue

            if self.answer_riddle():
                print("Congratulations! You've completed Level 2 and won the game!")
                return True

        print("Game Over. You couldn't complete Level 2.")
        return False

    def add_life(self):
        self.lives += 1
        print("You gained a life!")

    def fight_villain(self):
        weapons = ["Sword", "Bow", "Axe", "Spear", "Dagger"]
        villain_weakness = random.choice(weapons)

        print("\nA villain appears! Choose your weapon wisely:")
        for i, weapon in enumerate(weapons, 1):
            print(f"{i}. {weapon}")

        while True:
            try:
                choice = int(input("Enter the number of your chosen weapon: "))
                if 1 <= choice <= len(weapons):
                    chosen_weapon = weapons[choice - 1]
                    if chosen_weapon == villain_weakness:
                        print(
                            f"The {chosen_weapon} was super effective! You defeated the villain."
                        )
                        return True
                    print(f"The {chosen_weapon} wasn't effective. The villain escapes.")
                    return False
                print(
                    f"Invalid choice. Please choose a number between 1 and {len(weapons)}."
                )
            except ValueError:
                print("Please enter a valid number.")

    def answer_riddle(self):
        riddle = self.riddle_repo.get_random_riddle()
        print("\nSolve this final riddle:")
        print(riddle.question)

        answer = input("Your answer: ").lower().strip()
        if answer == riddle.answer:
            print("Correct! You've solved the final riddle.")
            return True
        print(f"Incorrect. The answer was: {riddle.answer}")
        return False


class Game:
    def __init__(self):
        riddle_repo = RiddleRepository()
        weapon_repo = WeaponRepository()
        key_repo = KeyRepository()
        self.level_one = LevelOne(riddle_repo, weapon_repo, key_repo)
        self.level_two = LevelTwo(riddle_repo)

    def play(self):
        print("Welcome to the Adventure Game!")
        input("Press Enter to start...")

        if self.level_one.play():
            time.sleep(1)  # Pause for dramatic effect
            self.level_two.play()

        print("\nThanks for playing!")


if __name__ == "__main__":
    game = Game()
    game.play()

