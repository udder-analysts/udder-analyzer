import MySQLdb as dbapi
import sys

dbServer='localhost'
dbSchema='udders'
dbUser='root'
dbPass='udders'

db=dbapi.connect(host=dbServer, user=dbUser, passwd=dbPass, db=dbSchema)
cur=db.cursor()

def querySpecies(sortby, order):
    if sortby != None and order != None:
        query = """SELECT * FROM species ORDER BY %s %s;"""
        cur.execute(query % (sortby, order))
    else:
        query =  """SELECT * FROM species;"""
        cur.execute(query)
    return cur.fetchall()

def queryComparisons(sortby, order):
    if sortby != None and order != None:
        query = """SELECT comparison, species FROM experiment ORDER BY %s %s;"""
        cur.execute(query % (sortby, order))
    else:
        query = """SELECT comparison, species FROM experiment;"""
        cur.execute(query)
    return cur.fetchall()

def queryExperiments(sortby, order):
    if sortby != None and order != None:
        query = """SELECT * FROM experiment ORDER BY %s %s;"""
        cur.execute(query % (sortby, order))
    else:
        query = """SELECT * FROM experiment;"""
        cur.execute(query)
    return cur.fetchall()

def queryGenes(sortby, order, reg):
    if sortby != None and order != None:
        query = """SELECT * FROM genes ORDER BY %s %s;"""
        cur.execute(query % (sortby, order))
    elif reg != None:
        query = """SELECT * FROM genes;"""
        cur.execute(query % (reg))
    else:
        query = """SELECT g.species, g.name, g.abbreviation, g.beginsite, g.endsite FROM genes;"""
        cur.execute(query)
    return cur.fetchall()

def queryElements(sortby, order):
    if sortby != None and order != None:
        query = """SELECT * FROM regulatory_elements ORDER BY %s %s;"""
        cur.execute(query % (sortby, order))
    else:
        query = """SELECT * FROM regulatory_elements;"""
        cur.execute(query)
    return cur.fetchall()

def queryFactors(sortby, order):
    #TODO make it distinct
    if sortby != None and order != None:
        query = """SELECT * FROM transcription_factors ORDER BY %s %s;"""
        cur.execute(query % (sortby, order))
    else:
        query = """SELECT * FROM transcription_factors;"""
        cur.execute(query)
    return cur.fetchall()

def queryCompForSpec(specID, sortby, order):
    if sortby != None and order != None:
        query = """SELECT comparison FROM experiment WHERE species='%s'
                   ORDER BY %s %s;"""
        cur.execute(query % (specID, sortby, order))
    else:
        query = """SELECT comparison FROM experiment WHERE species='%s';"""
        cur.execute(query % (specID))
    return cur.fetchall()

def queryExpForCompSpec(specID, compID, sortby, order):
    if sortby != None and order != None:
        query = """SELECT * FROM experiment 
                   WHERE species='%s' AND comparison='%s'
                   ORDER BY %s %s;"""
        cur.execute(query % (specID, compID, sortby, order))
    else:
        query = """SELECT * FROM experiment 
                   WHERE species='%s' AND comparison='%s';"""
        cur.execute(query % (specID, compID))
    return cur.fetchall()

def queryGenesForExp(expID, sortby, order, reg):
    if sortby != None and order != None:
        query = """SELECT g.id, g.name, g.abbreviation, g.species, 
                          g.chromosome, g.beginsite, g.endsite 
                   FROM genes g, job_parameters j 
                   WHERE j.exp_id='%s' AND j.gene_id=g.id
                   ORDER BY %s %s;"""
        cur.execute(query % (expID, sortby, order))
    elif reg != None:
        query = """SELECT g.id, g.name, g.abbreviation, g.species, 
                          g.chromosome, g.beginsite, g.endsite 
                   FROM genes g, job_parameters j 
                   WHERE j.exp_id='%s' AND j.regulation='%s' AND j.gene_id=g.id;"""
        cur.execute(query % (expID, reg))
    else:
        query = """SELECT g.id, g.name, g.abbreviation, g.species, 
                          g.chromosome, g.beginsite, g.endsite 
                   FROM genes g, job_parameters j 
                   WHERE j.exp_id='%s' AND j.gene_id=g.id;"""
        cur.execute(query % (expID))
    return cur.fetchall()

def queryFactorsForGeneExp(expID, geneID, sortby, order):
    if sortby != None and order != None:
        query = """SELECT DISTINCT f.name FROM job_parameters j, 
                          regulatory_elements r, transcription_factors f 
                   WHERE j.exp_id='%s' AND j.gene_id='%s' AND 
                         j.gene_id=r.gene_id AND r.id=f.reg_element
                   ORDER BY %s %s;"""
        cur.execute(query % (expID, geneID, sortby, order))
    else:
        query = """SELECT DISTINCT f.name FROM job_parameters j, 
                          regulatory_elements r, transcription_factors f 
                   WHERE j.exp_id='%s' AND j.gene_id='%s' AND 
                         j.gene_id=r.gene_id AND r.id=f.reg_element;"""
        cur.execute(query % (expID, geneID))
    return cur.fetchall()

def queryElemForFacGeneExp(expID, geneID, facID, sortby, order):
    if sortby != None and order != None:
        query = """SELECT r.id, r.beginning, r.length, r.sense, r.model, 
                          r.reg_sequence, r.la, r.la_slash, r.lq, r.ld, r.lpv, 
                          r.sc, r.sm, r.spv, r.ppv, r.gene_id, r.experiment_id 
                   FROM regulatory_elements r, transcription_factors f 
                   WHERE f.name='%s' AND f.reg_element=r.id AND 
                         r.experiment_id='%s' AND r.gene_id='%s' 
                   ORDER BY r.%s %s;"""
        cur.execute(query % (facID, expID, geneID, sortby, order))
    else:
        query = """SELECT r.id, r.beginning, r.length, r.sense, r.model, 
                          r.reg_sequence, r.la, r.la_slash, r.lq, r.ld, r.lpv, 
                          r.sc, r.sm, r.spv, r.ppv, r.gene_id, r.experiment_id 
                   FROM regulatory_elements r, transcription_factors f 
                   WHERE f.name='%s' AND f.reg_element=r.id AND 
                         r.experiment_id='%s' AND r.gene_id='%s';"""
        cur.execute(query % (facID, expID, geneID))
    return cur.fetchall()

def queryExpForComp(compID, sortby, order):
    if sortby != None and order != None:
        query = """SELECT * FROM experiment 
                   WHERE comparison='%s' 
                   ORDER BY %s %s;"""
        cur.execute(query % (compID, sortby, order))
    else:
        query = """SELECT * FROM experiment WHERE comparison='%s';"""
        cur.execute(query % (compID))
    return cur.fetchall()

def queryElemForGeneExp(expID, geneID, sortby, order, lvalue, lvalFrom, lvalTo, locFrom, locTo):
    if sortby != None and order != None:
        query = """SELECT * FROM regulatory_elements 
                   WHERE experiment_id='%s' AND gene_id='%s'
                   ORDER BY %s %s;"""
        cur.execute(query % (expID, geneID, sortby, order))
    elif lvalue != None and lvalFrom != None and lvalTo != None:
        query = """SELECT * FROM regulatory_elements 
                   WHERE experiment_id='%s' AND gene_id='%s' AND %s BETWEEN %s AND %s;"""
        print query % (expID, geneID, lvalue, lvalFrom, lvalTo)
        cur.execute(query % (expID, geneID, lvalue, lvalFrom, lvalTo))
    elif locFrom != None and locTo != None:
        query = """SELECT * FROM regulatory_elements 
                   WHERE experiment_id='%s' AND gene_id='%s'
                         AND beginning BETWEEN %s AND %s;"""
        cur.execute(query % (expID, geneID, locFrom, locTo))
    else:
        query = """SELECT * FROM regulatory_elements 
                   WHERE experiment_id='%s' AND gene_id='%s';"""
        cur.execute(query % (expID, geneID))
    return cur.fetchall()

def queryElemForGene(geneID, sortby, order):
    if sortby != None and order != None:
        query = """SELECT * FROM regulatory_elements 
                   WHERE gene_id='%s' ORDER BY %s %s;"""
        cur.execute(query % (geneID, sortby, order))
    else:
        query = """SELECT * FROM regulatory_elements WHERE gene_id='%s';"""
        cur.execute(query % (geneID))
    return cur.fetchall()

def queryElemForFactor(facID, sortby, order):
    if sortby != None and order != None:    
        query = """SELECT r.id, r.beginning, r.length, r.sense, r.model, 
                          r.reg_sequence, r.la, r.la_slash, r.lq, r.ld, r.lpv, 
                          r.sc, r.sm, r.spv, r.ppv, r.gene_id, r.experiment_id 
                   FROM regulatory_elements r, transcription_factors f 
                   WHERE f.name='%s' AND f.reg_element=r.id
                   ORDER BY %s %s;"""
        cur.execute(query % (facID, sortby, order))
    else:
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

def queryElementDetails(elemID):
    query = """SELECT r.id, r.beginning, r.length, r.sense, r.model, 
                      r.reg_sequence, r.la, r.la_slash, r.lq, r.ld, r.lpv, 
                      r.sc, r.sm, r.spv, r.ppv, r.gene_id, r.experiment_id,
                      e.dateof, e.location, e.experimenter, e.comparison, 
                      e.species, t.name 
               FROM regulatory_elements r, experiment e, 
                    transcription_factors t
               WHERE r.id='%s' AND r.experiment_id=e.id 
                     AND r.id=t.reg_element;"""
    cur.execute(query % (elemID))
    return cur.fetchall()

