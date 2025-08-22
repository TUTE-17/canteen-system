from flask import Blueprint, render_template, request, jsonify
from controllers.order_controller import OrderController

order_bp = Blueprint("order", __name__, url_prefix="/order")

@order_bp.route("/orders")
def orders_page():
    return render_template("orders.html")


@order_bp.route("/create", methods=["POST"])
def create_order():
    data = request.get_json()
    response = OrderController.create_new_order(data)
    return jsonify(response)

@order_bp.route("/list", methods=["GET"])
def list_orders():
    response = OrderController.get_orders()
    return jsonify(response)

@order_bp.route("/delete/<int:order_id>", methods=["DELETE"])
def delete_order(order_id):
    response = OrderController.delete_order(order_id)
    return jsonify(response)
