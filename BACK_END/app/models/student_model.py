from supabase_init import supabase

def regno_or_email_exists(regno, email):
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
    try:
        is_email = "@" in str(identifier)
        if is_email:
            resp = supabase.table('students').select('*').eq('email', identifier).limit(1).execute()
            if resp.data:
                return resp.data[0]

        response = supabase.table('students') \
            .select('*') \
            .or_(f"regno.eq.{identifier},email.eq.{identifier}") \
            .limit(1) \
            .execute()

        if not response.data:
            return None
        return response.data[0]
    except Exception as e:
        print("Error in get_student_by_regno_or_email:", e)
        raise





def debug_email_lookup(identifier):
    try:
        identifier = identifier.strip()
        response = supabase.table("students").select("email").eq("email", identifier).execute()
        print("Lookup result:", response.data)
        return response.data
    except Exception as e:
        print("Error in debug_email_lookup:", e)
        return []



def update_student_password(identifier, new_hashed_password):
    try:
        email = identifier.strip()
        response = (supabase.table("students")
                    .update({"password": new_hashed_password})
                .eq("email", identifier) 
                .execute())
        
        if response.data:
            print("Password updated successfully:", response.data)
            return True
        else:
            print("No student found with identifier:", identifier)
            return False

    except Exception as e:
        print("Error in update_student_password:", e)
        return False
