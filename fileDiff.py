import os
import sys



# take two folders as input and compare the files in them returning a list of files that are in only one of the folders
def compareFolders(folder1, folder2):
    # get the list of files in each folder as a set
    files1 = set(os.listdir(folder1))
    files2 = set(os.listdir(folder2))
    # create a list of files that are in only one of the folders
    filesOnlyInOneFolder = []
    # loop through the files in the first folder
    for file in files1:
        # if the file is not in the second folder add it to the list
        if file not in files2:
            filesOnlyInOneFolder.append(file)
    # loop through the files in the second folder
    for file in files2:
        # if the file is not in the first folder add it to the list
        if file not in files1:
            filesOnlyInOneFolder.append(file)
    # return the list of files that are in only one of the folders
    return filesOnlyInOneFolder

# given a list of files and a two folders, return a list of files that are in both folders, copying the files from the first folder to the second folder
# if the file does not exist in the first folder skip it
# check for windows and linux and use correct copy command
def copyFiles(files, folder1, folder2):
    # see if the file is in the first folder
    files1 = set(os.listdir(folder1))
    # create second folder if it does not exist
    if not os.path.exists(folder2):
        os.makedirs(folder2)

    for file in files:
        if file in files1:
            # copy the file from the first folder to the second folder
            if sys.platform == 'win32':
                os.system('copy ' + folder1 + '\\' + file + ' ' + folder2)
            elif sys.platform == 'linux':
                os.system('cp ' + folder + '/' + file + ' ' + folder2)

    

    
if __name__ == "__main__":
    # get the folder paths from the command line
    folder1 = sys.argv[1]
    folder2 = sys.argv[2]
    # call the compareFolders function
    filesOnlyInOneFolder = compareFolders(folder1, folder2)
    # print the list of files that are in only one of the folders
    print(filesOnlyInOneFolder)

    localFolderName = sys.argv[3]

    # call the copyFiles function
    copyFiles(filesOnlyInOneFolder, folder1, localFolderName + 'folder1')
    copyFiles(filesOnlyInOneFolder, folder2, localFolderName + 'folder2')