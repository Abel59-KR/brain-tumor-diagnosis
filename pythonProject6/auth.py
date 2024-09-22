from dbco import mycursor
def login(UserId, password):
    # Query database to check if the provided credentials are valid
    query = "SELECT * FROM users WHERE UserId = %s AND password = %s"
    mycursor.execute(query, (UserId, password))
    users = mycursor.fetchone()
    return users