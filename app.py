from flask import Flask, jsonify, make_response, request, abort
from flask.ext.mongoengine import MongoEngine
from models import *

# Setup Flask and MongoDB Connection
#
app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {'DB': "sos"}

db = MongoEngine(app)

# List all officers
#
@app.route('/officers/', methods = ['GET'])
def get_officers():
    officers = Officer.objects.all()
    return officers.to_json()

# get a single officer
#
@app.route('/officers/<string:officer_id>', methods = ['GET'])
def get_officer(officer_id):
    officer = Officer.objects.get_or_404(pk=officer_id)
    return officer.to_json()

# add an officer
#
@app.route('/officers/', methods = ['POST'])
def create_officer():
    if not request.json or not 'firstName' in request.json:
        abort(400)
    if not 'lastName' in request.json:
        abort(400)
    if not 'employeeNum' in request.json:
        abort(400)
    if not 'email' in request.json:
        abort(400)
    officer1 = Officer()
    officer1.firstName = request.json['firstName']
    officer1.lastName = request.json['lastName']
    officer1.employeeNum = request.json['employeeNum']
    officer1.email = request.json['email']
    officer1.save()
    return officer1.to_json()

# display 404 error
#
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify( { 'error': 'Not found' } ), 404)

# delete an officer
#
@app.route('/officers/<string:officer_id>', methods = ['DELETE'])
def delete_officer(officer_id):
    officer = Officer.objects.get_or_404(pk=officer_id)        
    officer.delete()
    return make_response(jsonify( { 'success': 'officer deleted' } ), 200)

# udpate an officer
#
@app.route('/officers/<string:officer_id>', methods = ['PUT'])
def update_officer(officer_id):
    if not request.json:
        abort(400)
    if 'lastName' in request.json and type(request.json['lastName']) != unicode:
        abort(400)
    if 'firstName' in request.json and type(request.json['firstName']) != unicode:
        abort(400)
    if 'employeeNum' in request.json and type(request.json['employeeNum']) != int:
        abort(400)
    if 'email' in request.json and type(request.json['email']) != unicode:
        abort(400)
    officer = Officer.objects.get_or_404(pk=officer_id)
    if 'firstName' in request.json:
        officer.firstName = request.json['firstName']
    if 'lastName' in request.json:
        officer.lastName = request.json['lastName']
    if 'employeeNum' in request.json:
        officer.employeeNum = request.json['employeeNum']
    if 'email' in request.json:
        officer.email = request.json['email']
    officer.save()
    return officer.to_json()    
    

if __name__ == '__main__':
    app.run(debug = True)
 
