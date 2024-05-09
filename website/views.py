from flask import Blueprint, render_template,request, flash, jsonify
# render templates is so we can import our templates so we can view it
from flask_login import login_required, current_user
from .models import Note
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method=="POST":
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note=Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')
    return render_template('home.html', user=current_user)

@views.route('/delete-note', methods=['POST'])
# takes in data from POST request
def delete_note():
    # loads it in as a json object as a python dict
    note=json.loads(request.data)
    # access the noteId attribute
    noteId=note['noteId']
    # look for the noteId if it exists
    note=Note.query.get(noteId)
    if note:
        # if we own this note,then we will delete the note
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
            # return an empty response
    return jsonify({})