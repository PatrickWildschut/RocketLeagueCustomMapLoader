#/usr/bin/env python3

import shutil
import tkinter as tk
from tkinter import filedialog as fd
import os

# Variables
root = tk.Tk()
customFolder = ''
rocketLeagueFolder = ''
customMaps = []
loadMap = tk.StringVar(root)

# Main entry of program
def main():
	global customMaps
	paths = False

	# Check if rocket league folder and custom map folder are assigned
	if os.path.isfile(os.path.expanduser("~\\Documents\\PW\\paths.txt")):
		paths = True
		customMaps = loadMaps()

	setupTk(paths)

def loadMaps():
	global customFolder
	var = []
	with open(os.path.expanduser("~\\Documents\\PW\\paths.txt"), "r") as file:
		folder = file.readline().strip() # Get first line
		customFolder = folder
		var = os.listdir(folder)

	return var

def setupTk(isSetup):
	global root

	if isSetup:
		tk.Button(root, text="Load custom", command=LoadCustom).pack()

		loadMap.set(customMaps[0])

		tk.OptionMenu(root, loadMap, *customMaps).pack()
	else:
		tk.Label(root, text="Welcome, please set up this before use:").pack()
		tk.Button(root, text="Set custom map folder", command=setCustomMapFolder).pack()
		tk.Button(root, text="Set 'rocketleague' folder", command=setrocketleagueFolder).pack()

	root.mainloop()

def LoadCustom():

	path = ''

	with open(os.path.expanduser("~\\Documents\\PW\\paths.txt"), "r") as file:
		path = file.readlines()[1].strip()

	shutil.copy2(customFolder + "\\" + loadMap.get(), path + "\\TAGame\\CookedPCConsole\\Labs_Underpass_P.upk")
	print("Placed custom map! In rocket league, in freeplay, Underpass to play!")

def restore():
	print("Unassigned!")


## SETUPSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
def restart():
	global root

	root.destroy()
	root = tk.Tk()
	main()

def setupFolders():
	if not os.path.isdir(os.path.expanduser("~\\Documents\\PW")):
		os.mkdir(os.path.expanduser("~\\Documents\\PW"))

	with open(os.path.expanduser("~\\Documents\\PW\\paths.txt"), "w") as file:
		file.write(customFolder + "\n" + rocketLeagueFolder + "\n")

	restart()

## ONCLICKSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
def setCustomMapFolder():
	global customFolder
	customFolder = fd.askdirectory()

	if os.path.isdir(customFolder) and os.path.isdir(rocketLeagueFolder):
		setupFolders()

def setrocketleagueFolder():
	global rocketLeagueFolder
	rocketLeagueFolder = fd.askdirectory()

	if os.path.isdir(customFolder) and os.path.isdir(rocketLeagueFolder):
		setupFolders()

if __name__ == "__main__":
	main()
