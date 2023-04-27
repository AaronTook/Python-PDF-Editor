"""
	Author: AaronTook (https://github.com/AaronTook/)
	Last modified : 4/26/2023
	Project name: Python PDF Editor
	File name: app.py
	File description: Run the menu for the console application, accessing the functionality of utils.py.
"""
import os, sys, json

if __name__ == "__main__":
	thisDirectory = os.getcwd()
	print("----- Python PDF Editor -----")
	try: # Import 3rd-party module PyPDF2.
		import PyPDF2
	except ModuleNotFoundError: # PyPDF2 is not installed. Inform the user and exit.
		input("!> ERROR: Necessary Module PyPDF2 is not installed. Please visit https://pypdf2.readthedocs.io/en/latest/user/installation.html for instructions on installing PyPDF2.\n!> Press Enter/Return to exit... ")
		sys.exit()
	try: # Import source code file utils.py.
		import utils
	except ModuleNotFoundError: # utils.py is missing. Inform the user and exit.
		input("!> ERROR: Necessary File utils.py could not be found. Please visit https://github.com/AaronTook/Python-PDF-Editor to download the file and place it in this directory/folder. \n!> Press Enter/Return to exit... ")
		sys.exit()
	try:
		jsonData = utils.loadVersionDataFromJSON()
	except FileNotFoundError:
		input("!> ERROR: Necessary File data.json could not be found. Please visit https://github.com/AaronTook/Python-PDF-Editor to download the file and place it in this directory/folder. \n!> Press Enter/Return to exit... ")
		sys.exit()
	currentDirectory = jsonData["current_directory"]
	if currentDirectory != "":
		print(f"Current root folder/directory: {currentDirectory}")
		os.chdir(currentDirectory)
	utils.check_for_update(jsonData["next_version"])
	print("Enter \"help\" for a list of commands or enter a command...") # Display an informative message.
	while True:
		userInput = input("\n>> ").lower().strip()
		if userInput == "merge" or userInput == "merge-files": # Merge all .pdf files input by the user.
			utils.merge()
		elif userInput == "merge-directory" or userInput == "merge-folder": # Merge all .pdf files in a directory/folder.
			utils.merge_directory()
		elif userInput == "decrypt":
			utils.decrypt_pdf()
		elif userInput == "encrypt":
			utils.encrypt_pdf()
		elif userInput == "re-encrypt":
			utils.re_encrypt_pdf()
		elif userInput == "reduce-size" or userInput == "reduce-file-size" :
			utils.reduce_size_pdf()
		elif userInput == "set-root-directory" or userInput == "set-root-folder":
			rootDirectory = utils.gui_get_directory()
			os.chdir(rootDirectory)
			jsonData["current_directory"] = rootDirectory
			with open (thisDirectory + '\\data.json', 'w') as f:
				json.dump (jsonData, f)
		elif userInput == "reset-root-directory" or userInput == "reset-root-folder":
			rootDirectory = thisDirectory
			os.chdir(rootDirectory)
			jsonData["current_directory"] = rootDirectory
			with open (thisDirectory + '\\data.json', 'w') as f:
				json.dump (jsonData, f)
		elif userInput == "get-root-directory" or userInput == "get-root-folder":
			print(f"Current root folder/directory: \"{os.getcwd()}\"")
		elif userInput == "help": # Display Help Menu, explaining functionality of each command.
			print(f"!> Note: All  filepaths can be absolute paths (start with C:\\Users\\...) or relative (starts at this directory/folder: \"{os.getcwd()}\").")
			print("!>Commands:")
			print("\"merge\" or \"merge-files\" -> Prompt for any number of files and filepaths, combine all into one PDF file.")
			print("\"merge-directory\" or \"merge-folder\" -> Prompt for a path to an input folder, combine all PDF files in that folder in alphanumerical order into one PDF file.")
			print("\"decrypt\" -> Remove a password from a PDF file.")
			print("\"encrypt\" -> Add a password to a PDF file.")
			print("\"re-encrypt\" -> Change the password on an encrypted PDF file.")
			print("\"reduce-size\" or \"reduce-file-size\" -> Attempt to reduce a PDF's size by removing duplicate data and by using lossless compression.'")
			print("\"set-root-directory\" or \"set-root-folder\" -> Set the root folder/directory to save files to.")
			print(f"\"reset-root-directory\" or \"reset-root-directory\" -> Set the root folder/directory to \"{thisDirectory}\".")
			print("\"get-root-directory\" or \"get-root-folder\"")
			print("\"help\" -> Display this menu.")
			print("\"version\" or \"credits\" -> Display credits and version information.")
			print("\"license\" -> Display the project's MIT license.")
			print("\"clear\" or \"restart\" -> Clear console output.")
			print("\"quit\" or \"exit\" -> Quit the program.")
		elif userInput == "version" or userInput == "credits": # Show Version information and credits.
			try:
				print("!> Version Information and Credits:")
				print(f"Python PDF Editor - Version {jsonData['version']}\n")
				print(f"Version Launch Date: {jsonData['launch_date']}")
				print("Project Contributors: AaronTook: https://github.com/AaronTook")
				for version in jsonData["all_versions"]:
					print(f"Version {version['version']}: {version['about']}")
				print("\nMany thanks to the developers and contributors of the PyPDF2 project, without whose work this project would have been impossible. You can learn more about PyPDF2 at https://pypdf2.readthedocs.io/en/latest/.")
			except Exception as e: # An error occurred. Inform the user without crashing the program.
				print("!> Something went wrong! Here is the error message:")
				print(e)
				print("!> Feel free to contact the developer (AaronTook) if the issue persists!")	
		elif userInput == "license": # Show Software MIT License.
			print("""MIT License\n\nCopyright (c) 2023 AaronTook\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.""")
		elif userInput == "clear" or userInput == "restart": # Clear the console and redisplay start messages.
			os.system('cls' if os.name == 'nt' else 'clear')
			print("----- Python PDF Editor -----")
			try: # Import 3rd-party module PyPDF2.
				import PyPDF2
			except ModuleNotFoundError: # PyPDF2 is not installed. Inform the user and exit.
				input("!> ERROR: Necessary Module PyPDF2 is not installed. Please visit https://pypdf2.readthedocs.io/en/latest/user/installation.html for instructions on installing PyPDF2.\n!> Press Enter/Return to exit... ")
				sys.exit()
			try: # Import source code file utils.py.
				import utils
			except ModuleNotFoundError: # utils.py is missing. Inform the user and exit.
				input("!> ERROR: Necessary File utils.py could not be found. Please visit https://github.com/AaronTook/Python-PDF-Editor to download the file and place it in this directory/folder. \n!> Press Enter/Return to exit... ")
				sys.exit()
			try:
				jsonData = utils.loadVersionDataFromJSON()
			except FileNotFoundError:
				input("!> ERROR: Necessary File data.json could not be found. Please visit https://github.com/AaronTook/Python-PDF-Editor to download the file and place it in this directory/folder. \n!> Press Enter/Return to exit... ")
				sys.exit()
			currentDirectory = jsonData["current_directory"]
			if currentDirectory != "":
				print(f"Current root folder/directory: {currentDirectory}")
				os.chdir(currentDirectory)
			utils.check_for_update(jsonData["next_version"])
			print("Enter \"help\" for a list of commands or enter a command...") # Display an informative message.
		elif userInput == "quit" or userInput == "exit": # Exit the program.
			break
		else:
			print(f"!> \"{userInput}\" is not a valid command.\n!> Enter \"help\" for a list of commands.")
