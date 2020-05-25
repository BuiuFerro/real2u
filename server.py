from flask import Flask, jsonify, request

import requests
import subprocess
import json

from script import criar_filtro

url = 'https://cdnb.artstation.com/p/assets/images/images/005/356/829/large/david-escribano-herrero-knight-colorf2-closeup.jpg?1490458528'

app = Flask(__name__)

@app.route("/", methods=['GET'])
def main():
    criar_filtro(url)
    return ""

if __name__ == "__main__":
    app.run(debug=True)