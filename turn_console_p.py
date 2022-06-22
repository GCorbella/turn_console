from turn_console_g import *

cosmetics_n = decorator(cosmetics)
perfumery_n = decorator(perfumery)
pharmacy_n = decorator(pharmacy)

def home():
    while True:
        print("Welcome to Pyhton Drugstore. You need a number to be attended.")
        selection = input("""Select one: 
        [C] - Cosmetics
        [P] - Perfumery
        [Ph] - Pharmacy
        """).upper()
        print("*" * 50)
        if selection == "C":
            cosmetics_n()
        elif selection == "P":
            perfumery_n()
        elif selection == "PH":
            pharmacy_n()
        else:
            print("Wrong selection. Please, enter a valid option.")
        print("*" * 50)

home()

