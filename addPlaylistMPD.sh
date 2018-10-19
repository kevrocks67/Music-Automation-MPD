#!/bin/bash
SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

if (($# == 0));then
	echo "Proper Usage: ./addPlaylistMPD username-in-home-folder"
	echo "Ex: ./addPlaylistMPD john"
	exit 1
fi

#Retrieve information to determine if playlist needs to be added
current="$(mpc|grep pla|cut -d' ' -f 2|cut -c 2-|cut -d'/' -f 1)"
total="$(mpc|grep pla|cut -d' ' -f 2|cut -c 2-|cut -d'/' -f 2)" 

diff=$((total-current))

if ((diff < 6));then

	#Create new playlist
	python3 /home/"$1"/Music-Automation/interpreter.py

	#Add playlist to mpd playlist folder
	list="$(ls -t /home/"$1"/Music-Automation/playlists/*.m3u|head -n1)"
	listNameDir=${list%.*}	
	prefix="/home/"$1"/Music-Automation/playlists/"
	listName=${listNameDir#$prefix}
	cp $list /home/"$1"/.config/mpd/playlists/

	#Update mpd database and play new playlist
	mpc update
	mpc load $listName
fi
mpc play
