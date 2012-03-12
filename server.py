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
    if request.args.getlist('sortby') and request.args.getlist('order'):
        result = querySpecies(request.args.getlist('sortby')[0], request.args.getlist('order')[0])
    else:
        result = querySpecies(None, None)
    for entry in result:
        dictEntry = getSpeciesDict(entry)
        print dictEntry
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/comparisons', methods=['GET', 'POST'])
def getComparisons():
    arr = []
    if request.args.getlist('sortby') and request.args.getlist('order'):
        result = queryComparisons(request.args.getlist('sortby')[0], request.args.getlist('order')[0])
    else:
        result = queryComparisons(None, None)
    for entry in result:
        dictEntry = getCompDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments', methods=['GET', 'POST'])
def getExperiments():
    arr = []
    if request.args.getlist('sortby') and request.args.getlist('order'):
        result = queryExperiments(request.args.getlist('sortby')[0], request.args.getlist('order')[0])
    else:
        result = queryExperiments(None, None)
    for entry in result:
        dictEntry = getExpDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/genes', methods=['GET', 'POST'])
def getGenes():
    arr = []
    if request.args.getlist('sortby') and request.args.getlist('order'):
        sortby = request.args.getlist('sortby')[0]
        order = request.args.getlist('order')[0]
        result = queryGenes(sortby, order, None)
    elif request.args.getlist('reg'):
        reg = request.args.getlist('reg')[0]
        result = queryGenes(None, None, reg)
    else:
        result = queryGenes(None, None, None)
    for entry in result:
        dictEntry = getGeneDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/elements', methods=['GET', 'POST'])
def getElements():
    arr = []
    if request.args.getlist('sortby') and request.args.getlist('order'):
        result = queryElements(request.args.getlist('sortby')[0], request.args.getlist('order')[0])
    else:
        result = queryElements(None, None)
    for entry in result:
        dictEntry = getElemDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/factors', methods=['GET', 'POST'])
def getFactors():
    arr = []
    if request.args.getlist('sortby') and request.args.getlist('order'):
        result = queryFactors(request.args.getlist('sortby')[0], request.args.getlist('order')[0])
    else:
        result = queryFactors(None, None)
    for entry in result:
        dictEntry = getFactorDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/species/<path:specID>/comparisons', methods=['GET', 'POST'])
def getComparisonForSpecies(specID):
    arr = []
    specID = urllib.unquote(specID)
    if request.args.getlist('sortby') and request.args.getlist('order'):
        result = queryCompForSpec(specID, request.args.getlist('sortby')[0], request.args.getlist('order')[0])
    else:
        result = queryCompForSpec(specID, None, None)
    for entry in result:
        dictEntry = getCompForSpecDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/species/<path:specID>/comparisons/<path:compID>/experiments', methods=['GET', 'POST'])
def getExperimentForCompSpec(specID, compID):
    arr = []
    specID = urllib.unquote(specID)
    compID = urllib.unquote(compID)
    if request.args.getlist('sortby') and request.args.getlist('order'):
        result = queryExpForCompSpec(specID, compID, request.args.getlist('sortby')[0], request.args.getlist('order')[0])
    else:
        result = queryExpForCompSpec(specID, compID, None, None)
    for entry in result:
        dictEntry = getExpDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<path:expID>/genes', methods=['GET', 'POST'])
def getGenesForExp(expID):
    arr = []
    expID = urllib.unquote(expID)
    if request.args.getlist('reg'):
        result = queryGenesForExp(expID, None, None, request.args.getlist('reg')[0])
    elif request.args.getlist('sortby') and request.args.getlist('order'):
        result = queryGenesForExp(expID, request.args.getlist('sortby')[0], request.args.getlist('order')[0], None)
    else:
        result = queryGenesForExp(expID, None, None, None)
    for entry in result:
        dictEntry = getGeneDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<path:expID>/genes/<path:geneID>/factors', methods=['GET', 'POST'])
def getFactorsForGeneExp(expID, geneID):
    arr = []
    expID = urllib.unquote(expID)
    geneID = urllib.unquote(geneID)
    if request.args.getlist('sortby') and request.args.getlist('order'):
        result = queryFactorsForGeneExp(expID, geneID, request.args.getlist('sortby')[0], request.args.getlist('order')[0])
    else:
        result = queryFactorsForGeneExp(expID, geneID, None, None)
    for entry in result:
        dictEntry = getDistinctFactorDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<path:expID>/genes/<path:geneID>/factors/<path:facID>/elements', methods=['GET', 'POST'])
def getElemForFacGeneExp(expID, geneID, facID):
    arr = []
    expID = urllib.unquote(expID)
    geneID = urllib.unquote(geneID)
    facID = urllib.unquote(facID)
    if request.args.getlist('sortby') and request.args.getlist('order'):
        result = queryElemForFacGeneExp(expID, geneID, facID, request.args.getlist('sortby')[0], request.args.getlist('order')[0])
    else:
        result = queryElemForFacGeneExp(expID, geneID, facID, None, None)
    for entry in result:
        dictEntry = getElemDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/comparisons/<path:compID>/experiments', methods=['GET', 'POST'])
def getExpForComp(compID):
    arr = []
    compID = urllib.unquote(compID)
    if request.args.getlist('sortby') and request.args.getlist('order'):
        result = queryExpForComp(compID, request.args.getlist('sortby')[0], request.args.getlist('order')[0])
    else:
        result = queryExpForComp(compID, None, None)
    for entry in result:
        dictEntry = getExpDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/experiments/<path:expID>/genes/<path:geneID>/elements', methods=['GET', 'POST'])
def getElemForGeneExp(expID, geneID):
    arr = []
    expID = urllib.unquote(expID)
    geneID = urllib.unquote(geneID)
    if request.args.getlist('sortby') and request.args.getlist('order'):
        sortby = request.args.getlist('sortby')[0]
        order = request.args.getlist('order')[0]
        result = queryElemForGeneExp(expID, geneID, sortby, order, None, None, None, None, None)
    elif request.args.getlist('lvalue') and request.args.getlist('lvalFrom') and request.args.getlist('lvalTo'):
        lvalue = request.args.getlist('lvalue')[0]
        lvalFrom = request.args.getlist('lvalFrom')[0]
        lvalTo = request.args.getlist('lvalTo')[0]
        result = queryElemForGeneExp(expID, geneID, None, None, lvalue, lvalFrom, lvalTo, None, None)
    elif request.args.getlist('locFrom') and request.args.getlist('locTo'):
        locFrom = request.args.getlist('locFrom')[0]
        locTo = request.args.getlist('locTo')[0]
        result = queryElemForGeneExp(expID, geneID, None, None, None, None, None, locFrom, locTo)
    else:
        result = queryElemForGeneExp(expID, geneID, None, None, None, None, None, None, None)
    for entry in result:
        dictEntry = getElemDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/genes/<path:geneID>/elements', methods=['GET', 'POST'])
def getElemForGene(geneID):
    arr = []
    geneID = urllib.unquote(geneID)
    if request.args.getlist('sortby') and request.args.getlist('order'):
        sortby = request.args.getlist('sortby')[0]
        order = request.args.getlist('order')[0]
        result = queryElemForGene(geneID, sortby, order)
    else:
        result = queryElemForGene(geneID, None, None)
    for entry in result:
        dictEntry = getElemDict(entry)
        arr.append(dictEntry)
    return json.dumps(arr)

@app.route('/factors/<path:facID>/elements', methods=['GET', 'POST'])
def getElemForFactor(facID):
    arr = []
    facID = urllib.unquote(facID)
    if request.args.getlist('sortby') and request.args.getlist('order'):
        sortby = request.args.getlist('sortby')[0]
        order = request.args.getlist('order')[0]
        result = queryElemForFactor(facID, sortby, order)
    else:
        result = queryElemForFactor(facID, None, None) 
    for entry in result:
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
    entry = queryElementDetails(elemID)[0]
    print entry
    dictEntry = getElemDetailDict(entry)
        #arr.append(dictEntry)
    return json.dumps(dictEntry)

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

