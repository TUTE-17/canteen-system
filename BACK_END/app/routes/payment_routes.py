from flask import Blueprint, request, jsonify, render_template
from controllers.payment_controller import PaymentController

payment_bp = Blueprint("payment", __name__)

@payment_bp.route("/payment/", methods=["GET"])
def payment_page():
    order_id = request.args.get("order_id")
    total = request.args.get("total")
    return render_template("payment.html", order_id=order_id, total=total)


@payment_bp.route("/payment/create", methods=["POST"])
def create_payment():
    data = request.get_json()
    order_id = data.get("order_id")
    amount = data.get("total")
    order = PaymentController.create_order(order_id, amount)
    return jsonify(order)


@payment_bp.route("/payment/verify", methods=["POST"])
def verify_payment():
    order_id = request.args.get("order_id")
    data = request.json  

    razorpay_payment_id = data.get("razorpay_payment_id")
    razorpay_order_id = data.get("razorpay_order_id")
    razorpay_signature = data.get("razorpay_signature")



    result = PaymentController.verify_payment(order_id, razorpay_payment_id, razorpay_order_id, razorpay_signature)
    return jsonify(result)
