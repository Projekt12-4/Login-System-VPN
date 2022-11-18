from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
#from .models import Note
from . import db
from flask_sqlalchemy import SQLAlchemy
from .models import User
#import json

views = Blueprint('views', __name__)

# Should show the downloadable content, change jinja template to show the downloadable file from slqite template
@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'GET':
        #blobs = db.session.query(User.key_file).order_by(User.id).all()
        filename = "requirements.txt"
        with open(filename, 'r') as f:
            blob = f.read()
        
        
        return render_template("home.html", user=current_user, blob=blob, file=filename)

# Adding Notes -> Not needed
# @views.route('/delete-note', methods=['POST'])
# def delete_note():
#     note = json.loads(request.data)
#     noteId = note['noteId']
#     note = Note.query.get(noteId)
#     if note:
#         if note.user_id == current_user.id:
#             db.session.delete(note)
#             db.session.commit()

#     return jsonify({})
