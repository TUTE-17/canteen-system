import os
from flask import Flask, render_template

from routes.student_routes import stud_bp
from routes.staff_routes import staff_bp
from routes.order_routes import order_bp
from routes.payment_routes import payment_bp
from routes.dish_routes import dish_bp
from controllers import student_controller
from controllers import staff_controller
from controllers import order_controller
from controllers import dish_controller
base_dir = os.path.abspath(os.path.dirname(__file__))
template_dir = os.path.join(base_dir, '../../FRONT_END/CANTEEN/templates')
static_dir = os.path.join(base_dir, '../../FRONT_END/CANTEEN/static')

app = Flask(__name__, template_folder=os.path.abspath(template_dir), static_folder=os.path.abspath(static_dir))

app.register_blueprint(stud_bp)
app.register_blueprint(staff_bp)
app.register_blueprint(order_bp)
app.register_blueprint(payment_bp)
app.register_blueprint(dish_bp)
@app.route('/')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
