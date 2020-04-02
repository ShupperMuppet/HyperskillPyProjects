class Needs:
    def __init__(self, money, water, milk, beans):
        self.money = money
        self.water = water
        self.milk = milk
        self.beans = beans


class CoffeeMachine:

    def __init__(self):
        self.espresso = Needs(4, 250, 0, 16)
        self.latte = Needs(7, 350, 75, 20)
        self.cappuccino = Needs(6, 200, 100, 12)
        self.money = 550
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.disposableCups = 9
        self.missing = None

    def make_it(self, want):
        self.money += want.money
        self.water -= want.water
        self.milk -= want.milk
        self.beans -= want.beans
        self.disposableCups -= 1

    def have_enough(self, check):
        if not (self.water >= check.water):
            self.missing = "water"
            return False
        elif not (self.milk >= check.water):
            self.missing = "milk"
            return False
        elif not (self.beans >= check.beans):
            self.missing = "coffee beans"
            return False
        elif not (self.disposableCups > 0):
            self.missing = "disposable cups"
            return False
        else:
            return True

    def run(self):
        while True:
            print("Write action (buy, fill, take, remaining, exit):")
            action = input()

            if action == "buy":
                print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
                option = input()
                if option == "1":
                    if self.have_enough(self.espresso):
                        print()
                        self.make_it(self.espresso)
                        print("I have enough resources, making you a coffee!\n")
                        continue
                    else:
                        print(f"Sorry, not enough {self.missing}!\n")

                elif option == "2":
                    if self.have_enough(self.latte):
                        print()
                        self.make_it(self.latte)
                        print("I have enough resources, making you a coffee!\n")
                        continue
                    else:
                        print(f"Sorry, not enough {self.missing}!\n")

                elif option == "3":
                    if self.have_enough(self.cappuccino):
                        print()
                        self.make_it(self.cappuccino)
                        print("I have enough resources, making you a coffee!\n")
                        continue
                    else:
                        print(f"Sorry, not enough {self.missing}!\n")
                else:
                    continue

            elif action == "fill":
                self.water += int(input("Write how many ml of water do you want to add:\n"))
                self.milk += int(input("Write how many ml of milk do you want to add:\n"))
                self.beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
                self.disposableCups += int(input("Write how many disposable cups of coffee do you want to add:\n"))

            elif action == "take":
                print(f"I gave you ${self.money}\n")
                self.money = 0

            elif action == "remaining":
                print(f"\nThe coffee machine has:\n{self.water} of water\n{self.milk} of milk")
                print(f"{self.beans} of coffee beans\n{self.disposableCups} of disposable cups\n{self.money} of money")
                continue

            elif action == "exit":
                break


coffee = CoffeeMachine()
coffee.run()
