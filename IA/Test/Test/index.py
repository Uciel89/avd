from flask import Flask, jsonify, request
import json

import requests

# from test_bloom import *
# from test_gpt2 import *
from test_openai import gpt3
from flask_cors import CORS


app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route("/1")
def server_info():
    personas = [
        {
            "nombre" : "sergio",
            "apellido" : "decoppet"
        }
    ]
    
    return jsonify(personas)



@app.route("/query_ia", methods=["POST", "GET"]) 
def ia_response():
    
    str_query = request.args.get('str_query')
    output = gpt3(str_query)
    StrA = " ".join(output)
    dicc_output = {'response' : f'{StrA}'}
    return jsonify(dicc_output)
    


if __name__ == "__main__":
    app.run(debug=True)


# http://localhost:5000/query_ia?str_query=adios