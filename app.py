import os
import sys
import logging
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import logging
from text_sim.serve import get_model_api
import argparse

# load the model
model_api = get_model_api()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


# API route
@app.route('/api', methods=['POST'])
def api():

    input_data1 = request.form['rawtext1']
    input_data2 = request.form['rawtext2']
    
    output_data = model_api(input_data1, input_data2)
    
    return render_template("index.html", input_data1=input_data1, input_data2=input_data2, output_data=output_data)

if __name__ == '__main__':
    # This is used when running locally.
    app.run(debug=True)
