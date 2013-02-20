#!/usr/bin/env python

"""
author: bart aelterman
date: 2012-10-12
description: This class will help you find the taxonomy of a given BLAST hit
  using its GI number. The taxon id is found for each GI number using the
  GItaxidFinder class.
  Next, for each taxon id, the taxonomy is fetched from the NCBI server using
  the Entrez module in Biopython. A caching system is used to reduce the 
  number of request to the NCBI server
"""

import os
import sys
from Bio import Entrez
sys.path.append("./scripts")
import gi_taxid_search
import pickle


class TaxonomyFetcher():
    def getKnownTaxa(self):
	infile = open(self.knownTaxaFile)
	self.knownTaxa = pickle.loads(infile.read())
	infile.close()

    def __init__(self):
	Entrez.email = "youremail@mail.com"
	self.knownTaxaFile = "knowntaxonomy.txt"
        self.getKnownTaxa()

    def setKnownTaxaFile(self, fileName):
        self.knownTaxaFile = fileName
	self.getKnownTaxa()

    def getTaxonID(self, giNr):
	giFinder = gi_taxid_search.GItaxidFinder("./gi_taxid_nucl.dmp")
        resultLine = giFinder.searchFile(giNr)
	taxonID = ""
	if resultLine != "":
	    taxonID = resultLine.split("\t")[1]
	return taxonID

    def retrieveTaxonomy(self, taxonID):
	handle = Entrez.efetch(id = taxonID, db = "Taxonomy", retmode = "xml")
	taxonomy = Entrez.read(handle)
	return taxonomy

    def getTaxonomy(self, giNr):
	taxonId = self.getTaxonID(giNr)
	taxonomy = ""
	if taxonId != "":
	    if self.knownTaxa.has_key(taxonId):
		taxonomy = self.knownTaxa[taxonId]
	    else:
		taxonomy = self.retrieveTaxonomy(taxonId)
		self.knownTaxa[taxonId] = taxonomy
	return taxonomy
	
    def die(self):
        outfile = open("knowntaxonomy.txt", "w")
	outfile.write(pickle.dumps(self.knownTaxa))
	outfile.close

class Classifier():
    def addClassificationToLine(self, line, eValueCutoff, similarityCutoff):
        lineList = line.split("\t")
	eValuestr = lineList[3]
	similaritystr = lineList[5]
	newfield = "unknown"
	if eValuestr != "" and similaritystr != "":
	    eValue = float(eValuestr)
	    similarity = float(similaritystr)
	    topLevelTaxonomy = lineList[9]
	    secondLevelTaxonomy = lineList[10]
	    if (eValue <= eValueCutoff) and (similarity >= similarityCutoff):
		if topLevelTaxonomy == "cellular organisms" and secondLevelTaxonomy != "":
		    # add top level taxonomy
		    newfield = secondLevelTaxonomy
		elif topLevelTaxonomy != "":
		    # add second level taxonomy
		    newfield = topLevelTaxonomy
	lineList.append(newfield)
	outLine = "\t".join(lineList)
	return outLine
