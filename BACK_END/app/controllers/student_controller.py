from flask import jsonify, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from models.student_model import  regno_or_email_exists, create_student,get_student_by_regno_or_email,update_student_password
from routes.student_routes import stud_bp
from utils.auth_utils import create_token
import secrets

@stud_bp.route('/signup', methods=['POST'])
def student_signup():
    try:
        data = request.get_json(force=True)
        regno = data.get('regno', '').strip()
        name = data.get('name', '').strip()
        year = data.get('year', '').strip()
        department = data.get('department', '').strip()
        email = data.get('email', '').strip()
        password = data.get('password', '').strip()

        if not all([regno, name, year, department, email, password]):
            return jsonify({"success": False, "message": "All fields are required"}), 400

        exists = regno_or_email_exists(regno, email)
        if exists == "regno":
            return jsonify({"success": False, "message": "Registration number already exists!"}), 400
        if exists == "email":
            return jsonify({"success": False, "message": "Email already exists!"}), 400

        hashed_password = generate_password_hash(password)
        student_data = {
            "regno": regno,
            "name": name,
            "year": year,
            "department": department,
            "email": email,
            "password": hashed_password
        }
        create_student(student_data)

        token = create_token(name, "student")
        return jsonify({"success": True, "message": "Signup successful!", "token": token}), 200

    except Exception as e:
        import traceback
        print("Exception in signup:\n", traceback.format_exc())
        return jsonify({"success": False, "message": "Signup failed"}), 500



@stud_bp.route('/login', methods=['POST'])
def student_login():
    try:
        data = request.get_json(force=True)
        identifier = data.get('identifier', '').strip()  
        password = data.get('password', '').strip()

        if not identifier or not password:
            return jsonify({"success": False, "message": "Identifier and password are required"}), 400

        student = get_student_by_regno_or_email(identifier)
        if not student:
            return jsonify({"success": False, "message": "Student not found"}), 404

        if not check_password_hash(student['password'], password):
            return jsonify({"success": False, "message": "Invalid credentials"}), 401

        token = create_token(student['name'], "student")
        return jsonify({
            "success": True,
            "message": "Login successful",
            "student_regno": student.get("regno"),
            "token": token
        }), 200

    except Exception as e:
        import traceback
        print("Exception in login:\n", traceback.format_exc())
        return jsonify({"success": False, "message": "Login failed"}), 500



reset_tokens = {}  

@stud_bp.route('/forgot-password', methods=['POST'])
def handle_forgot_password():
    """
    JSON body: { "email": "user@example.com" }
    Response: { success, message, reset_link }
    """
    try:
        data = request.get_json(force=True)
        email = data.get("email", "").strip()

        if not email:
            return jsonify({"success": False, "message": "Email is required"}), 400

        student = get_student_by_regno_or_email(email)
        if not student:
            return jsonify({"success": False, "message": "No student found with this email"}), 404

        token = secrets.token_urlsafe(32)
        reset_tokens[token] = student["email"]

        reset_link = url_for("student.reset_password_page", _external=True) + f"?token={token}"
        return jsonify({"success": True, "message": "Password reset link generated.", "reset_link": reset_link}), 200

    except Exception as e:
        import traceback
        print("Exception in forgot-password:\n", traceback.format_exc())
        return jsonify({"success": False, "message": "Unable to generate reset link"}), 500


@stud_bp.route('/reset-password', methods=['POST'])
def handle_reset_password():
    """
    JSON body: { "token": "...", "new_password": "...", "confirm_password": "..." }
    """
    try:
        data = request.get_json(force=True)
        token = data.get("token")
        new_password = data.get("new_password")
        confirm_password = data.get("confirm_password")

        if not token or token not in reset_tokens:
            return jsonify({"success": False, "message": "Invalid or expired reset link"}), 400

        if not new_password or not confirm_password:
            return jsonify({"success": False, "message": "Password fields are required"}), 400

        if new_password != confirm_password:
            return jsonify({"success": False, "message": "Passwords do not match"}), 400

        email = reset_tokens[token]
        hashed_password = generate_password_hash(new_password)

        update_student_password(email, hashed_password)

        del reset_tokens[token]

        return jsonify({"success": True, "message": "Password reset successful"}), 200

    except Exception as e:
        import traceback
        print("Exception in reset-password:\n", traceback.format_exc())
        return jsonify({"success": False, "message": "Password reset failed"}), 500
