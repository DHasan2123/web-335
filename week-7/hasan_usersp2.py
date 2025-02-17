"""
Title: hasan_usersp2.py
Author: Dua Hasan
Date: 16 February 2025
Description: A Python program to perform CRUD operations on MongoDB's web335DB database.
"""

from pymongo import MongoClient
import datetime

# Build a connection string to connect to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Configure a variable to access the web335DB
db = client['web335DB']

# 1. Create a new user document
user_data = {
    "firstName": "John",
    "lastName": "Doe",
    "employeeId": "1024",
    "email": "johndoe@me.com",
    "dateCreated": datetime.datetime.utcnow()
}

# Insert the document into the users collection
new_user_id = db.users.insert_one(user_data).inserted_id
print(f"New User Inserted with ID: {new_user_id}")

# 2. Prove the document was created by searching for the document
created_user = db.users.find_one({"employeeId": "1024"})
print("Document after creation:")
print(created_user)

# 3. Update the email address of the user document
db.users.update_one(
    {"employeeId": "1024"},
    {
        "$set": {
            "email": "john.doe@newemail.com"
        }
    }
)

# 4. Prove the document was updated by searching the collection
updated_user = db.users.find_one({"employeeId": "1024"})
print("Document after update:")
print(updated_user)

# 5. Delete the document that was created
delete_result = db.users.delete_one({"employeeId": "1024"})
print(f"Deleted Document Result: {delete_result.deleted_count} document(s) deleted.")

# 6. Prove the document was deleted by searching the collection
deleted_user = db.users.find_one({"employeeId": "1024"})
print("Document after deletion:")
print(deleted_user)  # This should print None as the document was deleted
