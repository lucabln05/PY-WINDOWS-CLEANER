import os




print("""
Willkommen im Windows Cache CLEANER

Version 1.0

Nutzung auf eigene Gefahr, keine Haftung fuer Schaeden oder Datenverlust.
""")


def user_start_question():
    user_input_start = input("Willst du deinen Windows Cache bereinigen?(y/n):  ")

    if user_input_start == "y":
        cache_clean_process()
    elif user_input_start == "n":
        print("Vorgang wurde abgebrochen")
        user_start_question()
    else:
        print("Befehl leider nicht verstanden")
        user_start_question()

def cache_clean_process():
    print("Process start")
    temp_file_location = os.getenv('temp')
    print(temp_file_location)
    os.chmod(temp_file_location, 0o777)
    dir = temp_file_location


    for file in os.listdir(dir):
        try:
            os.remove(os.path.join(dir, file))
        except PermissionError as err:
            print(f"{file} konnte nicht entfernt werden da: {err}" )











user_start_question()