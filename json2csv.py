"""
/ / / / / / / / / /
json2csv.py v0.2.1
/ / / / / / / / / /
Version Notes
-------------
0.1.0 Basic json file reader, but didn't use functions or loops and was rather long,
	introduced csv file output. Used hard references for filenames and filepaths.

0.1.1 Introduced functions and user input to find filepath to run script in.

0.2.0 Started from scratch and used v0.1.1 & 0.1.2 as references for writing this working
	version. This version removed initial user input and instead requires this script
	to already be in the json directory. Introducing user again can be implemented
	in Tkinter version (to be implemented maybe).

0.2.1 Added comments, cleaned up code, began introducing user input.
"""

import json
import os
import pandas as pd


#Returns the current filepath where this script is running from.
def startingDir():
	os.chdir(os.path.dirname(os.path.abspath(__file__)))
	cwd = os.getcwd()
	print("Current directory is: ", cwd)
	return cwd

#Scans the current directory for .json files. If they exist,
#this function will return a list of filenames that end in .json.
def scanDir(cwd):
	jsonFilenames = []
	for root, dirs, files in os.walk(cwd):
		for file in files:
			if file.endswith('.json'):
				#print(file)	#Print json filenames here if you need to debug
				jsonFilenames.append(file)
	return jsonFilenames

#Takes parameters of a filepath and the filename and copies them to a list.
def importJsonFiles(cwd, jfile):
	fp = cwd + "/" + jfile
	f = open(fp)
	"""Add error handling here in case filepath doesn't exist.
	Return error message so the code doesn't break."""
	data = json.load(f)
	#print(data)	#Print data list here to verify it imported the json file correctly
	f.close()
	return data

#Takes parameters of a filepath and list of json files and dumps them into a dictionary
def dumpJsonFiles(filepath, jsonFilenames):
	count = 0
	jsonDict = []
	csvFile = askUser() + ".csv"

	while count < len(jsonFilenames):
		jsonDict = importJsonFiles(filepath, jsonFilenames[count])
		if count == 0:
			save2csv(jsonDict, True, csvFile)
		elif count != 0:
			save2csv(jsonDict, False, csvFile)
		count+=1
		print(count)
	#print(jsonDict)	#Print dictionary to verify it works
	return jsonDict

#Takes parameters of a dictionary and boolean to append to csv file.
def save2csv(dict, bool, filename):
	df = pd.json_normalize(dict)
	df.to_csv(filename, mode='a', header=bool, index = False)

#Ask user for filename input
def askUser():
	userInput = input("What do you want to name the file? ")
	return userInput

#Keeps the script from autoclosing after running. Disable by not calling.
def exit():
	k = 0
	while k != '1':
		k = input("Press 1 to exit: ")
		print(k)

def main():
	filepath = startingDir() #Define the filepath
	jsonFilenames = scanDir(filepath) #Import json filenames as a list
	jsonDict = dumpJsonFiles(filepath, jsonFilenames) #Dumps json into dictionary
	exit()

if __name__ == "__main__":
	main()
