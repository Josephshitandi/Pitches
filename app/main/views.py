from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from ..models import Pitches, User, Comments
from . import main
from flask import render_template
from .. import db,photos
from .forms import PitchForm,CommentForm, UpdateProfile


@main.route('/')
def index():
    '''
    Index page
    return
    '''
    message= "Hello, welcome to Pitch-App!!"
    title= 'Pitch-app!'
    return render_template('index.html', message=message,title=title)