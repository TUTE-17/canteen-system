from flask import Blueprint, render_template

staff_bp = Blueprint('staff', __name__, url_prefix='/staff')

@staff_bp.route('/')
def staff_home():
    return render_template('staff_login.html')