

from supabase_init import supabase


def insert_data(table_name: str, data: dict):

    return supabase.table(table_name).insert(data).execute()


def get_all(table_name: str):
    return supabase.table(table_name).select("*").execute()


def get_where(table_name: str, column: str, value):
    
    return supabase.table(table_name).select("*").eq(column, value).execute()


def update_data(table_name: str, match_column: str, match_value, new_data: dict):
    
    return supabase.table(table_name).update(new_data).eq(match_column, match_value).execute()


def delete_data(table_name: str, match_column: str, match_value):
    
    return supabase.table(table_name).delete().eq(match_column, match_value).execute()

def upload_file(bucket_name: str, file_path: str, dest_file_name: str):
  
    with open(file_path, "rb") as f:
        res = supabase.storage.from_(bucket_name).upload(dest_file_name, f)
    return res


def get_file_url(bucket_name: str, file_name: str):
   
    return supabase.storage.from_(bucket_name).get_public_url(file_name)
