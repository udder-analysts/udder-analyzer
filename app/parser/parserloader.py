import os
from parser import *
import re

def parse(fileList):
	
	i = 0
	
	fails = []
	
	while i + 2 < len(fileList):

		#Find Hits
		inFile = fileList[i]
		i= i + 1
		m  = re.search("b([\w-]+) promoter TESS ([\w\s]+)\.csv", inFile.filename)
		if(m) :
			geneAbbr = m.group(1);
			fileTypeName = m.group(2);
			if fileTypeName.find("Hits") >= 0 :
				hits = inFile;
			else:
				fails.append(inFile.filename)
				continue;
		else:
			fails.append(inFile.filename)
			continue;
		
		#Find Job Parameters
		inFile = fileList[i]
		i = i + 1
		m  = re.search("b([\w-]+) promoter TESS ([\w\s]+)\.csv", inFile.filename)
		if(m) :
			tempGeneAbbr = m.group(1)
			fileTypeName = m.group(2)
			if fileTypeName.find("Job Parameters") >= 0 and geneAbbr == tempGeneAbbr :
				geneAbbr = tempGeneAbbr;
				params = inFile;
			else:
				#Also add Hits
				fails.append(hits.filename)
				fails.append(inFile.filename)
				continue;
		else:
			fails.append(hits.filename)
			fails.append(inFile.filename)
			continue;
		

		#Find Sequences
		inFile = fileList[i]
		i = i + 1
		m  = re.search("b([\w-]+) promoter TESS ([\w\s]+)\.csv", inFile.filename)
		if(m) :
			tempGeneAbbr = m.group(1);
			fileTypeName = m.group(2);
			if fileTypeName.find("Sequences") >= 0 and geneAbbr == tempGeneAbbr :
				geneAbbr = tempGeneAbbr;
				sequence = inFile;
			else:
				fails.append(hits.filename)
				fails.append(params.filename)
				fails.append(inFile.filename)
				continue;
		else:
			fails.append(hits.filename)
			fails.append(params.filename)
			fails.append(inFile.filename)
			continue;
		
		#Got all 3, run parser
		result = parse_gene_files(hits, params, sequence);
		if not result:
			fails.append(hits.filename)
			fails.append(params.filename)
			fails.append(sequence.filename)
			print "Failed in parser"
	
	while i < len(fileList):
		#Files remain, but not enough for set of 3, fail
		fails.append(fileList[i])
		i = i + 1
	
	return fails


#def getFname(inFile) :
#	return inFile.filename
#
#if __name__ == "__main__":
#	input = "Small"
#
#	files = []
#
#	for filename in os.listdir(input) :
#		currFile = open(input + "/" + filename)
#		files.append(currFile)
#
#	files = sorted(files, key = getFname)
#		
#
#	fails =parse(files)
#	for fail in fails :
#		print "Failed: " + fail.filename



