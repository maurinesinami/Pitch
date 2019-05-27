from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,UpdateProfile
from .. import db,photos
from flask_login import login_required, current_user
from ..models import Pitch, User , Comment
import markdown2  

@main.route('/')
def index():

    title='Pitch '
    return render_template('index.html',title=title)

@main.route('/<uname>/new/pitch', methods = ['GET','POST'])
@login_required
def new_pitch(uname):
    form = PitchForm()
    user = User.query.filter_by(username = uname).first()

    
    if form.validate_on_submit():

        pitch = form.pitch.data
        category = form.categories.data
        originalDate = datetime.datetime.now()
        time = str(originalDate.time())
        time =time[0:5]
        date = str(originalDate)
        date = date[0:10]
        new_pitch= Pitch( content = pitch,user_id = user.id,time = time, date = date)
        new_pitch.save_pitch()
        pitches = Pitch.query.all()
    return render_template('new_pitch.html', new_form=form)
@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)
@main.route('/user/<uname>/update',methods = ['GET','POST'])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form) 
@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))   