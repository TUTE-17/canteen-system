from flask import Blueprint, render_template

staff_bp = Blueprint('staff', __name__, url_prefix='/staff')

@staff_bp.route('/signup',methods=['GET'])
def staff_signup():
    return render_template('staffsignup.html')

@staff_bp.route('/login',methods=['GET'])
def staff_login():
    return render_template('staff_login.html')


