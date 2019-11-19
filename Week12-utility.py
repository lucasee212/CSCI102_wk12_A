        #   YOUR GITHUB REPO #https://github.com/lucasee212/CSCI102_wk12_A.git
        #   Lucas Emery
        #   ​CSCI 102 – Section A
        #   Week 12 - Part A
                                #1
#simple print word
def PrintOutput(word):
    return print('OUTPUT %s' %word)
                                #2
#function that calls file and reads the file
def LoadFile(file):
    openFile = open(file, 'r')
    readFile = openFile.read()
    openFile.close()
    return readFile
