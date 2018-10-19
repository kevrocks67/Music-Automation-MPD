import datetime
import glob
import os
import random


musicDir=" "
rotFile=" "
genreDir=" "
timestamp = datetime.datetime.now().strftime("%Y_%m_%d-%H_%M")
playlistName = timestamp + '.'+"m3u"
chosenSongs = []

user = input("Username from home folder of music dir: ")
rotFile = input("Rotation file name: ")

musicDir = "/home/"+user+"/Music"
rotFile = "/home/"+user+"/Music-Automation/"+rotFile

print("Music directory set to: "+musicDir)
print("Rotation File set to: "+rotFile)

def pickSong(genre):
    genreDirName = musicDir+'/'+genre
    genreDir = genreDirName.strip()
    filetypes = ['mp3','flac','wav','aac']
    songList = []

    for(dirpath, dirnames, filenames) in os.walk(genreDir, followlinks=True):
        for name in filenames:
            if(name[-3:] in filetypes):
                songList.append(os.path.join(dirpath,name))
            elif(name[-4:] in filetypes):
                songList.append(os.path.join(dirpath,name))

    song = random.choice(songList)
    if(song not in chosenSongs):
        chosenSongs.append(song)
    else:
        while(song in chosenSongs):
            song = random.choice(songList)
    
    addToPlaylist(song)

def addToPlaylist(song):
    playlist = "/home/"+user+"/Music-Automation/playlists/"+playlistName
    with open(playlist,'a') as p:
        p.write(song+'\n')


with open(rotFile) as r:
    for genre in r:
        song = pickSong(genre)
    
