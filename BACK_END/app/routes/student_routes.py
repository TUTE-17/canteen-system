from flask import Blueprint, render_template

stud_bp = Blueprint("student",__name__,url_prefix="/student",template_folder='../../FRONT_END/CANTEEN/templates')

@stud_bp.route('/login', methods=['GET'])
def student_home():
    return render_template('student_login.html')

@stud_bp.route('/signup', methods=['GET'])
def signup_page():
    return render_template('studentsignup.html')

@stud_bp.route('/forgot-password', methods=['GET'])
def forgot_password_page():
    return render_template('forgot_password_student.html')

@stud_bp.route('/reset-password', methods=['GET'])
def reset_password_page():
    return render_template('reset_password.html')
