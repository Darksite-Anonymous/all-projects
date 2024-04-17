import os
print(f"hey there you're in,")
askquestiontomkdir = input("do you want to make folder y/n:")
if askquestiontomkdir == "y" or askquestiontomkdir == "Y":
    foldername1 = input("name the folder you want to make:")
    os.mkdir(f"{foldername1}")
    limitmkfolder = input("do you want make folder more than one y/n:")
    if (limitmkfolder == "y" or limitmkfolder == "Y"):
        print(
            f"note: your if your want to make {foldername1} more than to of same name it's not possible, it's possible when adding a numerical at the last of our {foldername1}")
        foldername1amount = int(input(f"how many {foldername1}you want to make:"))
        for i in range(foldername1amount):
            if (not os.path.exists(f"{foldername1}")):
                os.mkdir(f"{foldername1}{i + 1}")
    else:
        print("ok continue....")
else:
    print("ok continue.../")
rmfolderquestion = input("do you want to remove folder y/n:")
if rmfolderquestion == "y" or rmfolderquestion == "Y":
    howmanyrmfolderquestion = int(input("how much times you want to remove folder:"))
    for i in range(howmanyrmfolderquestion):
        nameofrmfolder = input("name the directory you want to remove:")
        os.rmdir(f"{nameofrmfolder}")
else:
    print("ok your program is over:")
