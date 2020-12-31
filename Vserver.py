from flask import Flask, jsonify, request, abort
from VjudoDAO import judoDAO

app = Flask(__name__)

@app.route('/')
def home():
    return app.send_static_file('VSindex.html')

#curl "http://127.0.0.1:5000/athlets"
@app.route('/athlets')
def getAll():
    results = judoDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/athlets/2"
@app.route('/athlets/<int:id>')
def findById(id):
    foundAthlet = judoDAO.findByID(id)

    return jsonify(foundAthlet)

@app.route('/athlets', methods=['POST'])
def create():
    #name, age, belt,  weight, gender
    if not request.json:
        abort(400)
    # other checking 
    athlet = {
        "name": request.json['name'],
        "age": request.json['age'],
        "belt": request.json['belt'],
        "weight": request.json['weight'],
        "gender": request.json['gender'],
    }
    values =(athlet['name'],athlet['age'],athlet['belt'], athlet['weight'], athlet['gender'])
    newId = judoDAO.create(values)
    athlet['id'] = newId
    return jsonify(athlet)

@app.route('/athlets/<int:id>', methods=['PUT'])
def update(id):
    foundAthlet = judoDAO.findByID(id)
    if not foundAthlet:
        abort(410)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    #name, age, belt,  weight, gender 
    if 'name' in reqJson:
        foundAthlet['name'] = reqJson['name']
    if 'age' in reqJson:
        foundAthlet['age'] = reqJson['age']
    if 'belt' in reqJson:
        foundAthlet['belt'] = reqJson['belt']
    if 'weight' in reqJson:
        foundAthlet['weight'] = reqJson['weight']    
    if 'gender' in reqJson:
        foundAthlet['gender'] = reqJson['gender']  
    values = (foundAthlet['name'],foundAthlet['age'],foundAthlet['belt'],foundAthlet['weight'],foundAthlet['gender'],foundAthlet['id'])
    judoDAO.update(values)
    return jsonify(foundAthlet)
        

    

@app.route('/athlets/<int:id>' , methods=['DELETE'])
def delete(id):
    judoDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)