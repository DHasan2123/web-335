/**
 * Query to display all users in the 'users' collection.
 */
db.users.find({})

/**
 * Query to display the user with the email 'jbach@me.com'
 */
db.users.find({ email: "jbach@me.com" })

/**
 * Query to display the user with the last name 'Mozart'
 */
db.users.find({ lastName: "Mozart" })

/**
 * Query to display the user with the first name 'Richard'
 */
db.users.find({ firstName: "Richard" })

/**
 * Query to display the user with employeeId 1010
 */
db.users.find({ employeeId: "1010" })
