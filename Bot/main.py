import os
from shutil import rmtree

def download_anime():
    anime = input("Enter the name of the anime you want to download: ")
    os.system("python -m animdl download "+ anime) 
    return 0

def download_familyguy():
    pass

def download_simpsons():
    pass

def split_up():
    pass

def upload():
    pass

def new_file():
    if os.path.exists("content"): rmtree("content") 
    os.mkdir("content")

if __name__ == "__main__":
    choice = input("(A)nime, (F)amily Guy, (S)impsons \n:").upper()
    match input:
        case "A":
            new_file()
            download_anime()
            split_up()
            upload()
        case "F":
            new_file()
            download_familyguy()
            split_up()
            upload()
        case "S":
            new_file()
            download_simpsons()
            split_up()
            upload()
        case _:
            print("Invalid Input Type")
            exit