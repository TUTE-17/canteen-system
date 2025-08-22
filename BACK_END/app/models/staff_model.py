from supabase_init import supabase

def staff_id_exists(id: str) -> bool:
    try:
        res = supabase.table('staff').select('id').eq('id', id).limit(1).execute()
        return bool(res.data)
    except Exception as e:
        print("Error checking staff_id existence:", e)
        raise

def create_staff(staff_data: dict):
    try:
        response = supabase.table('staff').insert(staff_data).execute()
        print("Insert response:", response)
        if hasattr(response, 'error') and response.error:
            print("Supabase error:", response.error)
            raise Exception(response.error.message)
    
        if hasattr(response, 'status_code') and response.status_code != 201:
            raise Exception(f"Insert failed with status code: {response.status_code}")

        
        if hasattr(response, 'data') and response.data:
            return response.data[0]
    
        elif hasattr(response, 'json') and 'data' in response.json():
            return response.json()['data'][0]

    
    except Exception as e:
        print("Error in create_staff:", e)
        raise


def get_staff_by_id(id: str):
    try:
        response = supabase.table('staff').select('*').eq('id', id).limit(1).execute()
        if not response.data:
            return None
        return response.data[0]
    except Exception as e:
        print("Error in get_staff_by_id:", e)
        raise
