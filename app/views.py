from flask import render_template
from app import app
 

@app.route('/')
def index():

    title='Pitch '
    return render_template('index.html',title=title)