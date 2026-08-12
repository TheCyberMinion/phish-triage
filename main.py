import sys

def main():
    filePath = getFilePath()
    fileContent = getContentFromFile(filePath) #assign the content of .eml to file variable
    print(fileContent)

# gets the file path and sends it out
def getFilePath():
    if len(sys.argv) < 2:
        sys.exit('File Path Not Provided')
    elif len(sys.argv) == 2:
        #strips sidespaces and optional ' or " if they exist and returns the value
        return (sys.argv[1]).strip().strip("'\"")
    else:
        sys.exit('Too Many Arguments Provided')


# this gets the content of the .eml file if it exist
# otherwise exits with a message if the file does not exist
# or if the file path is invalid
def getContentFromFile(filePath):
    try:
        with open(filePath) as file:
            return file.read()
    except OSError:
        sys.exit('File Does Not Exist')

if __name__ == '__main__':
    main()