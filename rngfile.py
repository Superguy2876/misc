import random
import os
import sys

# given a folder path, open a random file in the folder in the default application
def openRandomFile(folder):
    # get the list of files in the folder
    files = os.listdir(folder)
    # get a random file from the list
    randomFile = random.choice(files)
    # open the file in the default application
    os.startfile(folder + '\\' + randomFile)

if __name__ == "__main__":
    # get the folder path from the command line
    folder = sys.argv[1]
    # check if second argument is passed
    imageNumber = 1
    if len(sys.argv) > 2:
        imageNumber = int(sys.argv[2])
    # call the openRandomFile function a number of times equal to the second command line argument which is optional
    for i in range(imageNumber):
        openRandomFile(folder)  
    

