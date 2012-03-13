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
        query = """SELECT g.id, g.species, g.name, g.abbreviation, g.chromosome, 
                          g.beginsite, g.endsite, COUNT(DISTINCT e.comparison),
                          COUNT(DISTINCT e.id) 
                   FROM genes g, job_parameters j, experiment e
                   WHERE g.id=gene_id and e.id=j.exp_id
                   GROUP BY g.species, g.name, g.abbreviation, g.chromosome,
                            g.beginsite, g.endsite
                   ORDER BY %s %s;"""
        cur.execute(query % (sortby, order))
    elif reg != None:
        query = """SELECT g.id, g.species, g.name, g.abbreviation, g.chromosome, 
                          g.beginsite, g.endsite, COUNT(DISTINCT e.comparison),
                          COUNT(DISTINCT e.id) 
                   FROM genes g, job_parameters j, experiment e
                   WHERE g.id=gene_id AND e.id=j.exp_id AND j.regulation='%s'
                   GROUP BY g.species, g.name, g.abbreviation, g.chromosome,
                            g.beginsite, g.endsite;"""
        cur.execute(query % (reg))
    else:
        query = """SELECT g.id, g.species, g.name, g.abbreviation, g.chromosome, 
                          g.beginsite, g.endsite, COUNT(DISTINCT e.comparison),
                          COUNT(DISTINCT e.id) 
                   FROM genes g, job_parameters j, experiment e
                   WHERE g.id=gene_id and e.id=j.exp_id
                   GROUP BY g.species, g.name, g.abbreviation, g.chromosome,
                            g.beginsite, g.endsite;"""
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
    query = """SELECT t.name, COUNT(DISTINCT r.model), 
                      COUNT(DISTINCT r.gene_id), COUNT(*)
               FROM transcription_factors t, regulatory_elements r
               WHERE r.id = t.reg_element
               GROUP BY t.name;"""
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

def queryElemForFacGeneExp(expID, geneID, facID, lvalue, lvalFrom, lvalTo, locFrom, locTo, sense):
    query = """SELECT r.id, r.beginning, r.length, r.sense, r.model, 
                      r.reg_sequence, r.la, r.la_slash, r.lq, r.ld, r.lpv, 
                      r.sc, r.sm, r.spv, r.ppv, r.gene_id, r.experiment_id 
               FROM regulatory_elements r, transcription_factors f 
               WHERE f.name='%s' AND f.reg_element=r.id AND 
                     r.experiment_id='%s' AND r.gene_id='%s'"""
    if sense != None:
        query = query + " AND r.sense=" + sense
    if lvalue != None and lvalFrom != None and lvalTo != None:
        query = query + " AND " + lvalue + " BETWEEN " + lvalFrom + " AND " + lvalTo
    if locFrom != None and locTo != None:
        query = query + " AND r.beginning BETWEEN " + locFrom + " AND " + locTo
    query = query + ";"
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

def queryElemForGeneExp(expID, geneID, lvalue, lvalFrom, lvalTo, locFrom, locTo):
    if lvalue != None and lvalFrom != None and lvalTo != None and locFrom != None and locTo != None:
        query = """SELECT * FROM regulatory_elements 
                   WHERE experiment_id='%s' AND gene_id='%s' 
                         AND %s BETWEEN %s AND %s 
                         AND beginning BETWEEN %s AND %s;"""
        cur.execute(query % (expID, geneID, lvalue, lvalFrom, lvalTo, locFrom, locTo))
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

def queryElemForFactor(facID):
    query = """SELECT r.id, e.dateof, e.location, e.experimenter, e.comparison,
                      e.species, g.name, r.beginning, r.length, r.sense, r.model
               FROM transcription_factors t, regulatory_elements r, 
                    genes g, experiment e
               WHERE t.name='%s' AND t.reg_element=r.id AND r.gene_id=g.id 
                     AND r.experiment_id=e.id;"""
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

def queryGeneDetails(geneID):
    query = """SELECT * FROM genes
               WHERE id='%s';"""
    cur.execute(query % (geneID))
    return cur.fetchall()

def queryExpForGene(geneID):
    query = """SELECT e.id, e.dateof, e.location, e.experimenter, e.comparison,
                      e.species, j.regulation
               FROM genes g, job_parameters j, experiment e
               WHERE g.id='%s' AND g.id=j.gene_id AND j.exp_id=e.id;"""
    cur.execute(query % (geneID))
    return cur.fetchall()

def queryMultipleFactors(facList, la, la_slash, lq, ld, species, comparison, experiment):
    query = """SELECT DISTINCT g.name, e.comparison, j.regulation, e.experimenter, 
                      e.species, e.dateof
               FROM genes g, experiment e, job_parameters j, 
                    regulatory_elements r, transcription_factors t
               WHERE g.id=j.gene_id AND e.id=j.exp_id AND g.id=r.gene_id 
                     AND e.id=r.experiment_id AND r.id=t.reg_element 
                     AND g.hidden=0 AND e.hidden=0 AND j.hidden=0 
                     AND r.hidden=0 AND t.hidden=0 AND (t.name='"""
    query = query + facList[0] + "'"
    i = 1
    while i < len(facList):
        query = query + " OR t.name='" + facList[i] + "'"
        i = i + 1
    query = query + ")"
    if species != None:
        query = query + " AND g.species='" + species + "'"
    if comparison != None:
        query = query + " AND e.comparison='" + comparison + "'"
    if experiment != None:
        query = query + " AND e.id='" + experiment + "'"
    if la != None:
        query = query + " AND r.la>=" + la
    if la_slash != None:
        query = query + " AND r.la_slash>=" + la_slash
    if lq != None:
        query = query + " AND r.lq>=" + lq
    if ld != None:
        query = query + " AND r.ld<=" + ld
    query = query + ";"
    print query
    cur.execute(query)
    return cur.fetchall()

