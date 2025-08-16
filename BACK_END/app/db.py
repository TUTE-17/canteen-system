

from supabase_init import supabase


def insert_data(table_name: str, data: dict):
    """Insert a single row into a table"""
    return supabase.table(table_name).insert(data).execute()


def get_all(table_name: str):
    """Fetch all rows from a table"""
    return supabase.table(table_name).select("*").execute()


def get_where(table_name: str, column: str, value):
    """Fetch rows where column = value"""
    return supabase.table(table_name).select("*").eq(column, value).execute()


def update_data(table_name: str, match_column: str, match_value, new_data: dict):
    """Update rows matching the condition"""
    return supabase.table(table_name).update(new_data).eq(match_column, match_value).execute()


def delete_data(table_name: str, match_column: str, match_value):
    """Delete rows matching the condition"""
    return supabase.table(table_name).delete().eq(match_column, match_value).execute()

def upload_file(bucket_name: str, file_path: str, dest_file_name: str):
    """Upload file to Supabase storage bucket"""
    with open(file_path, "rb") as f:
        res = supabase.storage.from_(bucket_name).upload(dest_file_name, f)
    return res


def get_file_url(bucket_name: str, file_name: str):
    """Get public URL of a file"""
    return supabase.storage.from_(bucket_name).get_public_url(file_name)
