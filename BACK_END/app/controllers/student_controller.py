from flask import jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from models.student_model import regno_or_email_exists, create_student, get_student_by_regno_or_email
from routes.student_routes import stud_bp
from utils.auth_utils import create_token
from supabase_init import supabase

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

        # Check if regno or email already exists
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
        return jsonify({"success": False, "message": str(e)}), 500


@stud_bp.route('/login', methods=['POST'])
def student_login():
    try:
        data = request.get_json(force=True)
        identifier = data.get('identifier', '').strip()  # can be regno or email
        password = data.get('password', '').strip()

        
        student = get_student_by_regno_or_email(identifier)
        if not student:
            return jsonify({"success": False, "message": "Student not found"}), 404

        
        if not check_password_hash(student['password'], password):
            return jsonify({"success": False, "message": "Invalid credentials"}), 401

        token = create_token(student['name'], "student")
        return jsonify({"success": True, "message": "Login successful", "token": token}), 200

    except Exception as e:
        import traceback
        print("Exception in login:\n", traceback.format_exc())
        return jsonify({"success": False, "message": str(e)}), 500



@stud_bp.route('/forgot-password', methods=['POST'])
def forgot_password():
    data = request.get_json()
    email = data.get("email", "").strip()

    if not email:
        return jsonify({"success": False, "message": "Email is required"}), 400

    try:
        redirect_url = "http://127.0.0.1:5000/student/reset-password"  
        supabase.auth.reset_password_for_email(
            email,
            options={"redirect_to": redirect_url}
        )

        return jsonify({"success": True, "message": "Password reset link sent to your email."}), 200
    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500