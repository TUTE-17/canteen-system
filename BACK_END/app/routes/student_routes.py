from flask import Blueprint, render_template

stud_bp = Blueprint('student', __name__, url_prefix='/student')

@stud_bp.route('/')
def student_home():
    return render_template('student_login.html')