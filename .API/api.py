#!/usr/bin/env python3
from flask import Flask, jsonify, request
from flask_cors import CORS

import os

# Non-mutexed global variable
companies = [
    {
        "id": "1",
        "name": "Vincy Productions"
    },
    {
        "id": "2",
        "name": "Kelly Incorporated"
    }
]

api = Flask(__name__)
# Enable CORS responses allowing all origins for testing purposes
CORS(api, resources={r"/*": {"origins": "*"}})

@api.route('/companies', methods=['GET'])
def get_companies():
    r = jsonify(companies)
    return r

@api.route('/companies', methods=['POST'])
def add_company():
    global companies

    content = request.json
    id = content['id']
    name = content['name']
    companies += [{ "id": id, "name": name }]

    r = jsonify(companies)
    return r

@api.route('/companies', methods=['DELETE'])
def remove_company():
    global companies

    content = request.json
    id = content['id']

    deleteCompany(id)

    r = jsonify(companies)
    return r

def deleteCompany(id):
    global companies

    for i, company in enumerate(companies):
        if company['id'] == id:
            print('Deleting: [' + company["id"] + ", " + company["name"] + "]")
            companies.pop(i)

if __name__ == '__main__':
    address = os.environ.get('API_ADDRESS', '0.0.0.0')
    port = os.environ.get('API_PORT', '5000')

    api.run(
        host=address,
        port=port,
        debug=True
    ) 
