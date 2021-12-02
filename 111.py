import os


def main():
    while keep_goingfolder():
        keep_goingfolder()

def keep_goingfolder():
    dirName = input("Howdy, What's the folder name?\n")
    print("You entered " + dirName)
    if not os.path.exists(dirName):
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created \n")
    else:    
        print("Directory " , dirName ,  " already exists\n")

    os.chdir(dirName)
    os.system('cmd /k "pnputil /export-driver * ."')
    answer = input("Do you wish to continue? (Y/y for yes)\n")

    if answer in ("Y","y"):
        print ("You have chosen to continue on")
        return True
    else:
        print ("You have chosen to quit this program")
        


main()
