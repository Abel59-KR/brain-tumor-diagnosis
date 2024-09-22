from dbco import mycursor
def signup(username, email, password):
    # Query database to check if the provided credentials are valid
    query = "SELECT * FROM users WHERE UserId = %s AND password = %s"
    mycursor.execute(query, (username,email,password))
    new = mycursor.fetchone()
    return new