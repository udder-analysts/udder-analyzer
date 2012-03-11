import MySQLdb as dbapi
import sys
import csv

dbServer='localhost'
dbSchema='udders'
dbUser='root'
dbPass='udders'

db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass,db=dbSchema)
cur=db.cursor()

#inserts tuple in to species
def insertIntoSpecies(name, division):
	#Inserts name and division into the species table if they don't already exist.
	query = """SELECT name from species where name = %s"""
	cur.execute(query,(name))
	if cur.fetchone() == None:
		query = """INSERT INTO species(name, flagged, hidden) values(%s, 0, 0)"""
		cur.execute(query,(name))
		commit()

#Returns the ID of the Experiment, if one exists, date in seconds.
def getExperimentID(experimenter, comparison, species, dateof):
	query = """SELECT id from experiment where experimenter = %s and comparison = %s
	and species = %s and dateof = %s"""
	cur.execute(query,(experimenter, comparison, species, dateof))
	expID = cur.fetchone()
	if expID == None:
		return -1
	else:
		return expID[0]

#inserts tuple into experiment
def insertIntoExperiment(dateof, location, experimenter,comparison,species):
	#Inserts values into experiment table if they don't already exist.
	if getExperimentID(experimenter, comparison, species, dateof) < 0 :
		query = """INSERT INTO experiment values(null,%s,%s,%s,%s,%s, 0, 0);"""
		cur.execute(query,(dateof, location,experimenter,comparison,species))
		commit()

#inserts tuple into genes
def insertIntoGenes(name, abbrev, species, chromosome, beginsite, endsite):
	#Inserts values into gene table if they don't already exist.
	if getGeneID(name, species) < 0:
		query = """INSERT INTO genes values(null,%s,%s,%s,%s,%s,%s, 0, 0)"""
		cur.execute(query,(name, abbrev, species, chromosome, beginsite, endsite))
		commit()

# gets geneID from genes table
def getGeneID(name, species):
	query = """SELECT id from genes where name = %s and species = %s"""
	cur.execute(query,(name,species))
	geneID = cur.fetchone()
	if geneID == None:
		return -1
	else:
		return geneID[0]

#inserts tuple into gene sequence			
def insertIntoGeneSeq(geneID, sequence):
	"""Inserts values into gene_sequence table if they don't already exist."""
	query = """SELECT id from gene_sequence where id = %s """
	cur.execute(query,(geneID))
	if cur.fetchone() == None:
		query = """INSERT INTO gene_sequence values(%s,%s, 0, 0)"""
		cur.execute(query,(geneID,sequence))
		commit()

#inserts a tuple in job_parameters	
def insertIntoJobParameters(geneID, expID, regulation, timeLen, email, transfacStrings, mySiteStrings, selected1, transfacMatrices, imdMatrices, gbilGibbsmatMatrices, jasparMatrices, myweightMat, selected2, combineWith, factorAttribute1, matches, useOnlyCorePos, maxAllowedMismatch, minLogLikelihoodRatioScore, minStringLength, minLgLikelihoodRatio, groupSelection1, maxLgLikelihoodDeficit, minCoreSimilarity, minMatrixSimilarity, secondLgLikelihoodDeficit, countSigThreshold, selected3, pseudocounts, groupSelection2, atContent, explicitAdist, explicitCdist, explicitGdist, explicitTdist, handleAmbigBases, tessJob):
	"""Inserts values into job parameters table if they don't already exist."""
	query = """SELECT gene_id from job_parameters where gene_id = %s and exp_id = %s"""
	cur.execute(query,(geneID, expID))
	if cur.fetchone() == None:
		query = """INSERT INTO job_parameters values(%s,%s,%s,%s,%s,%s,%s,%s,%s,
		%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,
		%s,%s,%s,%s,%s,%s,%s,%s, 0, 0)"""
		cur.execute(query,(geneID, expID, regulation, timeLen, email, transfacStrings, mySiteStrings, selected1, transfacMatrices, imdMatrices, gbilGibbsmatMatrices, jasparMatrices, myweightMat, selected2, combineWith, factorAttribute1, matches, useOnlyCorePos, maxAllowedMismatch, minLogLikelihoodRatioScore, minStringLength, minLgLikelihoodRatio, groupSelection1, maxLgLikelihoodDeficit, minCoreSimilarity, minMatrixSimilarity, secondLgLikelihoodDeficit, countSigThreshold, selected3, pseudocounts, groupSelection2, atContent, explicitAdist, explicitCdist, explicitGdist, explicitTdist, handleAmbigBases, tessJob))
		commit()

#inserts a tuple in regulatory_elements
def insertIntoRegulatoryElements(beginning, length, sense, model, regSequence, la, laSlash, lq, ld, lpv, sc, sm, spv, ppv, geneID, expID):
	#Inserts values into regulatory element table if they don't already exist.
	if getRegElementID(beginning, length, sense, model, geneID, expID) < 0 :
		query = """INSERT INTO regulatory_elements 
		values(null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s, 0, 0)"""
		cur.execute(query,(beginning, length, sense, model, regSequence, la, laSlash,
			lq, ld, lpv, sc, sm, spv, ppv, geneID, expID))
		commit()

#gets id of regulatory element
def getRegElementID(beginning, length, sense, model, geneID, expID):
	query = """SELECT id from regulatory_elements WHERE beginning = %s and length = %s
		and sense = %s and model = %s and gene_id = %s and experiment_id = %s"""
	cur.execute(query,(beginning, length, sense, model, geneID, expID))
	regElem = cur.fetchone()
	if regElem == None:
		return -1
	else:	
		return regElem[0]

#inserts tuple into transcription_factors
def insertIntoTranscriptionFactors(name, regElementID):
	#Inserts tuple into transcription_factors if it doesn't already exist.
	query = """SELECT name from transcription_factors where name = %s and 
	reg_element = %s"""
	cur.execute(query,(name, regElementID))
	if cur.fetchone() == None:
		query = """INSERT INTO transcription_factors values(%s,%s, 0, 0)"""
		cur.execute(query,(name, regElementID))
		commit()

#inserts tuple into t_number
def insertIntoTnumber(tnumber, regElementID):
	"""Inserts values into t_number table if they don't already exist."""
	query = """SELECT tnumber from t_number where tnumber = %s and reg_element = %s"""
	cur.execute(query,(tnumber,regElementID))
	if cur.fetchone() == None:
		query = """INSERT INTO t_number values(%s,%s, 0, 0)"""
		cur.execute(query,(tnumber, regElementID))
		commit()

#commit function to commit data in mysql database
def commit() :
	query = """commit;"""
	cur.execute(query)
