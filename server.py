from flask import Flask, url_for, render_template, request, jsonify
from parser import parse_gene_files
from werkzeug import secure_filename
from query import querySpecies
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

@app.route('/species')
def getSpecies():
	arr = []
	for entry in querySpecies():
		dictEntry = {'name': entry[0]}
		arr.append(json.dumps(dictEntry))
	return json.dumps(arr)

@app.route('/comparisons')
def getComparisons():
	return 'Not yet implemented'

@app.route('/experiments')
def getExperiments():
	return 'Not yet implemented'

@app.route('/genes')
def getGenes():
	return 'Not yet implemented'

@app.route('/elements')
def getElements():
	return 'Not yet implemented'

@app.route('/factors')
def getFactors():
	return 'Not yet implemented'

@app.errorhandler(404)
def page_not_found(error):
	return render_template('error.html'), 404

@app.errorhandler(500)
def server_error(error):
	return error, 500

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=80)

