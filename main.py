
print("""
Willkommen im Windows Cache CLEANER

Version 1.0

Nutzung auf eigene Gefahr, keine Haftung fuer Schaeden oder Datenverlust.
""")

def user_start_question():
    user_input_start = input("Willst du deinen Windows Cache bereinigen?(y/n):  ")

    if user_input_start == "y":
        print("START")
    elif user_input_start == "n":
        print("Vorgang wurde abgebrochen")
        user_start_question()
    else:
        print("Befehl leider nicht verstanden")
        user_start_question()
