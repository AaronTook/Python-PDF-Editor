"""
	Author: AaronTook (https://github.com/AaronTook/)
	Last modified : 4/26/2023
	Project name: Python PDF Editor
	File name: utils.py
	File description: Define functions to be used in app.py's console-based tool. Use PyPDF2 to manipulate the PDF (.pdf) files.
"""

import os, requests, webbrowser, json
import PyPDF2

from tkinter import *
from tkinter import filedialog

def loadVersionDataFromJSON(): # Added for update 1.3.1
	try:
		with open("data.json","r") as jsonFile:
			versionData = json.load(jsonFile)
		return versionData
	except Exception as e: # An error occurred. Inform the user without crashing the program.
		print("!> Something went wrong! Here is the error message:")
		print(e)
		print("!> Feel free to contact the developer (AaronTook) if the issue persists!")	
def gui_get_files(): # Added for update 1.2.1
	""" Open file explorer (using tkinter) to select multiple files. """
	root = Tk()
	root.withdraw()
	file_paths = filedialog.askopenfilenames()
	root.destroy()
	return [file_path for file_path in file_paths]
def gui_get_file(): # Added for update 1.2.1
	""" Open file explorer (using tkinter) to select a file. """
	root = Tk()
	root.withdraw()
	file_path = filedialog.askopenfilename()
	root.destroy()
	return file_path
def gui_get_directory(): # Added for update 1.2.1
	""" Open file explorer (using tkinter) to select a directory/folder """
	root = Tk()
	root.withdraw()
	directory_path = filedialog.askdirectory()
	root.destroy()
	return directory_path
def check_for_update(nextVersionNumber): # Added for update 1.2.1
	updateURL = f"https://github.com/AaronTook/Python-PDF-Editor/tree/main/{nextVersionNumber}"
	if requests.get(updateURL).status_code == requests.codes.ok:
		if input(f"!> An new update (Version {nextVersionNumber}) is available!\n !>Would you like to view the update download page (y/n)? ").lower() == "y":
			webbrowser.open(updateURL)
def add_extension_if_applicable(strInput): # Added for update 1.0.1
	""" Add .pdf to the passed string (representing a filename) if the string does not already end with some form of ".pdf". """
	if not strInput.lower().endswith(".pdf"):
		return strInput + ".pdf"
	return strInput
def encrypt_pdf(): # Added for update 1.1.1
	""" Encrypt a PDF file using a password input by the user. """
	try:
		inputFileName = gui_get_file()
		reader = PyPDF2.PdfReader(inputFileName)
		writer = PyPDF2.PdfWriter()
		
		for page in reader.pages: # Add all pages to the writer
			writer.add_page(page)
		writer.encrypt(input(">> Password for the PDF file: ")) # Add a password to the new .pdf file.
		with open(add_extension_if_applicable(input(">> Filename of output file: ")), "wb") as f: # Save the new PDF to a file
			writer.write(f)
	except Exception as e: # An error occurred. Inform the user without crashing the program.
		print("!> Something went wrong! Here is the error message:")
		print(e)
		print("!> Feel free to contact the developer (AaronTook) if the issue persists!")	
def decrypt_pdf(): # Added for update 1.1.1
	""" Decrypt  a PDF file using a password input by the user. """
	try:
		inputFileName = gui_get_file()
		reader = PyPDF2.PdfReader(inputFileName)
		writer = PyPDF2.PdfWriter()
		if reader.is_encrypted: # Check that the original filie is encrypted.
			reader.decrypt(input(">> Password of the encrypted PDF file: "))
		else:
			print("!> The requested PDF file is not encrypted! ")
		for page in reader.pages: # Add all pages to the writer.
			writer.add_page(page)
		with open(add_extension_if_applicable(input(">> Filename of output file: ")), "wb") as f: # Save the new PDF to a file.
			writer.write(f)
	except Exception as e: # An error occurred. Inform the user without crashing the program.
		print("!> Something went wrong! Here is the error message:")
		print(e)
		print("!> Feel free to contact the developer (AaronTook) if the issue persists!")	
def re_encrypt_pdf(): # Added for update 1.1.1
	""" Decrypt  a PDF file using a password input by the user and re-encrypt it with a new password. """
	try:
		inputFileName = gui_get_file()
		reader = PyPDF2.PdfReader(inputFileName)
		writer = PyPDF2.PdfWriter()
		if reader.is_encrypted: # Check that the original filie is encrypted.
			reader.decrypt(input(">> Password of the encrypted PDF file: "))
		else:
			print("!> The requested PDF file is not encrypted! ")
		for page in reader.pages: # Add all pages to the writer.
			writer.add_page(page)
		writer.encrypt(input(">> Password for the PDF file: ")) # Add a password to the new .pdf file.
		with open(add_extension_if_applicable(input(">> Filename of output file: ")), "wb") as f: # Save the new PDF to a file.
			writer.write(f)
	except Exception as e: # An error occurred. Inform the user without crashing the program.
		print("!> Something went wrong! Here is the error message:")
		print(e)
		print("!> Feel free to contact the developer (AaronTook) if the issue persists!")	
def merge(): # Added for update 1.0.1
	""" Merge an arbitrary number of .pdf files, each of whose paths are input by the user. """
	try:
		inputFilenames = gui_get_files()
		if len(inputFilenames) > 0:
			merger = PyPDF2.PdfWriter() # Create a PdfWriter object.
			for inputFilename in inputFilenames: # Add each of the .pdf files to the PdfWriter.
				merger.append(inputFilename)
			outputFileName = add_extension_if_applicable(input(">> Filename of output file: ")) # Get the output .pdf file name.
			merger.write(outputFileName) # Save the merged.pdf file.
			merger.close() # Close the PdfWriter object.
		else:
			print(f"!> Cannot merge {len(inputFilenames)} PDF files. File Merge Cancelled.")
	except Exception as e: # An error occurred. Inform the user without crashing the program.
		print("!> Something went wrong! Here is the error message:")
		print(e)
		print("!> Feel free to contact the developer (AaronTook) if the issue persists!")		
def merge_directory(): # Added for update 1.0.1
	""" Merge all .pdf files in a directory/folder whose path is input by the user. """
	try:
		pdfDirectoryPath = gui_get_directory()
		pdfFileNames = sorted([dataFile for dataFile in os.listdir(pdfDirectoryPath) if dataFile.lower().endswith(".pdf")]) # Add all the .pdf files from the given directory/folder to a list.
		if len(pdfFileNames) > 0:
			merger = PyPDF2.PdfWriter() # Create a PdfWriter object.
			for pdfFileName in pdfFileNames: # Add each of the .pdf files to the PdfWriter.
				merger.append(pdfDirectoryPath + "\\" + pdfFileName)
			outputFileName = add_extension_if_applicable(input(">> Filename of output file: ")) # Get the output .pdf file name.
			merger.write(outputFileName) # Save the merged.pdf file.
			merger.close() # Close the PdfWriter object.
		else:
			print(f"!> The Directory has no valid PDF Files. Directory Merge Cancelled.")
	except Exception as e: # An error occurred. Inform the user without crashing the program.
		print("!> Something went wrong! Here is the error message:")
		print(e)
		print("!> Feel free to contact the developer (AaronTook) if the issue persists!")
def reduce_size_pdf(): # Added for update 1.3.1
	""" Reduce a PDF file's size by removing duplicate objects and performing a lossless compression.  """
	try:
		inputFileName = gui_get_file()
		reader = PyPDF2.PdfReader(inputFileName)
		writer = PyPDF2.PdfWriter()
		if input("!> This process can be CPU intensive for some files. Continue (y/n)? ").lower() == "y":
			for page in reader.pages:
				page.compress_content_streams() # This is CPU intensive!
				writer.add_page(page)
			writer.add_metadata(reader.metadata)
			with open(add_extension_if_applicable(input(">> Filename of output file: ")), "wb") as f: # Save the new PDF to a file
				writer.write(f)
		else:
			print("!> Ok! Cancelling PDF size reduction")
	except Exception as e: # An error occurred. Inform the user without crashing the program.
		print("!> Something went wrong! Here is the error message:")
		print(e)
		print("!> Feel free to contact the developer (AaronTook) if the issue persists!")	
