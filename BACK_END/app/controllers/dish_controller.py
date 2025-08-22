from flask import request, jsonify
from models.dish_model import DishModel
from routes.dish_routes import dish_bp


@dish_bp.route("/", methods=["GET"])
def get_dishes():
    dishes = DishModel.get_all_dishes()
    return jsonify(dishes), 200


@dish_bp.route("/", methods=["POST"])
def create_dish():
    data = request.json
    photo = data.get("photo")      
    dishname = data.get("dishname")
    quantity = data.get("quantity")
    price = data.get("price")
    available = data.get("available", True)

    if not dishname or quantity is None or price is None:
        return jsonify({"error": "Missing required fields"}), 400

    try:
        quantity = int(quantity)
        price = float(price)
    except ValueError:
        return jsonify({"error": "Quantity must be int and price must be float"}), 400

    new_dish = DishModel.create_dish(photo, dishname, quantity, price, available)
    if "error" in new_dish:
        return jsonify(new_dish), 400

    return jsonify(new_dish), 201

@dish_bp.route("/<dish_id>", methods=["PUT"])
def update_dish(dish_id):
    dish = DishModel.get_dish_by_id(dish_id)
    if not dish:
        return jsonify({"error": "Dish not found"}), 404

    data = request.json
    updates = {
        "dishname": data.get("dishname", dish.get("dishname")),
        "quantity": int(data.get("quantity", dish.get("quantity"))),
        "price": float(data.get("price", dish.get("price"))),
        "photo": data.get("photo", dish.get("photo")),
        "available": data.get("available", dish.get("available"))
    }

    updated = DishModel.update_dish(dish_id, updates)
    if "error" in updated:
        return jsonify(updated), 400

    return jsonify(updated), 200

@dish_bp.route("/<dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    deleted = DishModel.delete_dish(dish_id)
    if not deleted:
        return jsonify({"error": "Dish not found or could not delete"}), 404
    return jsonify({"message": "Dish deleted"}), 200

