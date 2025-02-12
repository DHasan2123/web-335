# Filename: hasan_usersp1.py
# Author: Dua Hasan
# Date: 02/11/2025
# Description: MongoDB program to perform CRUD operations on the users collection.

from pymongo import MongoClient

# Build the connection string to connect to MongoDB
client = MongoClient("mongodb+srv://web335_user:s3cret@cluster0.lujih.mongodb.net/web335DB?retryWrites=true&w=majority")

# Configure a variable to access the web335DB database
db = client['web335DB']

# 4. Display all documents in the users collection
def display_all_users():
    print("Displaying all users:")
    for user in db.users.find({}, {"firstName": 1, "lastName": 1, "employeeId": 1, "email": 1}):
        print(user)

# 5. Display a document where employeeId is 1011
def find_user_by_employeeId(employee_id):
    print(f"\nDisplaying user with employeeId {employee_id}:")
    user = db.users.find_one({"employeeId": employee_id})
    print(user)

# 6. Display a document where lastName is Mozart
def find_user_by_lastName(last_name):
    print(f"\nDisplaying user with lastName {last_name}:")
    user = db.users.find_one({"lastName": last_name})
    print(user)

# Main function to call the functions
def main():
    display_all_users()
    find_user_by_employeeId("1011")
    find_user_by_lastName("Mozart")

# Execute the main function
if __name__ == "__main__":
    main()
