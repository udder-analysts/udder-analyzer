from flask import Flask, url_for, render_template, request, jsonify
from parser import parse_gene_files
from werkzeug import secure_filename
from query import *
from parserloader import parse
import json

ALLOWED_EXTENTIONS = set(['csv'])

app = Flask(__name__, template_folder='public/templates', static_path='/public', static_folder='public')

@app.route('/')
def main():
    #url_for('static', filename='style.css')
    return render_template('main.html')

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENTIONS

@app.route('/horizontal', methods=['GET'])
def horizontal():
    return render_template('horizontal.html')

@app.route('/upload', methods=['GET', 'POST'])
def uploadData():
    if request.method == 'POST':

        fileList = []
		
        for file in request.files.getlist('upload-files'):
            if allowed_file(file.filename):
                fileList.append(file)

        sorted(fileList, key=lambda file: file.filename)
		
        if parse(fileList):
            return 'Files successfully parsed'
        else:
            return 'Error while parsing files'

    else:
        return render_template('StaticTestPage.html')

@app.route('/browse')
def browse():
    return render_template('browse.html')

#==================
#Data Request URLs
#==================

@app.route('/species', methods=['GET', 'POST'])
def getSpecies():
    arr = []
    for entry in querySpecies():
        dictEntry = {'id': entry[0], 'name': entry[0]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/comparisons', methods=['GET', 'POST'])
def getComparisons():
    arr = []
    for entry in queryComparisons():
        dictEntry = {'id': entry[0], 'comparison': entry[0], 
                     'species': entry[1]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments', methods=['GET', 'POST'])
def getExperiments():
    arr = []
    for entry in queryExperiments():
        dictEntry = {'id': entry[0], 'dateof': entry[1], 'location': entry[2],
                     'experimneter': entry[3], 'comparison': entry[4], 
                     'species': entry[5]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/genes', methods=['GET', 'POST'])
def getGenes():
    arr = []
    for entry in queryGenes():
        dictEntry = {'id': entry[0], 'name': entry[1], 
                     'abbreviation': entry[2], 'species': entry[3], 
                     'chromosome': entry[4], 'beginsite': entry[5], 
                     'endsite': entry[6]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/elements', methods=['GET', 'POST'])
def getElements():
    arr = []
    for entry in queryElements():
        dictEntry = {'id': entry[0], 'beginning': entry[1], 'length': entry[2], 
                     'sense': entry[3], 'model': entry[4], 
                     'reg_sequence': entry[5], 'la': entry[6], 
                     'la_slash': entry[7], 'lq': entry[8], 'ld': entry[9], 
                     'lpv': entry[10], 'sc': entry[11], 'sm': entry[12], 
                     'spv': entry[13], 'ppv': entry[14], 'gene_id': entry[15], 
                     'experiment_id': entry[16]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/factors', methods=['GET', 'POST'])
def getFactors():
    arr = []
    for entry in queryFactors():
        dictEntry = {'id': entry[0], 'name': entry[0], 'reg_element': entry[1]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/species/<specID>/comparisons', methods=['GET', 'POST'])
def getComparisonForSpecies(specID):
    arr = []
    for entry in queryCompForSpec(specID):
        dictEntry = {'id': entry[0], 'comparison': entry[0]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/species/<specID>/comparisons/<path:compID>/experiments', methods=['GET', 'POST'])
def getExpimentForCompSpec(specID, compID):
    arr = []
    for entry in queryExpForCompSpec(specID, compID):
        dictEntry = {'id': entry[0], 'dateof': entry[1], 'location': entry[2], 
                     'experimenter': entry[3], 'comparison': entry[4], 
                     'species': entry[5]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<expID>/genes', methods=['GET', 'POST'])
def getGenesForExp(expID):
    arr = []
    if request.method == 'POST' and request.args.getlist('reg')[0]:
        result = queryGenesForExpRegulated(expID, request.args.getlist('reg')[0])
    else:
        result = queryGenesForExp(expID)
    for entry in result:
        dictEntry = {'id': entry[0], 'name': entry[1], 'abbreviation': entry[2],                     
                     'species': entry[3], 'chromosome': entry[4], 
                     'beginsite': entry[5], 'endsite': entry[6]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<expID>/genes/<geneID>/factors', methods=['GET', 'POST'])
def getFactorsForGeneExp(expID, geneID):
    arr = []
    for entry in queryFactorsForGeneExp(expID, geneID):
        dictEntry = {'id': entry[0], 'name': entry[0], 'reg_element': entry[1]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<expID>/genes/<geneID>/factors/<facID>/elements', methods=['GET', 'POST'])
def getElemForFacGeneExp(expID, geneID, facID):
    arr = []
    for entry in queryElemForFacGeneExp(expID, geneID, facID):
        dictEntry = {'id': entry[0], 'beginning': entry[1], 'length': entry[2],                      
                     'sense': entry[3], 'model': entry[4], 
                     'reg_sequence': entry[5], 'la': entry[6], 
                     'la_slash': entry[7], 'lq': entry[8], 'ld': entry[9], 
                     'lpv': entry[10], 'sc': entry[11], 'sm': entry[12], 
                     'spv': entry[13], 'ppv': entry[14], 'gene_id': entry[15], 
                     'experiment_id': entry[16]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/comparisons/<path:compID>/experiments', methods=['GET', 'POST'])
def getExpForComp(compID):
    arr = []
    for entry in queryExpForComp(compID):
        dictEntry = {'id': entry[0], 'dateof': entry[1], 'location': entry[2], 
                     'experimneter': entry[3], 'comparison': entry[4], 
                     'species': entry[5]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<expID>/genes/<geneID>/elements', methods=['GET', 'POST'])
def getElemForGeneExp(expID, geneID):
    arr = []
    for entry in queryElemForGeneExp(expID, geneID):
        dictEntry = {'id': entry[0], 'beginning': entry[1], 'length': entry[2],                      
                     'sense': entry[3], 'model': entry[4], 
                     'reg_sequence': entry[5], 'la': entry[6], 
                     'la_slash': entry[7], 'lq': entry[8], 'ld': entry[9], 
                     'lpv': entry[10], 'sc': entry[11], 'sm': entry[12], 
                     'spv': entry[13], 'ppv': entry[14], 'gene_id': entry[15], 
                     'experiment_id': entry[16]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/genes/<geneID>/elements', methods=['GET', 'POST'])
def getElemForGene(geneID):
    arr = []
    for entry in queryElemForGene(geneID):
        dictEntry = {'id': entry[0], 'beginning': entry[1], 'length': entry[2],                      
                     'sense': entry[3], 'model': entry[4], 
                     'reg_sequence': entry[5], 'la': entry[6], 
                     'la_slash': entry[7], 'lq': entry[8], 'ld': entry[9], 
                     'lpv': entry[10], 'sc': entry[11], 'sm': entry[12], 
                     'spv': entry[13], 'ppv': entry[14], 'gene_id': entry[15], 
                     'experiment_id': entry[16]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/factors/<facID>/elements', methods=['GET', 'POST'])
def getElemForFactor(facID):
    arr = []
    for entry in queryElemForFactor(facID):
        dictEntry = {'id': entry[0], 'beginning': entry[1], 'length': entry[2],                      
                     'sense': entry[3], 'model': entry[4], 
                     'reg_sequence': entry[5], 'la': entry[6], 
                     'la_slash': entry[7], 'lq': entry[8], 'ld': entry[9], 
                     'lpv': entry[10], 'sc': entry[11], 'sm': entry[12], 
                     'spv': entry[13], 'ppv': entry[14], 'gene_id': entry[15], 
                     'experiment_id': entry[16]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<expID>/genes/<geneID>/elements/<elemID>', methods=['GET', 'POST'])
def getSingleElemForGeneExp(expID, geneID, elemID):
    arr = []
    for entry in querySingleElemForGeneExp(expID, geneID, elemID):
        dictEntry = {'id': entry[0], 'beginning': entry[1], 'length': entry[2],                      
                     'sense': entry[3], 'model': entry[4], 
                     'reg_sequence': entry[5], 'la': entry[6], 
                     'la_slash': entry[7], 'lq': entry[8], 'ld': entry[9], 
                     'lpv': entry[10], 'sc': entry[11], 'sm': entry[12], 
                     'spv': entry[13], 'ppv': entry[14], 'gene_id': entry[15], 
                     'experiment_id': entry[16]}
        arr.append(dictEntry)
    return json.dumps(arr)

#====================
#POST Parameter URLs
#====================

@app.route('/test', methods=['GET'])
def runTest():
    return render_template('test.html')

@app.route('/parameters', methods=['GET', 'POST'])
def getParameters():
    print request.args
    print request.args.getlist('fname')[0]
    return 'Done'

#===============
#Error Handlers
#===============

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html'), 404

@app.errorhandler(500)
def server_error(error):
    return error, 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

