from flask import Flask, request, jsonify
from models.staff_model import  staff_id_exists, create_staff, get_staff_by_id
import bcrypt
from routes.staff_routes import staff_bp

@staff_bp.route('/signup', methods=['POST'])
def staff_signuppage():
    data = request.get_json(force=True)
    id = data.get('id', '').strip()
    name = data.get('name', '').strip()
    phone = data.get('phone', '').strip()
    password = data.get('password', '')

    if not id or not name or not phone or not password :
        return jsonify({"error": "Please fill all fields."}), 400

    if staff_id_exists(id):
        return jsonify({"error": "Staff ID already registered."}), 409

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

    staff_data = {
        "id": id,
        "name": name,
        "phone": phone,
        "password_hash": hashed_password
    }

    staff = create_staff(staff_data)
    return jsonify({"message": "Staff registered successfully.", "staff": staff}), 201

@staff_bp.route('/login', methods=['POST'])
def staff_loginpage():
    data = request.json
    id = data.get('id', '').strip()
    password = data.get('password', '')

    if not id or not password:
        return jsonify({"error": "Please provide staff ID and password"}), 400

    staff = get_staff_by_id(id)
    if not staff:
        return jsonify({"error": "Staff not found"}), 404

    stored_hash = staff.get('password_hash', '').encode('utf-8')
    if not bcrypt.checkpw(password.encode('utf-8'), stored_hash):
        return jsonify({"error": "Incorrect password"}), 401

    return jsonify({
        "message": f"Welcome, {staff['name']}!",
        "staff": {
            "id": staff['id'],
            "name": staff['name'],
            "phone": staff['phone']
        }
    }), 200

