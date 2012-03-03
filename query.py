import MySQLdb as dbapi
import sys

dbServer='localhost'
dbSchema='udders'
dbUser='root'
dbPass='udders'

db=dbapi.connect(host=dbServer, user=dbUser, passwd=dbPass, db=dbSchema)
cur=db.cursor()

def querySpecies():
	query =  """SELECT * from species;"""
	cur.execute(query)
	return cur.fetchall()

def queryExperiments():
	query = """SELECT * from experiments;"""
	cur.execute(query)
	return cur.fetchall()

def queryGenes():
	query = """SELECT * from genes;"""
	cur.execute(query)
	return cur.fetchall()

def queryElements():
	query = """SELECT * from regulatory_elements;"""
	cur.execute(query)
	return cur.fetchall()

def queryFactors():
	query = """SELECT * from transcription_factors;"""
	cur.execute(query)
	return cur.fetchall()
