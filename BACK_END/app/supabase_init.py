from supabase import create_client
from config import SUPABASE_URL, SUPABASE_KEY
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)