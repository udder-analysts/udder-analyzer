import os
from parser import *
import re

def parse(fileList):
	ret = True
	geneAbbr = ""

	print 'Now in parse()'

	for file in fileList:
		m  = re.match("b([\w-]+) promoter TESS ([\w\s]+)\.csv", file.filename)
		if(m) :
			tempGeneAbbr = m.group(1);
			fileTypeName = m.group(2);
      
			if fileTypeName.find("Hits") >= 0 :
				geneAbbr = tempGeneAbbr;
				hits = file;
				params = "";
				sequence = "";
			if fileTypeName.find("Job Parameters") >= 0:
				if geneAbbr == tempGeneAbbr :
					params = file;
				else :
					hits = "";
					params = "";
					sequence = "";
					geneAbbr = "";
			if fileTypeName.find("Sequences") >= 0:
				if geneAbbr == tempGeneAbbr :
					sequence = file;
					result = parse_gene_files(hits, params, sequence);
					if not result:
						ret = False
				hits = "";
				params = "";
				sequence = "";
				geneAbbr = "";

