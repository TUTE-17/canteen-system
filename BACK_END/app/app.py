from flask import Flask,render_template
from routes.student_routes import stud_bp
from routes.staff_routes import staff_bp
from routes.order_routes import order_bp
from routes.payment_routes import payment_bp

def canteen():
    app=Flask(__name__,template_folder='FRONT_END/CANTEEN')
    app.register_blueprint(stud_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(payment_bp)

    @app.route('/')
    def index():
      return render_template('index.html')
    
    return app

if __name__=="__main__":
  app=canteen()
  app.run(debug=True)
    