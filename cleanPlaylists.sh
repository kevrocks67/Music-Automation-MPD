#!/bin/bash

SHELL=/bin/sh
PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin

if (($# == 0));then
	echo "Proper Usage: ./cleanPlaylists.sh username-in-home-folder"
	echo "Ex: ./cleanPlaylists.sh john"
	exit 1
fi

#Clean Music-Automation folder
rm /home/"$1"/Music-Automation/playlists/*.m3u

#Clean mpd playlist folder
rm /home/"$1"/.config/mpd/playlists/*.m3u

#Clean mpd playlist
mpc clear
./addPlaylistMPD.sh "$1"
