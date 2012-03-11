
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
    return {'id': entry[0], 'name':entry[0], 'reg_element': entry[1]}
