import os
from parser2 import *
import re

def parse(fileList):
	
	i = 0
	
	fails = []
	
	while i + 2 < len(fileList):

		#Find Hits
		file = fileList[i]
		i= i + 1
		m  = re.search("b([\w-]+) promoter TESS ([\w\s]+)\.csv", file.name)
		if(m) :
			geneAbbr = m.group(1);
			fileTypeName = m.group(2);
			if fileTypeName.find("Hits") >= 0 :
				hits = file;
			else:
				fails.append(file)
				continue;
		else:
			fails.append(file)
			continue;
		
		#Find Job Parameters
		file = fileList[i]
		i = i + 1
		m  = re.search("b([\w-]+) promoter TESS ([\w\s]+)\.csv", file.name)
		if(m) :
			tempGeneAbbr = m.group(1);
			fileTypeName = m.group(2);
			if fileTypeName.find("Job Parameters") >= 0 and geneAbbr == tempGeneAbbr :
				geneAbbr = tempGeneAbbr;
				params = file;
			else:
				#Also add Hits
				fails.append(hits)
				fails.append(file)
				continue;
		else:
			fails.append(hits)
			fails.append(file)
			continue;
		

		#Find Sequences
		file = fileList[i]
		i = i + 1
		m  = re.search("b([\w-]+) promoter TESS ([\w\s]+)\.csv", file.name)
		if(m) :
			tempGeneAbbr = m.group(1);
			fileTypeName = m.group(2);
			if fileTypeName.find("Sequences") >= 0 and geneAbbr == tempGeneAbbr :
				geneAbbr = tempGeneAbbr;
				sequence = file;
			else:
				fails.append(hits)
				fails.append(params)
				fails.append(file)
				continue;
		else:
			fails.append(hits)
			fails.append(params)
			fails.append(file)
			continue;
		
		#Got all 3, run parser
		result = parse_gene_files(hits, params, sequence);
		if not result:
			fails.append(hits)
			fails.append(params)
			fails.append(sequence)
			print "Failed in parser"
	
	while i < len(fileList):
		#Files remain, but not enough for set of 3, fail
		fails.append(fileList[i])
		i = i + 1
	
	return fails


def getFname(file) :

	return file.name


if __name__ == "__main__":
	input = "ExperimentData"

	files = []

	for filename in os.listdir(input) :
		currFile = open(input + "/" + filename)
		files.append(currFile)

	files = sorted(files, key = getFname)
		

	fails =parse(files)
	for fail in fails :
		print "Failed: " + fail.name



