from flask import Flask,request,jsonify
from backend_services.backend import (
    get_levels,
    get_titles
)

app = Flask(__name__)

@app.route("/test",methods=["GET","POST"])
def test_endpoint():
    """Test endpoint

    sample request: 
    curl -d '{"test":123}' -H "Content-Type: application/json" -X POST http://localhost:5000/test

    Returns:
        json
    """
    if request.method=='POST':
        request_dict = request.get_json()
        response = request_dict #actual response json here
        return jsonify(response)

@app.route("/get_levels",methods=["GET","POST"])
def levels_endpoint():
    """_summary_

    curl -H "Content-Type: application/json" -X POST http://localhost:5000/get_levels

    Returns:
        _type_: _description_
    """
    if request.method=='POST':
        response = get_levels() #actual response json here
        return jsonify(response)


@app.route("/get_titles",methods=["GET","POST"])
def titles_endpoint():
    """_summary_

    curl -d '{"LEVEL":"total"}' -H "Content-Type: application/json" -X POST http://localhost:5000/get_titles

    Returns:
        _type_: _description_
    """
    if request.method=='POST':
        request_dict = request.get_json()
        response = get_titles(request_dict) #actual response json here
        return jsonify(response)

if __name__=='__main__':
    app.run()