#####################################
# Author: Kevin Diaz                #
# Version: 1.0                      #
# Date: 06/28/2018                  #
# Use: A simple gui wrapper for MPC #
#####################################

import subprocess
import sys
import threading
import time
import tkinter as tk

#Toggles the play/pause of MPD
def toggle():
    ret = subprocess.check_output("mpc toggle", shell=True).decode()
    retLabel.config(text=str(ret))

#Goes to previous sound track
def prev():
    ret = subprocess.check_output("mpc prev", shell=True).decode()
    retLabel.config(text=str(ret))

#Goes to next sound track
def nextS():
    ret = subprocess.check_output("mpc next", shell=True).decode()
    retLabel.config(text=str(ret))

#Returns status of mpd server
def status():
    mpdConnected = True
    while mpdConnected:
        try:
            ret = subprocess.check_output("mpc status", shell=True).decode()
            retLabel.config(text=str(ret))
            time.sleep(1)
        except:
            #If mpd server is not on, stop asking for status each second
            retLabel.config(text="MPD server not on. Exiting in 5 secs")
            time.sleep(5)
            mpdConnected = False
    
    #If MPD not running, exit application
    root.quit()
    root.destroy()

################### Beginning of Tkinter Code #####################
root = tk.Tk()
root.title("MPC GUI")

#Initialize frame for buttons
frame = tk.Frame(root)
frame.pack()

#Initialize frame for label
res = tk.Frame(root)
res.pack()

#Initializes all buttons
playPause = tk.Button(frame, text="Play/Pause\n►/ll", command=toggle)
playPause.pack(side=tk.LEFT)
previous = tk.Button(frame, text="Previous\n<<", command=prev)
previous.pack(side=tk.LEFT)
nextButt = tk.Button(frame, text="Next\n>>", command=nextS)
nextButt.pack(side=tk.LEFT)

#Initializes label for information returned by commands
retLabel = tk.Label(res)
retLabel.pack()

#A thread that constantly gives user the status of the mpd server
statusThread = threading.Thread(target=status, name="checkStatus", daemon=True)
statusThread.start()

root.mainloop()

