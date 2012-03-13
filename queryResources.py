
def getSpeciesDict(entry):
    return {'id': entry[0], 'name': entry[0]}

def getCompDict(entry):
    return {'id': entry[0], 'comparison': entry[0], 'species': entry[1]}

def getExpDict(entry):
    return {'id': entry[0], 'dateof': entry[1], 'location': entry[2], 
            'experimenter': entry[3], 'comparison': entry[4], 
            'species': entry[5]}

def getGeneDict(entry):
    return {'id': entry[0], 'name': entry[1], 'abbreviation': entry[2],
            'species': entry[3], 'chromosome': entry[4], 'beginsite': entry[5],
            'endsite': entry[6]}

def getElemDict(entry):
    return {'id': entry[0], 'beginning': entry[1], 'length': entry[2],
            'sense': entry[3], 'model': entry[4], 'reg_sequence': entry[5],
            'la': entry[6], 'la_slash': entry[7], 'lq': entry[8], 
            'ld': entry[9], 'lpv': entry[10], 'sc': entry[11], 'sm': entry[12],
            'spv': entry[13], 'ppv': entry[14], 'gene_id': entry[15],
            'experiment_id': entry[16]}

def getFactorDict(entry):
    return {'id': entry[0], 'name': entry[0], 'reg_element': entry[1]}

def getCompForSpecDict(entry):
    return {'id': entry[0], 'comparison': entry[0]}

def getElemDetailDict(entry):
    return {'id': entry[0], 'beginning': entry[1], 'length': entry[2],
            'sense': entry[3], 'model': entry[4], 'reg_sequence': entry[5],
            'la': entry[6], 'la_slash': entry[7], 'lq': entry[8], 
            'ld': entry[9], 'lpv': entry[10], 'sc': entry[11], 'sm': entry[12],
            'spv': entry[13], 'ppv': entry[14], 'gene_id': entry[15],
            'experiment_id': entry[16], 'dateof': entry[17], 
            'location': entry[18], 'experimenter': entry[19], 
            'comparison': entry[20], 'species': entry[21], 
            'factor_name': entry[22]}

def getDistinctFactorDict(entry):
    return {'id': entry[0], 'name': entry[0]}

def getGeneDictWithExpInfo(entry):
    return {'id': entry[0], 'species': entry[1], 'name': entry[2], 
            'abbreviation': entry[3], 'chromosome': entry[4], 
            'beginsite': entry[5], 'endsite': entry[6],
            'comparisons': entry[7], 'experiments': entry[8]}

def getExpForGeneDict(entry):
    return {'id': entry[0], 'dateof': entry[1], 'location': entry[2],
            'experimenter': entry[3], 'comparison': entry[4], 
            'species': entry[5], 'regulation': entry[6]}

def getMultipleFactorDict(entry):
    return {'name': entry[0], 'comparison': entry[1], 'regulation': entry[2],
            'experimenter': entry[3], 'species': entry[4], 'dateof': entry[5]}

def getFactorSummaryDict(entry):
    return {'id': entry[0], 'name': entry[0], 'models': entry[1], 'genes': entry[2], 
            'occurences': entry[3]}

def getElemForFacDict(entry):
    return {'id': entry[0], 'dateof': entry[1], 'location': entry[2], 
            'experimenter': entry[3], 'comparison': entry[4], 
            'species': entry[5], 'gene_name': entry[6], 'beginning': entry[7],
            'length': entry[8], 'sense': entry[9], 'model': entry[10]}
