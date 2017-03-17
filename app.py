import os

from flask import Flask
from flask import Flask, render_template, jsonify
from flask import Flask, render_template, request
from flask import request
from imdbpie import Imdb


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
    
    
if __name__ == "__main__":
    app.run()