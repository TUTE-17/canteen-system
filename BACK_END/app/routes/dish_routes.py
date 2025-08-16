from flask import Blueprint, render_template

dish_bp = Blueprint('dish', __name__, url_prefix='/dishes')

@dish_bp.route('/menu')
def menu_page():
    return render_template('menupage.html')

@dish_bp.route('/admin')
def admin_menu():
    return render_template('adminmenu.html')