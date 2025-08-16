from flask import Blueprint, render_template

order_bp = Blueprint('order', __name__, url_prefix='/order')

@order_bp.route('/orders')
def menu():
    return render_template('orders.html')

@order_bp.route('/menu')
def menu_page():
    return render_template('menupage.html')