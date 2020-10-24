from flask import render_template,request,redirect,url_for
from flask_login import login_required,current_user
from ..models import Category
from . import main
from flask import render_template
from .. import db,photos
from .forms import PitchForm


@main.route('/')
def index():
    '''
    Index page
    return
    '''
    message= "Welcome to Pitch Application!!"
    title= 'Pitch-app!'
    return render_template('index.html', message=message,title=title)