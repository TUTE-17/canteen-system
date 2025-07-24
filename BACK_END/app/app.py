from flask import Flask
from routes.student_routes import stud_bp
from routes.staff_routes import staff_bp
from routes.order_routes import order_bp
from routes.payment_routes import payment_bp

def canteen():
    app=Flask(__name__)
    app.register_blueprint(stud_bp)
    app.register_blueprint(staff_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(payment_bp)

    return app

if __name__=="__main__":

  app=canteen()
  app.run(debug=True)
    