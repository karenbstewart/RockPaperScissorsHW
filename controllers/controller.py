from app import app
from flask import render_template
from models.player import Player 

@app.route('/')
def index():
    return "Hello World"

@app.route('/rock/paper')
def paper_win():
    return render_template ('index.html')
