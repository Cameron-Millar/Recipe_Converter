import json

textName = input('Enter file name:')
jsonName = textName.split('.', 1)[0]+'.json'

with open(textName, encoding="latin-1") as inputFile:
    contents = inputFile.read()
    if (idx := contents.find('{')) >=0:
        d = json.loads(contents[idx:])
        with open(jsonName, 'w') as jout:
            json.dump(d,jout,indent=4)