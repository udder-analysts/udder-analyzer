from flask import Flask, url_for, render_template, request, redirect
from werkzeug import secure_filename
from query import *
from queryResources import *
from parserloader import parse
import json, urllib

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
        return redirect('/#upload')

@app.route('/browse')
def browse():
    return render_template('browse.html')

#==================
#Data Request URLs
#==================

@app.route('/species', methods=['GET', 'POST'])
def getSpecies():
    arr = []
    if request.method == 'POST' and request.args.getlist('sortby')[0]:
        result = querySortedSpecies()
    else:
        result = querySpecies()
    for entry in result:
        dictEntry = getSpeciesDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/comparisons', methods=['GET', 'POST'])
def getComparisons():
    arr = []
    if request.method == 'POST' and request.args.getlist('sortby')[0]:
        result = querySortedComparisons()
    else:
        result = queryComparisons()
    for entry in result:
        dictEntry = getCompDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments', methods=['GET', 'POST'])
def getExperiments():
    arr = []
    if request.method == 'POST' and request.args.getlist('sortby')[0]:
        result = querySortedExperiments()
    else:
        result = queryExperiments()
    for entry in result:
        dictEntry = getExpDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/genes', methods=['GET', 'POST'])
def getGenes():
    arr = []
    if request.method == 'POST' and request.args.getlist('sortby')[0]:
        result = querySortedGenes()
    else:
        result = queryGenes()
    for entry in result:
        dictEntry = getGeneDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/elements', methods=['GET', 'POST'])
def getElements():
    arr = []
    if request.method == 'POST' and request.args.getlist('sortby')[0]:
        result = querySortedElements()
    else:
        result = queryElements()
    for entry in result:
        dictEntry = getElemDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/factors', methods=['GET', 'POST'])
def getFactors():
    arr = []
    if request.method == 'POST' and request.args.getlist('sortby')[0]:
        result = querySortedFactors()
    else:
        result = queryFactors()
    for entry in result:
        dictEntry = getFactorDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/species/<path:specID>/comparisons', methods=['GET', 'POST'])
def getComparisonForSpecies(specID):
    arr = []
    specID = urllib.unquote(specID)
    if request.method == 'POST' and request.args.getlist('sortby')[0]:
        result = querySortedCompForSpec(specID)
    else:
        result = queryCompForSpec(specID)
    for entry in result:
        dictEntry = {'id': entry[0], 'comparison': entry[0]}
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/species/<path:specID>/comparisons/<path:compID>/experiments', methods=['GET', 'POST'])
def getExperimentForCompSpec(specID, compID):
    arr = []
    specID = urllib.unquote(specID)
    compID = urllib.unquote(compID)
    for entry in queryExpForCompSpec(specID, compID):
        dictEntry = getExpDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<path:expID>/genes', methods=['GET', 'POST'])
def getGenesForExp(expID):
    arr = []
    expID = urllib.unquote(expID)
    if request.method == 'POST' and request.args.getlist('reg')[0]:
        result = queryGenesForExpRegulated(expID, request.args.getlist('reg')[0])
    else:
        result = queryGenesForExp(expID)
    for entry in result:
        dictEntry = getGeneDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<path:expID>/genes/<path:geneID>/factors', methods=['GET', 'POST'])
def getFactorsForGeneExp(expID, geneID):
    arr = []
    expID = urllib.unquote(expID)
    geneID = urllib.unquote(geneID)
    for entry in queryFactorsForGeneExp(expID, geneID):
        dictEntry = getFactorDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<path:expID>/genes/<path:geneID>/factors/<path:facID>/elements', methods=['GET', 'POST'])
def getElemForFacGeneExp(expID, geneID, facID):
    arr = []
    expID = urllib.unquote(expID)
    geneID = urllib.unquote(geneID)
    facID = urllib.unquote(facID)
    for entry in queryElemForFacGeneExp(expID, geneID, facID):
        dictEntry = getElemDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/comparisons/<path:compID>/experiments', methods=['GET', 'POST'])
def getExpForComp(compID):
    arr = []
    compID = urllib.unquote(compID)
    for entry in queryExpForComp(compID):
        dictEntry = getExpDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<path:expID>/genes/<path:geneID>/elements', methods=['GET', 'POST'])
def getElemForGeneExp(expID, geneID):
    arr = []
    expID = urllib.unquote(expID)
    geneID = urllib.unquote(geneID)
    if request.method == 'POST':
        if request.args.getlist('sortby'):
            result = queryElemForGeneExpSort(expID, geneID, request.args.getlist('sortby')[0])
        elif request.args.getlist('lvalue'):
            result = queryElemForGeneExpLvalue(expID, geneID, request.args.getlist('lvalue')[0])
        else:
            result = queryElemForGeneExp(expID, geneID)
    else:
        result = queryElemForGeneExp(expID, geneID)
    for entry in result:
        dictEntry = getElemDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/genes/<path:geneID>/elements', methods=['GET', 'POST'])
def getElemForGene(geneID):
    arr = []
    geneID = urllib.unquote(geneID)
    for entry in queryElemForGene(geneID):
        dictEntry = getElemDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/factors/<path:facID>/elements', methods=['GET', 'POST'])
def getElemForFactor(facID):
    arr = []
    facID = urllib.unquote(facID)
    for entry in queryElemForFactor(facID):
        dictEntry = getElemDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<path:expID>/genes/<path:geneID>/elements/<path:elemID>', methods=['GET', 'POST'])
def getSingleElemForGeneExp(expID, geneID, elemID):
    arr = []
    expID = urllib.unquote(expID)
    geneID = urllib.unquote(geneID)
    elemID = urllib.unquote(elemID)
    for entry in querySingleElemForGeneExp(expID, geneID, elemID):
        dictEntry = getElemDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/elementDetails/<elemID>', methods=['GET'])
def getElementDetails(elemID):
    arr = []
    elemID = urllib.unquote(elemID)
    for entry in queryElementDetails(elemID):
        dictEntry = {'id': entry[0], 'beginning': entry[1], 'length': entry[2],
                     'sense': entry[3], 'model': entry[4], 
                     'reg_sequence': entry[5], 'la': entry[6], 
                     'la_slash': entry[7], 'lq': entry[8], 'ld': entry[9], 
                     'lpv': entry[10], 'sc': entry[11], 'sm': entry[12], 
                     'spv': entry[13], 'ppv': entry[14], 'gene_id': entry[15], 
                     'experiment_id': entry[16], 'dateof': entry[17], 
                     'location': entry[18], 'experimenter': entry[19], 
                     'comparison': entry[20], 'species': entry[21], 
                     'factor_name': entry[22]}
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
    #return render_template('error.html'), 404
    return '404 - Page Not Found'

@app.errorhandler(500)
def server_error(error):
    return error, 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)

