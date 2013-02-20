#!/usr/bin/python
import os
import sys

class GItaxidFinder:
    def __init__(self, fileName):
        self.fileName = fileName

    def readAtLineSeekPosition(self, offset):
	self.fileObject.seek(offset)
        if offset > 0:
	    self.fileObject.readline()
	tmpLine = self.fileObject.readline().rstrip("\n")
	return tmpLine

    def chunkLineIsOK(self, line, giNr):
        if line == "":
	    sys.__stderr__.write("no taxon id found for giNr: %i" % giNr)
	    return False
	elif line.find("\t") == -1:
	    sys.__stderr__.write("chunkLine \'%s\'does not contain two fields. For giNr: %i" % (line, giNr))
	    return False
	else:
	    return True

    def searchFile(self, giNr):
	fileSize = os.path.getsize(self.fileName)
	self.fileObject = open(self.fileName)
	chunkSize = fileSize
	chunkLine = ""
	seekPosition = chunkSize / 2
	offset = 0
	giFound = False
	while (not giFound) and (chunkSize > 0):
	    chunkSize = chunkSize / 2
	    chunkLine = self.readAtLineSeekPosition(seekPosition)
	    if self.chunkLineIsOK(chunkLine, giNr):
		giNrInLine, taxIdInLine = chunkLine.split("\t")
		if giNr == int(giNrInLine):
		    return chunkLine
		    giFound = True
		elif giNr < int(giNrInLine):
		    #offset stays the same
		    seekPosition = offset + (chunkSize / 2)
		elif giNr > int(giNrInLine):
		    offset = offset + chunkSize
		    seekPosition = offset + (chunkSize / 2)
	    else:
		return ""

	return ""

