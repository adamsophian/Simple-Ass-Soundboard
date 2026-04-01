import os
from playsound3 import playsound
soundDir=f"{os.path.abspath(os.path.dirname(__file__))}\\Sounds"
sounds=os.listdir(soundDir)

def soundList(): # function to print lists of sounds detected in "".\Sounds"
    listNum=(0)
    print("Available sounds:")
    for file in sounds:
        if file.endswith(".mp3"):
            listNum=(listNum+1)
            print(listNum, ":", file)
    return listNum 

list=[]
for file in sounds:
        if file.endswith(".mp3"):
            list.append(file)

os.system('cls' if os.name == 'nt' else 'clear')
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