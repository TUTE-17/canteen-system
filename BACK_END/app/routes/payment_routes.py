from flask import Blueprint, render_template

payment_bp = Blueprint('payment', __name__, url_prefix='/payment')

@payment_bp.route('/payment')
def student_home():
    return render_template('payment.html')

@payment_bp.route('/signup')
def student_signup():
    return render_template('studentsignup.html')