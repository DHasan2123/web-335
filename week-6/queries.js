// Load the houses.js script to initialize collections and data
load("houses.js");

// a. Display all students
print("Displaying all students:");
db.students.find();

// b. Add a new student
print("Adding a new student:");
db.students.insertOne({
  "firstName": "John",
  "lastName": "Doe",
  "studentId": "s1019",
  "houseId": "h1007"  // Gryffindor house
});
print("New student added:");
db.students.find({ "studentId": "s1019" });

// c. Update one of the properties from the student you added
print("Updating the last name of John Doe:");
db.students.updateOne(
  { "studentId": "s1019" },
  { $set: { "lastName": "Smith" } }
);
print("Updated student:");
db.students.find({ "studentId": "s1019" });

// d. Delete the student you created
print("Deleting the student John Doe:");
db.students.deleteOne({ "studentId": "s1019" });
print("Student deleted:");
db.students.find({ "studentId": "s1019" });

// e. Display all students by house
print("Displaying all students by house:");
db.students.aggregate([
  { $lookup: {
    from: "houses",
    localField: "houseId",
    foreignField: "houseId",
    as: "houseDetails"
  }},
  { $unwind: "$houseDetails" },
  { $group: {
    _id: "$houseDetails.houseId",
    houseName: { $first: "$houseDetails.mascot" },
    students: { $push: { firstName: "$firstName", lastName: "$lastName" } }
  }},
  { $sort: { _id: 1 } }
]);

// f. Display all students in house Gryffindor
print("Displaying all students in Gryffindor:");
db.students.aggregate([
  { $lookup: {
    from: "houses",
    localField: "houseId",
    foreignField: "houseId",
    as: "houseDetails"
  }},
  { $unwind: "$houseDetails" },
  { $match: { "houseDetails.houseId": "h1007" } },
  { $project: { firstName: 1, lastName: 1 } }
]);

// g. Display all students in the house with an Eagle mascot (Ravenclaw)
print("Displaying all students in the house with an Eagle mascot (Ravenclaw):");
db.houses.find({ "mascot": "Eagle" }).forEach(function(house) {
  db.students.find({ "houseId": house.houseId })
});
