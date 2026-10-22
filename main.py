'''
The core file of the program, handles all processes using functions from utilities.py
'''
import utilities

'''
Main function that prompts the user for inputs and randomized a loadout based on their decisions
Will immediately quit if either of the random functions fail
All choices are validated before they're run
"4" can be typed at any time to quit the program
'''
def main():
    running = True
    while running:
        choice = 0
        while choice != 1 and choice != 2 and choice != 3 and choice != 4:
            try:
                choice = int(input("Please enter a choice from the given options by typing its corresponding number/letter.\n1. Randomize toons only\n2. Randomize trinkets only\n3. Randomize full loadout\n4. Quit program\n"))
            except ValueError:
                print("Please enter a number from 1 to 4")
        if choice == 1:
            try:
                print(f"Chosen toon: {utilities.pick_toon()}")
            except FileNotFoundError:
                print("File \"toons.csv\" could not be opened. Please ensure that it's in the same directory")
        elif choice == 2:
            try:
                print(f"Chosen trinkets: {utilities.pick_trinket()}")
            except FileNotFoundError:
                print("File \"trinkets.csv\" could not be opened. Please ensure that it's in the same directory")
        elif choice == 3:
            try:
                trinket_list = utilities.pick_trinket()
                print(f"Selected {utilities.pick_toon()} with {trinket_list[0]} and {trinket_list[1]}")
            except FileNotFoundError:
                print("One or both files could not be opened. Please ensure that they are in the same directory")
        elif choice == 4:
            running = False
        if running:
            choice = input("Would you like to continue? Type \"y\" if yes or \"n\" if no\n")
            if choice == "n":
                running = False
if __name__ == "__main__":
    main()