from supabase_init import supabase

def regno_or_email_exists(regno, email):
    """Check if a regno or email already exists in the students table."""
    try:
        regno_check = supabase.table('students').select('regno').eq('regno', regno).limit(1).execute()
        if regno_check.data:
            return "regno"

        email_check = supabase.table('students').select('email').eq('email', email).limit(1).execute()
        if email_check.data:
            return "email"

        return None
    except Exception as e:
        print("Error in regno_or_email_exists:", e)
        raise

def create_student(student_data):
    """Insert a new student record into the table."""
    try:
        response = supabase.table('students').insert(student_data).execute()
        if response.data:
            return response.data
        else:
            raise Exception("Failed to insert student")
    except Exception as e:
        print("Error in create_student:", e)
        raise

def get_student_by_regno_or_email(identifier):
    """Fetch a student by regno or email for login."""
    try:
        response = supabase.table('students')\
            .select('*')\
            .or_(f"regno.eq.{identifier},email.eq.{identifier}")\
            .limit(1)\
            .execute()
        if not response.data:
            return None
        return response.data[0]
    except Exception as e:
        print("Error in get_student_by_regno_or_email:", e)
        raise
