import os
import shutil
#https://linuxize.com/post/python-delete-files-and-directories/

import winshell
#https://github.com/tjguk/winshell
# must also install pypiwin32 (pip install winshell and pip install pypwin32)


print("""
Willkommen im Windows Cache CLEANER

Version 1.1

Nutzung auf eigene Gefahr, keine Haftung fuer Schaeden oder Datenverlust.
""")


def user_start_question():
    user_input_start = input("Willst du deinen Windows Cache bereinigen?(y/n):  ")

    if user_input_start == "y":
        clean_process()
    elif user_input_start == "n":
        print("Vorgang wurde abgebrochen")
        user_start_question()
    else:
        print("Befehl leider nicht verstanden")
        user_start_question()


#Delete file to make more space and speedup windows
def clean_process():
    print("Process startet ...")

    # TEMP Ordner wird Lokalisiert und alle Dateien darin geloescht
    #
    def delete_temp_files():
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

    # Papierkorb wird gelert mittels winshell
    #
    def delete_trash_bin():
        try:
            winshell.recycle_bin().empty(confirm=False, show_progress=False, sound=False)
        except Exception as err:
            print(err)

    # WINDOWS.OLD Folder wird gelert mittels winshell
    #
    def delete_windows_old():
        temp_file_location = '/Windows.old'

        # Rechte werden angepasst das Python Script die meisten Dateien Loeschen kann
        try:
            os.chmod(temp_file_location, 0o777)
        except OSError as err:
            print(f"Fehler beim anpassen der Rechte: {err}")

        # Inhalt aus temp ordner wird ausgelesen, wenn ordner dann wir mit shutil.rmtree dieser entfernt.
        try:
            shutil.rmtree(temp_file_location)
        except OSError as err:
            print(f"{temp_file_location} konnte nicht entfernt werden da: {err}")


    delete_temp_files()
    delete_trash_bin()
    delete_windows_old()
    input("Process abgeschlossen")



user_start_question()