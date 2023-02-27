from tkinter import filedialog
from tkinter import *
from tkinter import ttk
import os
import shutil
import datetime

OUT_PATH = "\\UDAF\Fotografias Javo"
FOLDERS = ["RAW", "MOV", "JPEG", "JPG", "DNG"]
FOLDERS_DICT = {"RAW": "RAW", "MOV": "MOV", "JPEG": "JPEG", "JPG": "JPG", "DNG": "DNG"}
EXTENSIONS = {"ORF": ".ORF", "MOV": ".MOV", "JPEG": ".JPEG", "JPG": ".JPG", "DNG": ".DNG"}

def selectDirectory(title):
    inputPath = filedialog.askdirectory(title=title)
    inputPath = inputPath.replace("/", os.sep)
    return inputPath 

def getFilesFromDirectory(inputPath):
    files = []

    for file in os.listdir(inputPath):
        filePath = inputPath + os.sep + file

        if os.path.isfile(filePath):
            files.append(filePath)

    return files

def saveFiles(files, path):

    TOTAL_FILES = float(files.__len__())

    for i, file in enumerate(files):

        percent = i * 100 / TOTAL_FILES

        print("Copiando foto " + str(i) + " de " + str(int(TOTAL_FILES)) + ". " + str(percent) + "'%' completado." ,end="\r")
        
        outPath = path

        fileDate = str(datetime.date.fromtimestamp(os.path.getmtime(file)))
        dateFolder = outPath + os.sep + fileDate
        createDirectories(dateFolder)   

        fileDateSimple = fileDate.replace("-", "")
        print(fileDateSimple)
        
        filePath, fileExtension = os.path.splitext(file)
        fileExtension = fileExtension.upper()
        print(filePath, fileExtension)

        if fileExtension == EXTENSIONS["ORF"]:
            outPath = dateFolder + os.sep + FOLDERS_DICT["RAW"]
        elif fileExtension == EXTENSIONS["MOV"]:
            outPath = dateFolder + os.sep + FOLDERS_DICT["MOV"]
        elif fileExtension == EXTENSIONS["JPEG"]:
            outPath = dateFolder + os.sep + FOLDERS_DICT["JPEG"]
        elif fileExtension == EXTENSIONS["JPG"]:
            outPath = dateFolder + os.sep + FOLDERS_DICT["JPG"]
        elif fileExtension == EXTENSIONS["DNG"]:
            outPath = dateFolder + os.sep + FOLDERS_DICT["DNG"]
        
        fileName = fileDateSimple + "-" + str("{:02d}".format(i)) + fileExtension
        outPath = outPath + os.sep + fileName

        print(outPath)
        print(file)
        shutil.copy2(file, outPath)

def createDirectories(path):
    if not os.path.exists(path):
        for folderName in FOLDERS:
            os.makedirs(path + os.sep + folderName)


if __name__ == '__main__':
    inputPath = selectDirectory("Selecciona la carpeta de la tarjeta")
    files = getFilesFromDirectory(inputPath)
    outPath = selectDirectory("Selecciona la carpeta fotografias Javo")
    saveFiles(files, outPath)


    