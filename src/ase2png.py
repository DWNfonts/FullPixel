import os
for i in os.listdir("..\\design"):
    if i.endswith(".ase"):
        os.system("..\\aseprite\\aseprite.exe -b --layer \"字形\" ..\\design\\" + i + " --save-as " + i.replace(".ase", ".png"))