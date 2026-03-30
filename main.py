import os
from playsound3 import playsound

def soundList():
    listNum=(0)
    print("Available sounds:")
    for file in os.listdir(r"C:\Users\Adam S\SynologyDrive\03 Personal\02 Projects\random ass soundboard\Sounds"):
        if file.endswith(".mp3"):
            listNum=(listNum+1)
            print(listNum, ":", file)
    return listNum 

total=soundList()
list=[]
for file in os.listdir(r"C:\Users\Adam S\SynologyDrive\03 Personal\02 Projects\random ass soundboard\Sounds"):
        if file.endswith(".mp3"):
            list.append(file)
print(list)

while True:
    print("Play sound 1 -", total, "(0 to quit):")
    option=int(input())
    if not option == 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        soundOption=list[option-1]
        print("Playing ",soundOption)
        playsound(f".\Sounds\{soundOption}")
        os.system('cls' if os.name == 'nt' else 'clear')
        soundList()
    else:
        break