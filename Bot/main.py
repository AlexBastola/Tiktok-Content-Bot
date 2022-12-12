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

if __name__ == "__main__":
    choice = input("(A)nime, (F)amily Guy, (S)impsons \n: ").upper()
    match choice:
        case 'A':
            download_anime()
            split_up()
            upload()
        case 'F':
            download_familyguy()
            split_up()
            upload()
        case 'S':
            download_simpsons()
            split_up()
            upload()
        case _:
            print("Invalid Input Type")
            exit