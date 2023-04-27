"""
	Author: AaronTook (https://github.com/AaronTook/)
	Last modified : 4/23/2023
	Project name: Python PDF Editor
	File name: utils.py
	File description: Define functions to be used in app.py's console-based tool. Use PyPDF2 to manipulate the PDF (.pdf) files.
"""

import os
import PyPDF2

def add_extension_if_applicable(strInput): # Added for update 1.0.1
	""" Add .pdf to the passed string (representing a filename) if the string does not already end with some form of ".pdf". """
	if not strInput.lower().endswith(".pdf"):
		return strInput + ".pdf"
	return strInput

def encrypt_pdf(): # Added for update 1.1.1
	""" Encrypt a PDF file using a password input by the user. """
	try:
		while True: # Repeat until a valid filename is entered.
				inputFileName = add_extension_if_applicable(input(f">> Filename of file PDF file to decrypt: "))
				if os.path.exists(inputFileName):
					break
				else:
					print("!> That file does not exist! Please try again!")
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
		while True: # Repeat until a valid filename is entered.
				inputFileName = add_extension_if_applicable(input(f">> Filename of file PDF file to decrypt: "))
				if os.path.exists(inputFileName):
					break
				else:
					print("!> That file does not exist! Please try again!")
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
		while True: # Repeat until a valid filename is entered.
				inputFileName = add_extension_if_applicable(input(f">> Filename of file PDF file to decrypt: "))
				if os.path.exists(inputFileName):
					break
				else:
					print("!> That file does not exist! Please try again!")
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
		numPDFs = int(input(">> How many PDF files would you like to merge: ")) # Get the number of files to be merged.
		inputFilenames = []
		for i in range(numPDFs):
			while True: # Repeat until a valid filename is entered.
				fileName = add_extension_if_applicable(input(f">> Filename of file #{i + 1}: "))
				if os.path.exists(fileName):
					inputFilenames.append(fileName) # Add the .pdf file to the list of files.
					break
				else:
					print("!> That file does not exist! Please try again!")
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
		while True: # Repeat until a valid directory/folder is entered.
			pdfDirectoryPath = input(">> Path to directory/folder containing PDF files to be merged: ").replace('"','')
			if os.path.exists(pdfDirectoryPath):
				break
			else:
				print("!> That directory/folder does not exist! Please try again!")
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
