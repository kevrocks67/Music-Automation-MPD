# Music Rotation & Automation Project
This project is a series of bash and python scripts used to rotate music in MPD
from a large collection of music based on genre.

## Dependencies
- MPD already setup
- MPC
- python 3

## Installation
1. Clone this project to the /home/$USER/ folder
2. Arrange your music by genre in folders within the /home/$USER/Music directory.
   The folder names should be the genre of the music within it
3. Run "python createRotation.py" within the Music-Automation folder and follow the prompts.
   This will generate a file defining the quantity of each genre the program will select and
   when it will select them. This list will loop while the music automation program is running.
   The rotation file can also be edited manually since its just a list of genres seperated by
   a new line.
4. Move 'addPlaylistMPD.sh' and 'cleanPlaylists.sh' to /etc/cron.d
5. Edit your crontab to run addPlaylistMPD.sh at a predefined time. This script
   will run the interpreter.py script in the Music-Automation folder. I personally use 40 minutes
   based on the amount of songs I have in my rotation file. This is my entry below.
   
   		40 \*	\*\*\*	kevin	/bin/bash /etc/cron.d/addPlaylistMPD.sh \>/dev/null 2>&1

6. Add another crontab entry for cleanPlaylists.sh. Have this one run once a week so that
   you dont keep old playlists the script creates. I like to have mine run at midnight sunday.

		\* 0	\*\*\*	kevin	/bin/bash /etc/cron.d/cleanPlaylists.sh \>/dev/null 2>&1

7. Test it out and make adjustments as needed to the crontab timing for addPlaylistMPD.sh.

8. (Optional) Start the mpcGUI.py program if you want a simple interface for playing, pausing
   or moving to the next or previous track. 

