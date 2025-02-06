// Assignment 4.2 MongoDB Queries by Dua Hasan
// Date: 02/05/2025

// 1. a. Add a new user to the collection

db.users.insertOne({
    firstName: "Mary",
    lastName: "Smith",
    employeeId: "1013",
    email: "msmith@me.com"
  });
  
  // To prove the new user was added, we retrieve all users from the collection
  db.users.find({});
  
  // 2. b. Update Mozart's email address to 'mozart@me.com
  db.users.updateOne(
    { firstName: "Wolfgang", lastName: "Mozart" },  // Find Mozart's document
    { $set: { email: "mozart@me.com" } }  // Set the new email address
  );
  
  // Prove the update was successful by retrieving Mozart's document
  db.users.find({ firstName: "Wolfgang", lastName: "Mozart" });
  
  // 3. c. Display all users with first name, last name, and email address
  db.users.find({}, { firstName: 1, lastName: 1, email: 1, _id: 0 });
  