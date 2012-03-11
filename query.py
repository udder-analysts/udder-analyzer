import MySQLdb as dbapi
import sys

dbServer='localhost'
dbSchema='udders'
dbUser='root'
dbPass='udders'

db=dbapi.connect(host=dbServer, user=dbUser, passwd=dbPass, db=dbSchema)
cur=db.cursor()

def querySpecies():
	query =  """SELECT * FROM species;"""
	cur.execute(query)
	return cur.fetchall()

def queryComparisons():
    query = """SELECT comparison, species FROM experiment;"""
    cur.execute(query)
    return cur.fetchall()

def queryExperiments():
	query = """SELECT * FROM experiment;"""
	cur.execute(query)
	return cur.fetchall()

def queryGenes():
	query = """SELECT * FROM genes;"""
	cur.execute(query)
	return cur.fetchall()

def queryElements():
	query = """SELECT * FROM regulatory_elements;"""
	cur.execute(query)
	return cur.fetchall()

def queryFactors():
	query = """SELECT * FROM transcription_factors;"""
	cur.execute(query)
	return cur.fetchall()

def queryCompForSpec(specID):
    query = """SELECT comparison FROM experiment WHERE species='%s';"""
    cur.execute(query % (specID))
    return cur.fetchall()

def queryExpForCompSpec(specID, compID):
    query = """SELECT * FROM experiment 
               WHERE species='%s' AND comparison='%s';"""
    cur.execute(query % (specID, compID))
    return cur.fetchall()

def queryGenesForExp(expID):
    query = """SELECT g.id, g.name, g.abbreviation, g.species, g.chromosome, 
                      g.beginsite, g.endsite FROM genes g, job_parameters j 
               WHERE j.exp_id='%s' AND j.gene_id=g.id"""
    cur.execute(query % (expID))
    return cur.fetchall()

def queryFactorsForGeneExp(expID, geneID):
    query = """SELECT DISTINCT f.name FROM job_parameters j, 
                      regulatory_elements r, transcription_factors f 
               WHERE j.exp_id='%s' AND j.gene_id='%s' AND 
                     j.gene_id=r.gene_id AND r.id=f.reg_element"""
    cur.execute(query % (expID, geneID))
    return cur.fetchall()

def queryElemForFacGeneExp(expID, geneID, facID):
    query = """SELECT r.id, r.beginning, r.length, r.sense, r.model, 
                      r.reg_sequence, r.la, r.la_slash, r.lq, r.ld, r.lpv, 
                      r.sc, r.sm, r.spv, r.ppv, r.gene_id, r.experiment_id 
               FROM regulatory_elements r, transcription_factors f 
               WHERE f.name='%s' AND f.reg_element=r.id AND 
                     r.experiment_id='%s' AND r.gene_id='%s';"""
    cur.execute(query % (facID, expID, geneID))
    return cur.fetchall()

def queryExpForComp(compID):
    query = """SELECT * FROM experiment WHERE comparison='%s';"""
    cur.execute(query % (compID))
    return cur.fetchall()

def queryElemForGeneExp(expID, geneID):
    query = """SELECT * FROM regulatory_elements 
               WHERE experiment_id='%s' AND gene_id='%s';"""
    cur.execute(query % (expID, geneID))
    return cur.fetchall()

def queryElemForGene(geneID):
    query = """SELECT * FROM regulatory_elements WHERE gene_id='%s';"""
    cur.execute(query % (geneID))
    return cur.fetchall()

def queryElemForFactor(facID):
    query = """SELECT r.id, r.beginning, r.length, r.sense, r.model, 
                      r.reg_sequence, r.la, r.la_slash, r.lq, r.ld, r.lpv, 
                      r.sc, r.sm, r.spv, r.ppv, r.gene_id, r.experiment_id 
               FROM regulatory_elements r, transcription_factors f 
               WHERE f.name='%s' AND f.reg_element=r.id;"""
    cur.execute(query % (facID))
    return cur.fetchall()

def querySingleElemForGeneExp(expID, geneID, elemID):
    query = """SELECT * FROM regulatory_elements 
               WHERE experiment_id='%s' AND gene_id='%s' AND id='%s';"""
    cur.execute(query % (expID, geneID, elemID))
    return cur.fetchall()

def queryGenesForExpRegulated(expID, regulation):
    query = """SELECT g.id, g.name, g.abbreviation, g.species, g.chromosome, 
                      g.beginsite, g.endsite FROM genes g, job_parameters j 
               WHERE j.exp_id='%s' AND j.regulation='%s' AND j.gene_id=g.id"""
    cur.execute(query % (expID, regulation))
    return cur.fetchall()

def queryElemForGeneExpSort(expID, geneID, sort):
    query = """SELECT * FROM regulatory_elements 
               WHERE experiment_id='%s' AND gene_id='%s'
               SORT BY %s;"""
    cur.execute(query % (expID, geneID, sort))
    return cur.fetchall()

def queryElemForGeneExpLvalue(expID, geneID, lvalue):
    query = """SELECT * FROM regulatory_elements 
               WHERE experiment_id='%s' AND gene_id='%s' AND lvalue='%s';"""
    cur.execute(query % (expID, geneID, lvalue))
    return cur.fetchall()
  
def queryElementDetails(elemID):
    query = """SELECT r.id, r.beginning, r.length, r.sense, r.model, 
                      r.reg_sequence, r.la, r.la_slash, r.lq, r.ld, r.lpv, r.sc,
                      r.sm, r.spv, r.ppv, r.gene_id, r.experiment_id, e.dateof,
                      e.location, e.experimenter, e.comparison, e.species, 
                      t.name 
               FROM regulatory_elements r, experiment e, transcription_factors t
               WHERE r.id='%s' AND r.experiment_id=e.id 
                     AND r.id=t.reg_element"""
    cur.execute(query % (elemID))
    return cur.fetchall()
