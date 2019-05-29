from flask import render_template,request,redirect,url_for,abort
from . import main
from .forms import PitchForm,UpdateProfile,CommentForm
from .. import db,photos
from flask_login import login_required, current_user
from ..models import Pitch, User , Comment
import markdown2  
import datetime

@main.route('/',methods = ['GET','POST'])
def index():
    
    form = PitchForm()

    
    if form.validate_on_submit():

        pitch = form.pitch.data
        category = form.category.data
       
        new_pitch= Pitch(name=pitch,category=category)
        new_pitch.save_pitch()

    pitches = Pitch.query.all()
    title='Pitch '
    return render_template('index.html',title=title,new_form=form,pitches=pitches)

@main.route('/pitch/<int:id>', methods=['GET', 'POST'])
@login_required
def new_comment(id):
   pitch=Pitch.query.filter_by(id=id).first()
   form = CommentForm()
   comments = Comment.query.filter_by(pitch_id=id).all()
   print(comments)
   if form.validate_on_submit():
       comment = form.comment.data

       new_comment = Comment(comment=comment)
       new_comment.save_comment()
   title = "COMMENTS"
   return render_template('comments.html', comments=comments, comment_form=form, title=title, pitch=pitch)

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