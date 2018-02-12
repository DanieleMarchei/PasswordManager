import sys
import random
import string

randomChar = None

if len(sys.argv) == 1:
    name = sys.argv
else:
    if len(sys.argv) == 2:
        name, randomChar = sys.argv
    else:
        print "Max 1 parameter (-r) is allowed"
        sys.exit(0)

def generateIndex():
    index = 0
    for i in xrange(5):
        index += random.randint(1,6) * 10**i

    return index

nWords = random.randint(4,6)

password = ""
with open('words.txt') as f:
    for i in xrange(nWords):
        index = generateIndex()
        for line in f:
            if str(index) in line:
                password += line[len(str(index))+1:len(line)-1]
                if i < nWords-1:
                    password += " "
        f.seek(0)

if randomChar != None:
    if randomChar == "-r":
        randomness = random.randint(len(password)/10, len(password)/5)
        changedIndex = []
        for i in xrange(randomness):
            indexChange = random.randint(0, len(password))
            while indexChange in changedIndex:
                indexChange = random.randint(0, len(password))
            
            char = password[indexChange]
            replaceChar = random.choice(string.letters.replace(char, ""))
            passList = list(password)
            passList[indexChange] = replaceChar
            password = ''.join(passList)

        print password
        
    else:
        print randomChar, "command is not valid, use -r to add random characters to the password"
else:
    print password
