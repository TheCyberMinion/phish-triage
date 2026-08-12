import sys

# gets the file path, does a .eml check and sends it out    
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
def getContentFromFile():
    filePath = getFilePath()
    try:
        with open(filePath, 'rb') as file:
            return file.read()
    except OSError as error:
        sys.exit(f'Could Not Read The File: {error}')