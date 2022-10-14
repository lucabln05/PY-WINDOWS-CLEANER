import os
import shutil
#https://linuxize.com/post/python-delete-files-and-directories/

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

#TEMP Ordner wird Lokalisiert und alle Dateien darin geloescht

def cache_clean_process():
    print("Process startet ...")

    temp_file_location = os.getenv('temp')  #Temp Ordner wir mit hilfe os.gentev gesucht

    # Rechte werden angepasst das Python Script die meisten Dateien Loeschen kann
    try:
        os.chmod(temp_file_location, 0o777)
    except OSError as err:
        print(f"Fehler beim anpassen der Rechte: {err}")


    #Inhalt aus temp ordner wird ausgelesen, wenn ordner dann wir mit shutil.rmtree dieser entfernt.
    for dir_ in os.scandir(temp_file_location):
        if dir_.is_dir():
            try:
                shutil.rmtree(dir_.path)
            except OSError as err:
                print(f"{dir_.path} konnte nicht entfernt werden da: {err}")

    # Inhalt aus temp ordner werden ausgelese, wenn datei dann wird mit os.remove datei geloescht.
    for file in os.listdir(temp_file_location):
        try:
            os.remove(os.path.join(temp_file_location, file))
        except PermissionError as err:
            print(f"{file} konnte nicht entfernt werden da: {err}")



user_start_question()