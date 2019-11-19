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
                                #3
#turn string to list and then add word at spot and then back to string
def UpdateString(string, NewChar, index):
    output = ''
    string = list(string)
    string.insert(index, NewChar)
    string.pop(index+1)
    for x in range(len(string)):
        output += string[x]
    return PrintOutput(output)
