#!/usr/bin/python
import sys
from Bio.Blast import NCBIXML

def printBlastResults(outputfile):
    resultHandle = open(outputfile)
    blastRecords = NCBIXML.parse(resultHandle)
    for blastRecord in blastRecords:
	for description in blastRecord.descriptions:
	    print blastRecord.descriptions[0].title
	for alignment in blastRecord.alignments:
	    for hsp in alignment.hsps:
		print "sequence: ", alignment.title
		print "evalue: ", hsp.expect
		print hsp.query
		print hsp.match
		print hsp.sbjct
		print ""

def parseMetagenomeSeqNumber(queryDefLine):
    """
    By default, the script just returns the entire queryDefLine.
    On certain occasions, you might want to parse certain parts of this line
    such as:
    lineElements = queryDefLine.split("|")
    return lineElements[3]
    """
    return queryDefLine

def parseGIandNameFromDefLine(defLine):
    lineElements = defLine.split("|")
    return [lineElements[1], lineElements[4]]

# this method was implemented for testing
def showFirstBlastResult(outputfile):
    resultHandle = open(outputfile)
    blastRecords = NCBIXML.parse(resultHandle)
    blastRecord = blastRecords.next()
    print "query name: ", blastRecord.query
    print "sequence number: ", parseMetagenomeSeqNumber(blastRecord.query)
    print "nr of descriptions: ", len(blastRecord.descriptions)
    print "nr of alignments: ", len(blastRecord.alignments)
    print "alignments: "
    for alignment in blastRecord.alignments:
	for hsp in alignment.hsps:
	    if hsp.expect < 0.3:
		print "    name: ", alignment.title
		print "        hsp subject: ", hsp.sbjct
		print "        hsp expect: ", hsp.expect

def blastresults2tabformat(outputfile):
    resultHandle = open(outputfile)
    blastRecords = NCBIXML.parse(resultHandle)
    print "\t".join(["seqnr", "hitginr", "hitname", "evalue", "bitscore", "similarity", "score"])
    for blastrecord in blastRecords:
	if len(blastrecord.alignments) > 0:
	    topalignment = blastrecord.alignments[0]
	    topalGI, topalName = parseGIandNameFromDefLine(topalignment.title)
	    tophit = topalignment.hsps[0]
	    expect = str(tophit.expect)
	    bits = str(tophit.bits)
	    similarity = str(float(tophit.positives) / tophit.align_length)
	    score = str(tophit.score)
	else:
	    topalGI = ""
	    topalName = ""
	    expect = ""
	    bits = ""
	    similarity = ""
	    score = ""
	print "\t".join([parseMetagenomeSeqNumber(blastrecord.query), topalGI, topalName, expect, bits, similarity, score])

def main():
    blastresultsfile = sys.argv[1]
    blastresults2tabformat(blastresultsfile)

if len(sys.argv) != 2:
    print "usage: ./parsexmlblast.py <blastresultsfile>\n"
    print "    Make sure the blastresultsfile is in xml.\n"
    sys.exit(-1)

main()
