import firebase_admin
from firebase_admin import credentials

path=credentials.Certificate("firebase_sdk.json")
firebase_admin.initialize_app(path)

