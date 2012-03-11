import MySQLdb as dbapi
import sys
import csv

dbServer='localhost'
dbSchema='udders'
dbUser='root'
dbPass='udders'

db=dbapi.connect(host=dbServer,user=dbUser,passwd=dbPass,db=dbSchema)
cur=db.cursor()

def commit() :
	query = """commit;"""
	cur.execute(query)

def setFlaggedSpecies (name, flag) :
	query = """UPDATE species SET flagged = %s WHERE name = %s"""
	cur.execute(query,(flag, name))
	commit()

def setFlaggedexperiment (id, flag) :
	query = """UPDATE experiment SET flagged = %s WHERE id = %s"""
	cur.execute(query,(flag, id))
	commit()

def setFlaggedGenes (id, flag) :
	query = """UPDATE genes SET flagged = %s WHERE id = %s"""
	cur.execute(query,(flag, id))
	commit()

def setFlaggedGeneSeq (id, flag) :
	query = """UPDATE gene_sequence SET flagged = %s WHERE id = %s"""
	cur.execute(query,(flag, id))
	commit()

def setFlaggedJobParams (gene_id, exp_id, flag) :
	query = """UPDATE job_parameters SET flagged = %s WHERE gene_id = %s AND exp_id = %s"""
	cur.execute(query,(flag, gene_id, exp_id))
	commit()

def setFlaggedRegElements (id, flag) :
	query = """UPDATE regulatory_elements SET flagged = %s WHERE id = %s"""
	cur.execute(query,(flag, id))
	commit()

def setFlaggedTfactors (name, reg_element, flag) :
	query = """UPDATE transcription_factors SET flagged = %s WHERE name = %s AND reg_element = %s"""
	cur.execute(query,(flag, name, reg_element))
	commit()

def setFlaggedTnumber (tnumber, reg_element, flag) :
	query = """UPDATE transcription_factors SET flagged = %s WHERE tnumber = %s AND reg_element = %s"""
	cur.execute(query,(flag, tnumber, reg_element))
	commit()


def setHiddenSpecies (name, hide) :
	query = """UPDATE species SET hidden = %s WHERE name = %s"""
	cur.execute(query,(hide, name))
	commit()

def setHiddenexperiment (id, hide) :
	query = """UPDATE experiment SET hidden = %s WHERE id = %s"""
	cur.execute(query,(hide, id))
	commit()

def setHiddenGenes (id, hide) :
	query = """UPDATE genes SET hidden = %s WHERE id = %s"""
	cur.execute(query,(hide, id))
	commit()

def setHiddenGeneSeq (id, hide) :
	query = """UPDATE gene_sequence SET hidden = %s WHERE id = %s"""
	cur.execute(query,(hide, id))
	commit()

def setHiddenJobParams (gene_id, exp_id, hide) :
	query = """UPDATE job_parameters SET hidden = %s WHERE gene_id = %s AND exp_id = %s"""
	cur.execute(query,(hide, gene_id, exp_id))
	commit()

def setHiddenRegElements (id, hide) :
	query = """UPDATE regulatory_elements SET hidden = %s WHERE id = %s"""
	cur.execute(query,(hide, id))
	commit()

def setHiddenTfactors (name, reg_element, hide) :
	query = """UPDATE transcription_factors SET hidden = %s WHERE name = %s AND reg_element = %s"""
	cur.execute(query,(hide, name, reg_element))
	commit()

def setHiddenTnumber (tnumber, reg_element, hide) :
	query = """UPDATE transcription_factors SET hidden = %s WHERE tnumber = %s AND reg_element = %s"""
	cur.execute(query,(hide, tnumber, reg_element))
	commit()



#species (name)
#experiment (id)
#genes (id) 
#gene_sequence (id)
#job_parameters (gene_id, exp_id)
#regulatory_elements (id)
#transcription_factors (name, reg_element)
#t_number (tnumber, reg_element)