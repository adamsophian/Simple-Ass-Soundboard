import os
from playsound3 import playsound
import readchar
soundDir=f"{os.path.abspath(os.path.dirname(__file__))}\\Sounds"
sounds=os.listdir(soundDir)

def soundList(): # function to print lists of sounds detected in "".\Sounds"
    listNum=(0)
    print("Available sounds:")
    for file in sounds:
        if file.endswith(".mp3") or file.endswith(".wav"):
            listNum=(listNum+1)
            print(listNum, ":", file)
    return listNum 

list=[]
for file in sounds:
    if file.endswith(".mp3") or file.endswith(".wav"):
        list.append(file)

os.system('cls' if os.name == 'nt' else 'clear')

if not list: # cheks if sounds folder is empty
    print("'Sounds' folder is currently empty! Add audio files to continue")
    print("Press Any Key To Exit")
    readchar.readchar()

else:
    while True: # the main code
        soundTotal=soundList()
        print("Play sound 1 -", soundTotal, "(0 to quit):")
        option=int(input())
        if option == 0:
            print("Thank you for using SASS!")
            break
        elif option > soundTotal or option < 1:
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Option", option, "does not exist. Try another option.")
        else:
            os.system('cls' if os.name == 'nt' else 'clear')
            soundOption=list[option-1]
            print("Playing ",soundOption)
            playsound(f"{soundDir}\\{soundOption}")
            os.system('cls' if os.name == 'nt' else 'clear')