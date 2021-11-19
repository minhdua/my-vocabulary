import firebase_admin
from firebase_admin import credentials
# from firebase_admin import db
from firebase_admin import firestore


class FireStore:

    def __init__(self):
        self.app_path = './connections/firebase-sdk.json'

    def connect(self):
        cred = credentials.Certificate(self.app_path)
        firebase_admin.initialize_app(cred)
        return firestore.client()
