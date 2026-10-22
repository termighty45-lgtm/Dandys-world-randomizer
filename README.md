# Loadout randomizer for Dandy's World

### Purpose

This program allows users to randomize a complete or partial loadout for themselves

---
### Components

- main.py
    
    The primary program file that contains everything needed to generate a random loadout
- utilities.py

    Contains all the useful functions used by main.py and doesn't run anything by itself
- toons.csv

    Maintains a list of toons that is used by the program
- trinkets.csv

    Maintains a list of trinkets that is used by the program

---
# Instructions for use

### Prerequisites

- This program requires python to be installed in order to run
- Install and extract the files from the zip archive instead of downloading them individually

---
### General usage

- Double-click on main.py or activate it through the terminal to get started
- The program contains instructions that walk you through how to use it 
- All choices are validated so it won't crash during runtime
- The program can be quit by typing 4 during the primary loop or typing "n" after an operation has concluded

---
### Editing files

- The two .csv files can be edited to remove toons or trinkets that you don't own
- This is most easily accomplished by opening a text editor
- Before running the program again, ensure that every value has no spaces between them and are separated by only a single comma

---
### Troubleshooting

- The functions will fail if toons.csv or trinkets.csv can not be found, always make sure they're kept in the same folder as main.py and utilities.py
- If the .csv files are edited incorrectly, the program will crash while trying to read them 
- If all else fails, redownload and replace the .csv files from the GitHub repo directly