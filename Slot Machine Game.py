#Robert
#slots

#init
import random
#functions
def slots():
    credits = 200
    print("Welcome to the Slot Machine!")
    print("You have", (credits), "credits.", "Each spin costs 10 credits.")
    print("Slot Machine Symbols: 💖, 💝, ❤, 7")
    while True:
        try:
            if credits < 10:
                raise ValueError("Not enough credits to spin.")

            spin = input("Spin the slots? (Y/N): ").upper()
            if spin not in ["Y", "N"]:
                raise ValueError("Invalid input. Please enter Y or N.")
            if spin == "N":
                print("Final Credits:", (credits))
                print("Have a good day!")
                break
            credits -= 10
            print("You now have", credits, "credits")
            print("Spinning...")
            symbol1 = random.choice(["[💖]", "[❤]", "[💝]", "[7]"])
            symbol2 = random.choice(["[💖]", "[❤]", "[💝]", "[7]"])
            symbol3 = random.choice(["[💖]", "[❤]", "[💝]", "[7]"])
            print("Current Slots:", (symbol1), (symbol2), (symbol3))
            if symbol1 == symbol2 == symbol3:
                if symbol1 == "[7]":
                    credits += 500
                    print("JACKPOT!!! You won 500 credits!")
                else:
                    credits += 50
                    print("Congratulations, you won 50 credits!")
            else:
                 print("Sorry, you lost.")
            print("Casino Profit:", 200-credits)
        except ValueError as e:
            print("Error:", e)
            if credits < 10:
                print("Better luck next time!")
                break

slots()
