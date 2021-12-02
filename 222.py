import os


def main():
    while keep_going():
        keep_going()

def keep_going():
    dirName = input("Howdy, What's the folder name?\n")
    print("You entered " + dirName)
    if  os.path.exists(dirName):
        os.chdir(dirName)
        os.system('cmd /k "pnputil /a *.inf /subdirs /install"')
    else:    
        print("Director doesnt exist")

    
    answer = input("Do you wish to continue? (Y/y for yes)\n")

    if answer in ("Y","y"):
        print ("You have chosen to continue on")
        return True
    else:
        print ("You have chosen to quit this program")
        


main()
