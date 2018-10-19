import os

user = input("Name of user in home folder of music: ")
musicDir = "/home/"+user+"/Music"

print("Music Directory set to: "+musicDir)

rotFileName = input("What would you like to call the rotation file?: ")
rotFile = open(rotFileName,"w")
rotFile.close()

for genre in os.listdir(musicDir):
    print(genre) 

def addGenre():
    toAdd = input("Pick a genre to add to rotation: ")
    numToAdd = input("How many of this genre to add?: ")
    
    with open(rotFileName,'a') as r:
        r.write((toAdd+'\n')*int(numToAdd))
    print("Added {0} of genre: {1} to rotation".
            format(numToAdd, toAdd))

while True:
    response = input("Add genre?(y/n)")
    if response.lower() == 'y':
        addGenre()
    else:
        break
    
print("Rotation file {0} created".format(rotFile))

