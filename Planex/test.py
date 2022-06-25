'''
from flask import Flask, render_template


app = Flask(__name__)

@app.route("/Fisica")

def index():
    return render_template('template.html')

def main():
    return  'main page'

'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('')
def hello():
    return render_template('template.html')