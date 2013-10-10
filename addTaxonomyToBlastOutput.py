#!/usr/bin/python

import sys
sys.path.append("./scripts")
import blasthittaxonomy

def checkarguments():
    if len(sys.argv) != 2:
	print "usage: ./addTaxonomyToBlastOutput.py <blast output file>"
	sys.exit(-1)

def main():
    checkarguments()
    taxfetcher = blasthittaxonomy.TaxonomyFetcher()
    filename = sys.argv[1]
    infile = open(filename)
    header = infile.readline()
    print "\t".join(["seqnr", "hitginr", "hitname", "evalue", "bitscore", "similarity", "score", "division", "scientificName", "rank1", "rank2"])
    for line in infile:
	newline = line.rstrip("\n")
	seqnr, ginr, hitname, evalue, bitscore, sim, score = newline.split("\t")
	division = ""
	scientName = ""
	rank1 = ""
	rank2 = ""
	if ginr != "":
	    taxonomy = taxfetcher.getTaxonomy(int(ginr))
	    if taxonomy != "":
		scientName = taxonomy[0]["ScientificName"]
		if scientName == "unidentified":
		    scientName = ""
		else:
		    division = taxonomy[0]["Division"]
		    try:
			rank1 = taxonomy[0]["LineageEx"][0]["ScientificName"]
		    except:
		        rank1 = ""
		    try:
			rank2 = taxonomy[0]["LineageEx"][1]["ScientificName"]
		    except:
		        rank2 = ""
	print "\t".join([seqnr, ginr, hitname, evalue, bitscore, sim, score, division, scientName, rank1, rank2])
    taxfetcher.die()

main()
