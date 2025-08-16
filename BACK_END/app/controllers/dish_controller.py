from flask import Blueprint, request, jsonify
from models.dish_model import DishModel
from routes.dish_routes import dish_bp

# Get all dishes
@dish_bp.route("/", methods=["GET"])
def get_dishes():
    dishes = DishModel.get_all_dishes()
    return jsonify(dishes), 200

# Get single dish
@dish_bp.route("/<dish_id>", methods=["GET"])
def get_dish(dish_id):
    dish = DishModel.get_dish_by_id(dish_id)
    if dish:
        return jsonify(dish), 200
    return jsonify({"error": "Dish not found"}), 404

# Create new dish
@dish_bp.route("/", methods=["POST"])
def create_dish():
    data = request.json
    photo = data.get("photo")       # must match frontend
    name = data.get("name")         # must match frontend
    quantity = data.get("quantity")
    price = data.get("price")
    available = data.get("available", True)

    if not name or quantity is None or price is None:
        return jsonify({"error": "Missing required fields"}), 400

    new_dish = DishModel.create_dish(photo, name, int(quantity), float(price), available)
    return jsonify(new_dish), 201

# Update dish
@dish_bp.route("/<dish_id>", methods=["PUT"])
def update_dish(dish_id):
    dish = DishModel.get_dish_by_id(dish_id)
    if not dish:
        return jsonify({"error": "Dish not found"}), 404

    data = request.json
    updates = {
        "name": data.get("name", dish.get("name")),
        "quantity": int(data.get("quantity", dish.get("quantity"))),
        "price": float(data.get("price", dish.get("price"))),
        "available": data.get("available", dish.get("available")),
        "photo": data.get("photo", dish.get("photo"))
    }

    updated = DishModel.update_dish(dish_id, updates)
    return jsonify(updated), 200

# Delete dish
@dish_bp.route("/<dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    deleted = DishModel.delete_dish(dish_id)
    return jsonify(deleted), 200
