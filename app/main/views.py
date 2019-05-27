from flask import render_template
from . import main
from .forms import PitchForm
from flask_login import login_required 

@main.route('/')
def index():

    title='Pitch '
    return render_template('index.html',title=title)

@main.route('/create/pitch', methods = ['GET','POST'])
@login_required
def new_pitch(id):
    form = PitchForm()
    

    pitch = form.pitch.data
    category = form.categories.data
    originalDate = datetime.datetime.now()
    time = str(originalDate.time())
    time =time[0:5]
    date = str(originalDate)
    date = date[0:10]
    new_pitch= Pitch( content = pitch,user_id = user.id,time = time, date = date)
    
    return render_template('create_pitch.html', new_form=form)